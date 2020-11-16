"""Setup module for Robot Framework Windows Remote Library."""

# To use a consistent encoding
# from codecs import open
# from os import path

import setuptools


with open("README.MD", "r") as fh:
    long_description = fh.read()

# Get install requires from requirements.txt
with open('requirements.txt') as f:
    install_requires = f.read().strip().splitlines()

setuptools.setup(
    name="WINRMAdapter",
    version="1.0.0",
    author="Matt Harvey",
    author_email="matt.2.harvey@bt.com",
    description="Robot Framework library for Windows Remote Management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(), 
    install_requires=install_requires,
    setup_requires=install_requires,
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent", 
        "Topic :: Software Development :: Testing",
        "Framework :: Robot Framework :: Library",
    ],
        
)
