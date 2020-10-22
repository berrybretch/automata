from setuptools import setup
from Cython.Build import cythonize

setup(
    name='naive_convolve',
    ext_modules=cythonize('src/naive_convolve.pyx'),
    zip_safe=False
)