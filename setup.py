"""Setup for data structures."""
from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-cov', 'tox', 'faker']
}

setup(
    name='Data structures',
    description='Python implementation of various data structures.',
    version='1.0',
    author='Chris Hudson, Carlos Cadena',
    author_email='c.ahudson84@yahoo.com, cs.cadena@gmail.com',
    license='MIT',
    py_modules=['trie', 'bubble_sort', 'insert_sort',
                'merge_sort', 'quick_sort'],
    package_dir={'': 'src/working'},
    install_requires=[],
    extras_require=extra_packages,
    entry_points={}
)
