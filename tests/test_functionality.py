from pathlib import Path

import pytest
import image_intensities.intensities as cffi_compiled
import image_intensities.pure_python as pure_python
from image_intensities import Intensities
from constants import EXPECTED_SUMS_PNG, EXPECTED_SUMS_JPG
from constants import IMAGE_PATH_PNG, IMAGE_PATH_JPG
from constants import COMPARISON_DISTANCE




@pytest.mark.parametrize("png_intensities", [cffi_compiled.png_intensities, pure_python.png_intensities])
def test_png(png_intensities):
    expected = {  # https://derpibooru.org/api/v1/json/images/954482
        "ne": 10.513891063388744,
        "nw": 35.832628091300684,
        "se": 20.831389937866714,
        "sw": 20.76546499989676
    }
    assert expected == EXPECTED_SUMS_PNG  # just to keep it consistent across tests
    expected = Intensities(**EXPECTED_SUMS_PNG)

    result = png_intensities(IMAGE_PATH_PNG)
    assert result.compare(expected, distance=COMPARISON_DISTANCE) or result == expected
# end def


@pytest.mark.parametrize("jpg_intensities", [cffi_compiled.jpg_intensities, pure_python.jpg_intensities])
def test_jpeg(jpg_intensities):
    expected = {  # https://derpibooru.org/api/v1/json/images/2544057
      "ne": 8.46639,
      "nw": 8.284639,
      "se": 23.260085,
      "sw": 22.85193
    }
    assert expected == EXPECTED_SUMS_JPG  # just to keep it consistent across tests
    expected = Intensities(**expected)

    result = jpg_intensities(IMAGE_PATH_JPG)
    assert result.compare(expected, distance=COMPARISON_DISTANCE) or result == expected
# end def


@pytest.mark.parametrize("image_intensities", [cffi_compiled.image_intensities, pure_python.image_intensities])
def test_image_intensities_png(image_intensities):
    result = image_intensities(IMAGE_PATH_PNG)

    expected = Intensities(**EXPECTED_SUMS_PNG)
    assert result.compare(expected, distance=COMPARISON_DISTANCE) or result == expected
# end def


@pytest.mark.parametrize("image_intensities", [cffi_compiled.image_intensities, pure_python.image_intensities])
def test_jpeg_mime(image_intensities):
    result = image_intensities(IMAGE_PATH_JPG)

    expected = Intensities(**EXPECTED_SUMS_JPG)
    assert result.compare(expected, distance=COMPARISON_DISTANCE) or result == expected
# end def
