from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="youtube-suggestions",
    version="0.2.3",
    author="Ryan Huang",
    author_email="ryan@stdint.com",
    description="A package to get YouTube search suggestions with proxy support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryan-huang1/youtube_suggestions",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "requests>=2.25.1",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)