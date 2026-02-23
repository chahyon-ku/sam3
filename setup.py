from setuptools import find_packages, setup

setup(
    name="sam3",
    packages=find_packages(include=["sam3*"]),
    install_requires=[
        "einops",
        "ftfy",
        "iopath",
        "timm",
        "pycocotools",
    ],
    version="0.1.0",
)
