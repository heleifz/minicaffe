# -*- coding: utf-8 -*-

from setuptools import setup, find_packages, extension
from Cython.Build import cythonize

optimize = extension.Extension('*', ["minica/optimize/*.pyx"])

setup(
    name = "minica",
    version = "0.0.1",
    author = "Lei He",
    author_email = "heleifz@126.com",
    description = ("Yet another neural net library. :)"),
    license = "MIT",
    keywords = "neural net machine learning",
    install_requires = ['scipy >= 0.12', 'numpy'],
    ext_modules = cythonize(optimize),
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
	"Topic :: Scientific/Engineering :: Artificial Intelligence",
	"License :: OSI Approved :: MIT License"
    ],
)
