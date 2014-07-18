# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='ark-tweet-nlp',
    version='0.0.1',
    description='A wrapper of ARK Tweet NLP Tagger',
    long_description=open('README.md').read(),
    packages=find_packages(),
    include_package_data=True,
    keywords=[],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
