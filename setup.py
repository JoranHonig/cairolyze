import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

REQUIREMENTS = (HERE / "requirements.txt")

requirements = [x for x in map(str.strip, REQUIREMENTS.read_text().split("\n")) if x != ""]

setup(
    name="cairolyze",
    version="0.0.1",
    description="A cli tool to analyze cairo contracts",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/joranhonig/cairolyze",
    author="Joran Honig",
    author_email="joran.honig@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "cairolyze=cairolyze.cli:cairolyze",
        ]
    },
)
