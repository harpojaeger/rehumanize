from setuptools import setup, find_packages

setup(
    name="rehumanize",
    version="0.1.0",
    description="make numbers sound cooler",
    # long_description=,
    author="Harpo jaeger",
    author_email="harpo.jaeger@gmail.com",
    url="https://github.com/harpojaeger/rehumanize",
    # license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
