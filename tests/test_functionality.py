from pathlib import Path

import pytest
import image_intensities.intensities as cffi_compiled
import image_intensities.pure_python as pure_python
from image_intensities import Intensities


@pytest.mark.parametrize("png_intensities", [cffi_compiled.png_intensities, pure_python.png_intensities])
def test_png(png_intensities):
    expected = {  # https://derpibooru.org/api/v1/json/images/954482
      "ne": 10.513891063388744,
      "nw": 35.832628091300684,
      "se": 20.831389937866714,
      "sw": 20.76546499989676
    }
    expected = Intensities(**expected)
    result = png_intensities(str(Path(__file__).parent / '954482.png'))
    assert result == expected
# end def


@pytest.mark.parametrize("jpg_intensities", [cffi_compiled.jpg_intensities, pure_python.jpg_intensities])
def test_jpeg(jpg_intensities):
    expected = {  # https://derpibooru.org/api/v1/json/images/2544057
      "ne": 8.46639,
      "nw": 8.284639,
      "se": 23.260085,
      "sw": 22.85193
    }
    expected = Intensities(**expected)
    result = jpg_intensities(str(Path(__file__).parent / '2544057.jpg'))
    assert result == expected
# end def


@pytest.mark.parametrize("image_intensities", [cffi_compiled.image_intensities, pure_python.image_intensities])
def test_image_intensities_png(image_intensities):
    expected = {  # https://derpibooru.org/api/v1/json/images/954482
      "ne": 10.513891063388744,
      "nw": 35.832628091300684,
      "se": 20.831389937866714,
      "sw": 20.76546499989676
    }
    expected = Intensities(**expected)
    result = image_intensities(str(Path(__file__).parent / '954482.png'))
    assert result == expected
# end def


@pytest.mark.parametrize("image_intensities", [cffi_compiled.image_intensities, pure_python.image_intensities])
def test_jpeg_mime(image_intensities):
    expected = {  # https://derpibooru.org/api/v1/json/images/2544057
      "ne": 8.46639,
      "nw": 8.284639,
      "se": 23.260085,
      "sw": 22.85193
    }
    expected = Intensities(**expected)
    result = image_intensities(str(Path(__file__).parent / '2544057.jpg'))
    assert result == expected
# end def
