#!/usr/bin/env python

from setuptools import setup

setup(
    name='fastqc_pipeline',
    version='0.0.5',
    author='Peter Georgeson',
    author_email='peter.georgeson@unimelb.edu.au',
    packages=['src'],
    entry_points={
        'console_scripts': ['fastqc_pipeline = src.main:main']
    },
    url='https://github.com/supernifty/fastqc_pipeline',
    license='LICENSE',
    description='fastqc_pipeline is a demonstration pipeline based on Ruffus', 
    long_description=open('README.md').read(),
    install_requires=[
        "ruffus == 2.6.3",
        "pipeline_base == 1.0.0"
    ],
)
