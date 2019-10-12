from setuptools import setup


NAME = 'wdog'
VERSION = '1.0.0'

with open('README.md', 'r') as fh:
    long_description = fh.read()


setup(
    name=NAME,
    version=VERSION,
    description='A File System Watch dog',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['wdog'],
    install_requires=['watchdog>=0.8.3'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Licence :: OSI Approved :: GNU General Public Licence v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
)
