from setuptools import setup

# [...]

setup(
    # [...]
    entry_points={
        'console_scripts': ['dojo = dojo.app'],
    },
)