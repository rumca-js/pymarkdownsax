import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymarkdownsax",
    version="0.0.1",
    author="Piotr Zielinski",
    author_email="rozbujnik@gmail.com",
    description="MarkDown processing for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rumca-js/pymarkdownsax",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite="pymarkdownsax.tests.test_all",
)
