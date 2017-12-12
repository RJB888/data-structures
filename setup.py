"""."""

from setuptools import setup

setup(

    name='day of code',
    description='Day of code katas.',
    package_dir={'': 'src'},
    author='Robert Bronson',
    author_email='robert.j.bronson@gmail.com',
    py_modules=['_1s_0s_and_wildcards',
                'coordinates_validator',
                'grouped_by_commas',
                'simple_pig_latin'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']
    },
    entry_points={}

)
