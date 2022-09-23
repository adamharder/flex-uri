#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="flexuri",
    description="A simple URI scheme to abstract away blobstores (S3, Azure, local file, ect).",
    long_description=open("README.md").read().strip(),
    long_description_content_type="text/markdown",
    keywords=["flexuri"],
    license="MIT",
    version="0.1",
    packages=find_packages(
        include=[
            "FlexUri",
        ]
    ),
    url="https://github.com/adamharder/flex-uri",
    project_urls={
        "Changes": "https://github.com/adamharder/flex-uri/releases",
        "Code": "https://github.com/adamharder/flex-uri",
        "Issue tracker": "https://github.com/adamharder/flex-uri/issues",
    },
    author="GrepBox Inc.",
    author_email="",
    python_requires=">=3.6",
    install_requires=[
        "deprecated>=1.2.3",
        "packaging>=20.4",
        'importlib-metadata >= 1.0; python_version < "3.8"',
    ],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    extras_require={
    },
)