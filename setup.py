from setuptools import setup, find_packages

setup(
    name="nextcord_jukebox",
    version="0.0.1",
    packages=find_packages(),
    author="Rystal-Team",
    author_email="code@rystal.xyz",
    description="A lightweight Python library for Nextcord music bot.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Rystal-Team/Nextcord-JukeBox",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests",
        "xmltodict",
    ],
)
