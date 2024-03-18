#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='AI_In_Schools',
    version='1.0',
    description='AI in Schools Project',
    author='Nicole Wheeler',
    author_email='nwheeler443@gmail.com',
    packages=find_packages(where='utils'),  # This tells setuptools that your packages are under the 'utils' directory
    install_requires=[
        'biopython',
    ]
    )