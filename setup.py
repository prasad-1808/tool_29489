from setuptools import setup, find_packages
import codecs
import os

VERSION = '2.0.3'
DESCRIPTION = 'Tool to identify URL with cve-2023-29489 vulnerability'
LONG_DESCRIPTION = 'Tool to identify URL with cve-2023-29489 vulnerability'

# Setting up
setup(
    name="tool-29489",
    version=VERSION,
    scripts=['src/main.py'],
    author="Prasad D",
    author_email="<prasadd.1808@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
     entry_points={
        'console_scripts': [
            'tool-29489 = src.main:main',
        ],
    },
    install_requires=[],
    keywords=['python', 'url', 'cve', 'cve-2023', 'cve-2023-29489', 'vulnerabilty detection tool'],
    classifiers=[
    ]
)