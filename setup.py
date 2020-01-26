import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ez-cli",
    version="0.0.1",
    author="Harsh Verma",
    author_email="harsh376@gmail.com",
    description="A small cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harsh376/ez-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
