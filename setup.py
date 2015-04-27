#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '030'

from setuptools import setup,find_packages
import codecs

from prproxy import __version__

#description = 'description'
#long_description = 'long_description'

setup(
    name='prproxy',
    version=__version__,
    #description=description,
    #long_description=long_description,

    author='030',
    author_email="root@030.io",
    url="https://github.com/030io/prproxy",
    license="MIT",

    #test_suite = 'test',

    packages=find_packages(),

    install_requires=[
        'tornado',
        'chardet',
    ],

    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ]
)
