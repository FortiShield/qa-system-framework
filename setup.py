# Copyright (C) 2024, Fortishield Inc.
# Created by Fortishield, Inc. <info@fortishield.github.io>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
from setuptools import setup, find_namespace_packages
import shutil
import glob


setup(
    name='fortishield-qa-framework',
    version='1.0.0',
    description='Fortishield testing utilities to help programmers automate tests',
    url='https://github.com/fortishield/fortishield-qa-framework',
    author='Fortishield',
    author_email='hello@fortishield.github.io',
    license='GPLv2',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    zip_safe=False
)

# Clean build files
shutil.rmtree('dist')
shutil.rmtree('build')
shutil.rmtree(glob.glob('src/*.egg-info')[0])
