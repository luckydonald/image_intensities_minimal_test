from pathlib import Path

import pytest
from image_intensities import png_intensities, Luma


@pytest.mark
def test_png(variant):
    expected = {  # https://derpibooru.org//api/v1/json/images/954482
      "ne": 10.513891063388744,
      "nw": 35.832628091300684,
      "se": 20.831389937866714,
      "sw": 20.76546499989676
    }
    expected = Luma(**expected)
    result = png_intensities(str(Path(__file__).parent / 'd94ymc6-7401014c-59fb-4a52-b314-8eed8172d33e.png'))
    assert result == expected
# end def