#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"
__date__ = "Apr 02, 2015"

from setuptools import setup, find_packages
import os
import setlinks

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-setlinks',
    version=setlinks.__version__,
    packages=find_packages(),
    # package_data={'setlinks.templates': ['*']},
    install_requires=['django>=1.5'],
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to conduct Web-based setlinks.',
    long_description=README,
    url='http://www.example.com/',
    author=setlinks.__author__,
    author_email=setlinks.__email__,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)