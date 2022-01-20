import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="df3d",
    version="0.55",
    description="GUI and 3D pose estimation pipeline for tethered Drosophila.",
    author="Semih Gunel",
    author_email="gunelsemih@gmail.com",
    entry_points={
        "console_scripts": ["df3d = df3d.gui:main", "df3d-cli = df3d.cli:main"]
    },
    packages=setuptools.find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NeLy-EPFL/DeepFly3D",
    install_requires=[
        "PyQt5",
        "sklearn",
        "scipy<=1.2.1",
        "scikit-video",
        "scikit-image",
        "matplotlib",
        "opencv-python==4.2.0.32",
        "tqdm",
        "colorama",
        "progress",
        "pytorch_lightning",
        "torchvision",
        "pyba==0.12",
        "df2d==0.13",
    ],
)
