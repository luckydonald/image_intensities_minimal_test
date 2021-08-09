from pathlib import Path

IMAGE_FOLDER = Path(__file__).parent

IMAGE_PATH_JPG = str(IMAGE_FOLDER / '2544057.jpg')
EXPECTED_SUMS_JPG = {  # https://derpibooru.org/api/v1/json/images/2544057
  "ne": 8.46639,
  "nw": 8.284639,
  "se": 23.260085,
  "sw": 22.85193
}

IMAGE_PATH_PNG = str(IMAGE_FOLDER / '954482.png')
EXPECTED_SUMS_PNG = {  # https://derpibooru.org/api/v1/json/images/954482
  "ne": 10.513891063388744,
  "nw": 35.832628091300684,
  "se": 20.831389937866714,
  "sw": 20.76546499989676
}

IMAGE_PATH_GIF = str(IMAGE_FOLDER / '791101.gif')
EXPECTED_SUMS_GIF = {  # https://derpibooru.org/api/v1/json/images/791101
  "ne": 60.06419984738461,
  "nw": 60.03048984451281,
  "se": 67.11382688943588,
  "sw": 64.52939786379487
}

COMPARISON_DISTANCE = 0.001
