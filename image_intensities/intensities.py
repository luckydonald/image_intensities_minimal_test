#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from luckydonaldUtils.logger import logging
from typing import List, Union, Tuple

from luckydonaldUtils.encoding import to_binary

__author__ = 'luckydonald'

# logger = logging.getLogger(__name__)
# if __name__ == '__main__':
#     logging.add_colored_handler(level=logging.DEBUG)
# # end if

# noinspection PyUnresolvedReferences
from ._intensities import ffi as __ffi, lib as __lib
from .classes import Intensities
from mimetypes import guess_type


class ErrorCode(Exception):
    error: int

    def __init__(self, *args, error=None, **kwargs):
        assert error is not None
        self.error = error
        super().__init__(*args, **kwargs)
    # end def
# end class


def _convert_struct_to_luma(struct) -> Intensities:
    """
    :raises ErrorCode: The library had an error.
    """
    if struct.error:
        raise ErrorCode(error=struct.error)
    # end if
    return Intensities(nw=struct.nw, ne=struct.ne, sw=struct.sw, se=struct.se)
# end def


def jpg_intensities(filename) -> Intensities:
    """
    :raises ErrorCode: The library had an error.
    """
    filename = to_binary(filename)
    result_struct = __lib.jpeg_intensities(filename)
    return _convert_struct_to_luma(result_struct)
# end def


def png_intensities(filename) -> Intensities:
    """
    :raises ErrorCode: The library had an error.
    """
    filename = to_binary(filename)
    result_struct = __lib.png_intensities(filename)
    return _convert_struct_to_luma(result_struct)
# end def


def pixel_array_intensities(
    pixels: Union[List[int], List[Tuple[int, int, int]]], *, width: int, height: int
) -> Intensities:
    """
    :param pixels: List of pixel values,
                   either a tuple of `(R, G, B)` integers (0-255)
                   or a continuous list of `R`, `G` and `B` values of pixels.
                   It has either `width x height` or `width x height x 3` elements respectively.
    :param width: width of the image, needed to figure out the quadrant a pixel is in.
    :param height: height of the image, needed to figure out the quadrant a pixel is in.
    :return: The calculated intensities in the quadrants.
    """
    assert len(pixels) == width * height or len(pixels) == width * height * 3
    # plaintext_buf = __ffi.new("unsigned char [{}]".format(plaintext_size))
    # __lib.crypto_kem_dec(plaintext_buf, ciphertext, secret_key)
    final_bytes = b''
    if all(isinstance(element, int) for element in pixels):
        final_bytes += bytes(pixels)
    else:
        # so we found at least one tuple, so we gonna process that manually.
        for element in pixels:
            if isinstance(element, tuple):
                # (r, g, b), (r, g, b), ...
                final_bytes += bytes(element)
            else:
                # r, g, b, r, g, b, ...
                assert isinstance(element, int)
                final_bytes += bytes([element])
            # end if
        # end for
    # end if

    return pixel_bytes_intensities(final_bytes, width=width, height=height)
# end if


def pixel_bytes_intensities(pixels: bytes, *, width: int, height: int) -> Intensities:
    """
    :param pixels: A binary stream of `R`, `G` and `B` values, repeated for every pixel.
                   Binary representation b'\0x255\0x255\0x255\0x255\0x255\0x255...' of pixel values.
                   It has a length of `width x height x 3`.
    :param width: width of the image, needed to figure out the quadrant a pixel is in.
    :param height: height of the image, needed to figure out the quadrant a pixel is in.
    :return: The calculated intensities in the quadrants.
    """

    # The function to call:
    """
    intensity_data buffer_intensities(raster_data data);
    """
    # The struct raster_data we need to fill:
    """
    typedef struct raster_data {
        uint32_t width;
        uint32_t height;
        rgb_pixel *pixels;
        int error;
    } raster_data;
    """
    raster_data = __ffi.new('raster_data', dict(width=width, height=height, pixels=[], error=0))
    rgb_pixels = __ffi.new("rgb_pixel*", width * height)  # allocate the array of rgb_pixels
    raster_data.pixels = rgb_pixels  # NOTE that everything returned by `ffi.new()` must be kept alive [in a python variable], so never write directly `raster_data.pixels = ffi.new(...)`!

    for i in range(width):
        for j in range(height):
            pixel_index = i * height + j
            # pillow style:
            # r = img[i, j][0]
            # g = img[i, j][1]
            # b = img[i, j][2]
            # binary style:
            r = pixels[pixel_index * 3 + 0]
            g = pixels[pixel_index * 3 + 1]
            b = pixels[pixel_index * 3 + 2]
            # now put that into our allocated struct pointer.
            rgb_pixels[pixel_index].r = r
            rgb_pixels[pixel_index].g = g
            rgb_pixels[pixel_index].b = b
        # end for
    # end for

    raster_data.rgb_pixel = rgb_pixels
    result_struct = __lib.buffer_intensities(raster_data)
    return _convert_struct_to_luma(result_struct)
# end def


def image_intensities(filename: str, *, _fallback_no_temporary_file: bool = True) -> Intensities:
    """
    In case it's neither png nor jpg, we load it into PIL. See `fallback_no_temporary_file` for what to do then.

    :param _fallback_no_temporary_file: Instead of directly sending the binary data to work with it, we convert it to a png and write that to a temporary file to then call the png version on it.
                                        This is an temporary feature toggle until the issues with the first approach are ironed out. At a later point, if you need that behaviour you should simply copy the code from below.
    :raises ErrorCode: The library had an error.
    :raises NotImplementedError: The file is not png/jpg.
    """
    (mime_type, encoding) = guess_type(filename)
    if mime_type == 'image/png':
        return png_intensities(filename)
    elif mime_type == 'image/jpeg':
        return jpg_intensities(filename)
    else:
        try:
            from PIL import Image
            img = Image.open(filename).convert('RGB')
            if _fallback_no_temporary_file:
                return pixel_bytes_intensities(pixels=img.tobytes(), width=img.width, height=img.height)
            else:
                from tempfile import NamedTemporaryFile
                with NamedTemporaryFile(prefix='converted', suffix='png') as f:
                    img.save(f.name)
                    return png_intensities(f.name)
                # end with
            # end if
        except ImportError:  # PIL/Pillow not found
            raise NotImplementedError(
                f'Unsupported mime, only `image/png` and `image/jpeg` are supported, got {mime_type}.'
            )
        # end try
    # end if
# end def
