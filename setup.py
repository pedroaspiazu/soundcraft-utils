from setuptools import setup, find_packages
import re

version = re.search('^__version__\s*=\s*"(.*)"',
    open('soundcraft/__init__.py').read(),
    re.M).group(1)
 
with open("README.md", "rb") as fh:
    long_description = fh.read().decode("utf-8")

setup(
    name="soundcraft_utils",
    version=version,
    description="Soundcraft Notepad control utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jim Ramsay",
    author_email="i.am@jimramsay.com",
    url="https://github.com/lack/soundcraft-utils",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio :: Mixers",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pyusb",
    ],
    entry_points={
        "console_scripts": [
            "soundcraft_ctl=soundcraft:main",
        ],
    },
)