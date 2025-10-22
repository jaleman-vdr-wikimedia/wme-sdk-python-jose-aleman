"""Setup script for the wme-sdk-python package.

This file uses setuptools to define the project's metadata, find all
necessary packages, and specify its dependencies. Running this script
(e.g., `pip install .`) will install the SDK and its requirements.
"""

from setuptools import setup, find_packages

setup(
    name="wme-sdk-python",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "matplotlib==3.10.0",
        "pandas==2.2.3",
        "pytest==8.3.3",
        "python-dotenv==1.0.1",
        "requests==2.32.3",
    ],
    extras_require={
        "dev": ["pytest"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
