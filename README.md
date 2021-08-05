# HEADLINE

the algorithmic overview is to convert the image into the yuv colorspace, drop the u and v components,
and then average the y component over 4 evenly-spaced rectangles on the image dimensions

# Docker
 
> ⚠️ Make sure you pull a recent release of the python docker image (even if it's an older python version!).
> Especially if you're getting errors complaining about a `png_set_longjmp_fn` function when you try to use it.
> As time of writing the 2-month old version did not work, but the newest releases (`python:3.6`: `6ac87e65b6d0`, `pythong:3.9`: `1b33974176a3`) ones have that fixed.  

```
# e.g. docker run --rm -it python:3.9 bash


# UNINSTALL OLD libpng LIBRARY
apt-get purge -y libpng-dev

# INSTALL UP TO DATE libpng LIBRARY
# https://geeksww.com/tutorials/libraries/libpng/installation/installing_libpng_on_ubuntu_linux.php
wget https://sourceforge.net/projects/libpng/files/libpng16/1.6.37/libpng-1.6.37.tar.gz/download?download -O libpng.tar.gz
tar xzf libpng.tar.gz
cd libpng-*/
./configure --prefix=/usr/local
make install
cd ..

# INSTALL THIS
git clone https://github.com/luckydonald/image_intensities_minimal_test.git
cd image_intensities_minimal_test/
python setup.py install
cd ..

# TEST
# test import
python -c"import image_intensities as it; print(it._intensities.ffi)"

# test with a png
python -c"from image_intensities import png_intensities; print(png_intensities('/image_intensities_minimal_test/tests/954482.png'))"
# see tests/test_functionality.py for the expected result.
```

# Mac OS:
```
brew install libpng
CPPFLAGS='-I/usr/local/include/' LDFLAGS='-L/usr/local/lib/' python setup.py install
```
