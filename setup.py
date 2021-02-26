import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="awshelper",
    version="0.1.0",
    author="Samuel Judith",
    author_email="samjudith@gmail.com",
    description="AWS Utils - Common python helper for AWS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: MIT",
        "Development Status :: beta",
    ],
    python_requires=">=3.5",
    install_requires=["boto3", "packaging"],
    entry_points={
        'console_scripts': [
            'updateip=__main__:main',
        ],
    }
)
