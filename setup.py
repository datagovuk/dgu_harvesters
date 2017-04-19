#!/usr/bin/env python

from setuptools import setup, find_packages

install_requires = [
    'requests==2.13.0',
    'ckanapi==4.0',
    'lxml==3.7.3',
    'OWSLib==0.14.0',
    'dotmap==1.2.17',

    # Testing tools
    'mock==2.0.0',
    'nose==1.3.7',
    'requests-mock==1.3.0'
]


setup(
    name='DGU_Harvesters',
    version='1.0',
    description='Harvester library for data.gov.uk',
    author='Data Discovery Team',
    author_email='',
    url='https://github.com/datagovuk/dgu_harvesters',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    install_requires=install_requires,
)
