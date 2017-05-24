"""Setup for linked_list.py."""
from setuptools import setup

extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-watch', 'pytest-cov', 'tox']
}

setup(
    name='Data structures',
    desctription='Implements various data structures.',
    version='0.1',
    author='Chris Hudson, Morgan Nomura',
    author_email='c.ahudson84@yahoo.com, morganelle@gmail.com',
    license='MIT',
    py_modules=['linked_list'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require=extra_packages,
    entry_points={
        'console_scripts': [
            'linked_list = linked_list:main'
        ]
    }
)
