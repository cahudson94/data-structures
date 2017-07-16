"""Setup for data structures."""
from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-cov', 'tox']
}

setup(
    name='Data structures',
    description='Python implementation of various data structures.',
    version='0.1',
    author='Chris Hudson, Carlos Cadena',
    author_email='c.ahudson84@yahoo.com, cs.cadena@gmail.com',
    license='MIT',
    py_modules=['linked_list', 'doubly_linked_list',
                'stack', 'que_', 'deque', 'binheap',
                'priorityque', 'graph_1', 'graph_w',
                'bst'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require=extra_packages,
    entry_points={}
)
