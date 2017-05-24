"""Setup for http server."""
from setuptools import setup

dependencies = []
extra_packages = {
    'testing': ['ipython', 'pytest', 'pytest-cov', 'tox']
}

setup(
    name='http-server',
    description='Client sends message and server sends OK back.',
    version='0.1',
    author='Carlos Cadena, Chris Hudson',
    author_email='cs.cadena@gmail.com, c.ahudson84@yahoo.com',
    license='MIT',
    py_modules='client, server',
    package_dir={'': 'src'},
    install_requires=dependencies,
    extras_require=extra_packages,
    entry_points={}
)
