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
