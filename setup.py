import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name="pyimpute_geometric",
    version="0.0.2",
    author="Mel Mashiku",
    author_email="melchy.mashiku@gmail.com",
    description=("Utilities for applying scikit-learn to spatial datasets based on Matthew Perry's Pyimpute"),
    license="BSD",
    keywords="gis geospatial geographic raster vector zonal statistics machinelearning",
    url="https://github.com/mashiku7/pyimpute_geometric",
    package_dir={'': 'src'},
    packages=['pyimpute_geometric'],
    long_description=read('README.md'),
    install_requires=[
        'scikit-learn',
        'scipy',
        'numpy',
        'rasterstats',
        'rasterio'
    ],
    tests_require=['pytest', 'pyshp>=1.1.4', 'coverage'],
    cmdclass = {'test': PyTest},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: GIS',
    ],
)
