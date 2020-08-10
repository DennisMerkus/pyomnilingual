import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="omnilingual",
    version="0.2.1",
    author="Dennis Merkus",
    description="Language code/feature utilities.",
    long_description=long_description,
    url="https://github.com/DennisMerkus/pyomnilingual",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.8",
)
