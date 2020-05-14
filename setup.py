import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-RichardPoulson", # Replace with your own username
    version="0.0.1",
    author="Richard Poulson",
    author_email="contact@RichardPoulson.com",
    description="Example package that uses the Flask web application framework.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RichardPoulson/python-flask",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)