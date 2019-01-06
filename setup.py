#!/usr/bin/env python
from setuptools import setup
setup(
    name='ghief',
    version='0.1.3',
    author='Matthias Lohr',
    author_email='matthias@lohr.me',
    description='Git Backup Script',
    packages=['ghief'],
    install_requires=['pyyaml>=4.2b1'],
    entry_points={
        'console_scripts': ['ghief=ghief.__main__:main']
    }
)
