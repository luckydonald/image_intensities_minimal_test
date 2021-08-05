# HEADLINE

the algorithmic overview is to convert the image into the yuv colorspace, drop the u and v components,
and then average the y component over 4 evenly-spaced rectangles on the image dimensions

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
python
from image_intensities import png_intensities
```

# Mac OS:
```
CPPFLAGS='-I/usr/local/include/' LDFLAGS='-L/usr/local/lib/' python setup.py install
```
