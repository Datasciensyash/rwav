from pathlib import Path

from setuptools import find_packages, setup

THIS_DIR = Path(__file__).parent


setup(
    name="rwav",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "pyaudio",
    ],
    entry_points={
        "console_scripts": [
            "rwav=rwav.main:main",
        ],
    },
)