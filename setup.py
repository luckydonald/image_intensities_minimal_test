#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
from setuptools import setup, find_packages


__author__ = 'luckydonald'

here = Path(__file__).parent.absolute()

with open(str(here / 'README.md')) as f:
    long_description = f.read()
# end with

with open(str(here / 'image_intensities/VERSION.txt')) as f:
    version = f.read().strip()
# end with

setup(
    name="image_intensities", version=version,
    description='Calculate image intensities, a database friendly alternative to image hashing..',
    long_description=long_description,
    long_description_content_type='text/markdown',
    cffi_modules=["build.py:intensities_ffi"],
    # The project's main homepage.
    url='https://github.com/luckydonald/image_intensities',
    project_urls={
        "Code": "https://github.com/luckydonald/image_intensities",
        "Issue tracker": "https://github.com/luckydonald/image_intensities/issues"
    },
    # Author details
    author='luckydonald',
    author_email='image_intensities+code@luckydonald.de',
    # Choose your license
    license='GPLv3+',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',  # 2 - Pre-Alpha, 3 - Alpha, 4 - Beta, 5 - Production/Stable
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Plugins',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        #'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.6',
        #'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: 3.7',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
    ],
    # What does your project relate to?
    keywords='image hash image hashing image intensities nw sw se ne derpibooru',
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=["tests"]),
    # packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    # List run-time dependencies here. These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        "cffi>=1.4.0",
        "luckydonald-utils>=0.73",  # general utils
        # "pytgbot>=4.1.1",  # telegram communication
    ],
    # https://cffi.readthedocs.io/en/latest/cdef.html
    setup_requires=["cffi>=1.4.0"],
    # List additional groups of dependencies here (e.g. development dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    # extras_require = {
    # 'dev': ['check-manifest'],
    # 'test': ['coverage'],
    # },
    # If there are data files included in your packages that need to be
    # installed, specify them here. If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    # 'sample': ['package_data.dat'],
    # },
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages.
    # see http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data'    , ['data/data_file'])],
    include_package_data=True,
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
)
