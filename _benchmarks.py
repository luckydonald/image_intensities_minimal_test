from timeit import timeit
import sys
from luckydonaldUtils.logger import logging

# # USAGE
# python _benchmarks.py /path/to/file.png
# python _benchmarks.py /path/to/file.png 1000

PNG_IMAGE_FILENAME = sys.argv[1]
TIMES = int(sys.argv[2]) if len(sys.argv) > 2 else 10


logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if

logger.info('Testing [cffi]...')
result_cffi = None
try:
    from image_intensities.intensities import png_intensities
    result_cffi = timeit(lambda: png_intensities(filename=PNG_IMAGE_FILENAME), number=TIMES)
    logger.success(f'Took {result_cffi}s:\n{result_cffi!r}')
except:
    logger.exception('Could not import/execute cffi.')
# end try

logger.info('Testing [pure_python]...')
result_pure_python = None
try:
    from image_intensities.pure_python import rgb_luma_from_filename as rgb_luma_from_filename_pure_python
    result_pure_python = timeit(lambda: rgb_luma_from_filename_pure_python(filename=PNG_IMAGE_FILENAME), number=TIMES)
    logger.success(f'Took {result_pure_python}:\n{result_pure_python!r}')
except:
    logger.exception('Could not import/execute pure_python.')
# end try



