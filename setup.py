#!/usr/bin/env python

from setuptools import setup
import os
import yaml

# These get saved into version.py for use in the package:
with open('setup.yml') as f:
    cfg = yaml.safe_load(f)

# Write a "version.py" file containing version and author info:
with open(os.path.join('spacesystems', 'version.py'), 'w') as f:
    for key in cfg:
        f.write('__{}__ = "{}"\n'.format(key, cfg[key]))

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name = 'spacesystems',
    version = cfg['version'], 
    description = 'Tools for common space systems engineering problems', 
    long_description = long_description,
    author = cfg['author'],
    maintainer = 'Matt Dallas',
    license = 'MIT',
    keywords = ['astronomy'],
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 3.11',
                   'Operating System :: OS Independent',
                   'Intended Audience :: Science/Research',
                   'Topic :: Scientific/Engineering :: Astronomy',
                   'Topic :: Scientific/Engineering :: Physics',
                   'Topic :: Software Development :: Libraries :: Python Modules'],
    packages = ['spacesystems'],
    install_requires = ['setuptools', 'pyyaml', 'numpy', 'astropy', 'matplotlib', 'pandas', 'datetime', 'bs4'], 
)
