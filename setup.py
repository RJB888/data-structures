"""."""

from setuptools import setup

setup(

    name='data structures',
    description='data structures',
    package_dir={'': 'src'},
    author='Robert Bronson',
    author_email='robert.j.bronson@gmail.com',
    py_modules=['insertion'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']
    },
    entry_points={}

)
