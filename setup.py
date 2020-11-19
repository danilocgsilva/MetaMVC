from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="metamvc",
    version=VERSION,
    description="Stores and admin mvc common data for web mvc frameworks project",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="mvc web development",
    url="https://github.com/danilocgsilva/MetaMVC",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["metamvc"],
    entry_points={"console_scripts": ["mmvc=metamvc.__main__:main"],},
    include_package_data=True
)

