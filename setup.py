from os import path
from setuptools import setup, find_packages

with open(path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8") as handle:
    readme = handle.read()

setup(
    name="image-intensities_test",
    version="0.0.10.dev3",
    description="Blah.",
    long_description=readme,
    url="https://github.com/luckydonald/image_intensities",
    author="luckydonald",
    author_email="fooppppoo@example.com",
    license="GPL3+",
    packages=find_packages(exclude=["tests"]),
    setup_requires=["cffi>=1.4.0"],
    cffi_modules=["build.py:intensities_ffi"],
    install_requires=["cffi>=1.4.0", "luckydonald-utils"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: C",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Topic :: Utilities",
    ],
)
