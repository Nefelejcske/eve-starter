#!/usr/bin/env python

from setuptools import setup, find_packages

APPLICATION_DEPENDENCIES = ["Eve==0.8"]
TEST_DEPENDENCIES = ["pytest"]

setup_options = dict(
    name='my_awesome_app',
    version='0.0.1',
    packages=find_packages(exclude=["test/*"]),
    package_dir={'': 'src'},
    install_requires=APPLICATION_DEPENDENCIES,
    extras_require={"dev": TEST_DEPENDENCIES}
)

if __name__ == '__main__':
    setup(**setup_options)
