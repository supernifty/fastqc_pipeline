#!/usr/bin/env python

from setuptools import setup

setup(
    name='test_ruffus_pipeline',
    version='0.0.5',
    author='Bernie Pope, Khalid Mahmood, Jessica Chung',
    author_email='bjpope@unimelb.edu.au',
    packages=['src'],
    entry_points={
        'console_scripts': ['test_pipeline = src.main:main']
    },
    url='https://github.com/bjpop/test_ruffus_pipeline',
    license='LICENSE',
    description='test_ruffus_pipeline is a demonstration pipeline based on Ruffus', 
    long_description=open('README.md').read(),
    install_requires=[
        "ruffus == 2.6.3",
        "pipeline_base == 1.0.0"
    ],
)
