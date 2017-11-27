"""Setup file for data-structures package."""


from setuptools import setup


setup(
    name="data-structures",
    description="Python data structures.",
    author=["Robert Bronson", "Brendan Davis"],
    author_email=["robert.j.bronson@gmail.com",
                  "brendanmd@gmail.com"],
    license="MIT",
    py_modules=["deque"],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox', 'ipython'],
        'development': ['ipython']
    },
    entry_points={
    }
)
