#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convert the image into the yuv colorspace, drop the u and v components,
and then average the y component over 4 evenly-spaced rectangles on the
image dimensions that gives you a floating point number
"""

from PIL import Image
from PIL.Image import open

from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'

from .classes import Intensities, RGB, QuadrantSums

__all__ = ['classes', 'intensities', 'jpg_intensities', 'png_intensities', 'image_intensities']

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if


def rgb_sums(img: Image.Image, log_prefix="") -> QuadrantSums:
    width, height = img.size
    pixels = list(img.getdata())
    sums = QuadrantSums()
    log_counter = -1  # more efficient then i % 10 == 0
    log_interval = height // 10
    for i in range(height):
        log_counter += 1
        if log_counter == log_interval:
            logger.debug(f'{log_prefix}Processing line {i} of {width}x{height} px image.')
            log_counter = 0
        # end if
        for j in range(width):
            nw = (i <= height / 2) and (j <= width / 2)
            # noinspection PyShadowingNames
            ne = (i <= height / 2) and (j >= width / 2)
            # noinspection PyShadowingNames
            sw = (i >= height / 2) and (j <= width / 2)
            # noinspection PyShadowingNames
            se = (i >= height / 2) and (j >= width / 2)
            img.load()
            pixel = pixels[i * width + j]
            r, g, b = pixel[0], pixel[1], pixel[2]

            if nw:
                sums.nw.r += r
                sums.nw.g += g
                sums.nw.b += b
            # end if

            if ne:
                sums.ne.r += r
                sums.ne.g += g
                sums.ne.b += b
            # end if

            if sw:
                sums.sw.r += r
                sums.sw.g += g
                sums.sw.b += b
            # end if

            if se:
                sums.se.r += r
                sums.se.g += g
                sums.se.b += b
            # end if
        # end for
    # end for
    return sums
# end def


# noinspection PyShadowingBuiltins
def _calculate_luma(dim: int, sum: RGB):
    return (
       (sum.r / dim * 0.2126) +
       (sum.g / dim * 0.7152) +
       (sum.b / dim * 0.0772)
    ) / 3.0
# end def


def sums_to_luma(sums: QuadrantSums, img: Image.Image) -> Luma:
    width, height = img.size

    dim = max(width * height / 4.0, 1)

    return Intensities(
        nw=_calculate_luma(dim, sums.nw),
        ne=_calculate_luma(dim, sums.ne),
        sw=_calculate_luma(dim, sums.sw),
        se=_calculate_luma(dim, sums.se),
    )
# end def


def image_intensities(filename: str) -> Intensities:
    img = open(filename)
    result = rgb_sums(img)
    return sums_to_luma(result, img)
# end def


jpg_intensities = image_intensities
png_intensities = image_intensities
