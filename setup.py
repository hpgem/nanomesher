#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# To update the package version number, edit CITATION.cff
with open('CITATION.cff', 'r') as cff:
    for line in cff:
        if 'version:' in line:
            version = line.replace('version:', '').strip().strip('"')

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='nanomesh',
    version=version,
    description='Creates 3d meshes from microscopy experimental data',
    long_description=readme + '\n\n',
    author='Nicolas Renaud',
    author_email='n.renaud@esciencecenter.nl',
    url='https://github.com/hpgem/nanomesh',
    packages=[
        'nanomesh',
    ],
    include_package_data=True,
    license='Apache Software License 2.0',
    zip_safe=False,
    keywords='nanomesh',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'IPython!=7.23',  # 7.23 contains a bug that prevents matplotlib inline
        'ipywidgets',
        'itkwidgets',
        'matplotlib',
        'meshio',
        'numpy',
        'pyvista',
        'scikit-image',
        'scikit-learn',
        'trimesh',
        'open3d',  # 3d mesh simplification
        'rtree',  # soft dependency of trimesh
    ],
    extras_require={
        'develop': [
            # linting
            'isort',
            'pre-commit',
            'yapf',
            # testing
            'nbmake',
            'pytest',
            'pytest-cov',
            'pycodestyle',
            # documentation
            'recommonmark',
            'sphinx',
            'sphinx_rtd_theme',
        ],
        'with_pygalmesh': [
            'pygalmesh @ git+http://git@github.com/hpgem/pygalmesh',
        ],
    },
    data_files=[('citation/nanomesh', ['CITATION.cff'])])
