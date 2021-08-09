from PIL import Image

import pytest
import image_intensities.intensities as cffi_compiled
import image_intensities.pure_python as pure_python
from constants import EXPECTED_SUMS_PNG, EXPECTED_SUMS_JPG
from constants import IMAGE_PATH_PNG, IMAGE_PATH_JPG
from constants import COMPARISON_DISTANCE


@pytest.mark.parametrize("pixel_bytes_intensities", [cffi_compiled.pixel_bytes_intensities, pure_python.pixel_bytes_intensities])
def test_pixel_bytes_intensities_png(pixel_bytes_intensities):
    img = Image.open(IMAGE_PATH_PNG).convert('RGB')
    result = pixel_bytes_intensities(pixels=img.tobytes(), width=img.width, height=img.height)
    assert result.compare(EXPECTED_SUMS_PNG, distance=COMPARISON_DISTANCE) or result == EXPECTED_SUMS_PNG
# end def


@pytest.mark.parametrize("pixel_bytes_intensities", [cffi_compiled.pixel_bytes_intensities, pure_python.pixel_bytes_intensities])
def test_pixel_bytes_intensities_jpeg(pixel_bytes_intensities):
    img = Image.open(IMAGE_PATH_JPG).convert('RGB')
    result = pixel_bytes_intensities(
        pixels=img.tobytes(),
        width=img.width,
        height=img.height,
    )
    assert result.compare(EXPECTED_SUMS_JPG, distance=COMPARISON_DISTANCE) or result == EXPECTED_SUMS_JPG
# end def


@pytest.mark.parametrize("pixel_bytes_intensities", [cffi_compiled.pixel_bytes_intensities, pure_python.pixel_bytes_intensities])
def test_pixel_bytes_intensities_png(pixel_bytes_intensities):
    img = Image.open(IMAGE_PATH_PNG).convert('RGB')
    result = pixel_bytes_intensities(
        pixels=img.tobytes(),
        width=img.width,
        height=img.height,
    )
    assert result.compare(EXPECTED_SUMS_PNG, distance=COMPARISON_DISTANCE) or result == EXPECTED_SUMS_PNG
# end def


@pytest.mark.parametrize("pixel_array_intensities", [cffi_compiled.pixel_array_intensities, pure_python.pixel_array_intensities])
def test_pixel_array_intensities__tuple_array__png(pixel_array_intensities):
    img = Image.open(IMAGE_PATH_PNG).convert('RGB')
    result = pixel_array_intensities(
        pixels=[img.getpixel((x, y)) for y in range(img.height) for x in range(img.width)],
        width=img.width,
        height=img.height,
    )
    assert result.compare(EXPECTED_SUMS_PNG, distance=COMPARISON_DISTANCE) or result == EXPECTED_SUMS_PNG
# end def


@pytest.mark.parametrize("pixel_array_intensities", [cffi_compiled.pixel_array_intensities, pure_python.pixel_array_intensities])
def test_pixel_array_intensities__tuple_array__jpg(pixel_array_intensities):
    img = Image.open(IMAGE_PATH_JPG).convert('RGB')
    result = pixel_array_intensities(
        pixels=[img.getpixel((x, y)) for y in range(img.height) for x in range(img.width)],
        width=img.width,
        height=img.height,
    )
    assert result.compare(EXPECTED_SUMS_JPG, distance=COMPARISON_DISTANCE) or result == EXPECTED_SUMS_JPG
# end def


@pytest.mark.parametrize("pixel_array_intensities", [cffi_compiled.pixel_array_intensities, pure_python.pixel_array_intensities])
def test_pixel_array_intensities__flat_array__png(pixel_array_intensities):
    img = Image.open(IMAGE_PATH_PNG).convert('RGB')
    pixels = []
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            pixels.append(r)
            pixels.append(g)
            pixels.append(b)
        # end for
    # end for

    result = pixel_array_intensities(
        pixels=pixels,
        width=img.width,
        height=img.height,
    )
    assert result.compare(EXPECTED_SUMS_PNG, distance=COMPARISON_DISTANCE) or result == EXPECTED_SUMS_PNG
# end def


@pytest.mark.parametrize("pixel_array_intensities", [cffi_compiled.pixel_array_intensities, pure_python.pixel_array_intensities])
def test_pixel_array_intensities__flat_array__png(pixel_array_intensities):
    img = Image.open(IMAGE_PATH_PNG).convert('RGB')
    pixels = []
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            pixels.append(r)
            pixels.append(g)
            pixels.append(b)
        # end for
    # end for

    result = pixel_array_intensities(
        pixels=pixels,
        width=img.width,
        height=img.height,
    )
    assert result.compare(EXPECTED_SUMS_PNG, distance=COMPARISON_DISTANCE) or result == EXPECTED_SUMS_PNG
# end def
