#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
from os.path import dirname, abspath, join

with open('README.md') as file:
    long_ddescription = file.read()

ROOT = dirname(abspath(__file__))
requirements_dev = join(ROOT, 'requirements-dev.txt')
extras_require = {}
with open(requirements_dev) as file:
    extras_require['dev'] = [i.strip().split('#', 1)[0].strip()
                             for i in file.read().strip().split('\n')]

setup(
    name='AFD',
    version='1.0',
    description='AFD',
    author='Matheus Tirabassi',
    author_email='tirabassi.matheus@aluno.ifsp.edu.br',
    packages=find_packages(),  # same as name
    python_requires='>= 3.6',
    keywords='AFD',
    package_data={'': ['LICENSE', 'requirements-dev.txt', 'README.md']}
)
