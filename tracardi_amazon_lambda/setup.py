from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tracardi-amazon-lambda',
    version='0.1.2',
    description='The purpose of this plugin is to connect with amazon lambda',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Bartosz Dobrosielski`',
    author_email='bdobrosielski@edu.cdv.pl',
    packages=['tracardi_amazon_lambda'],
    install_requires=[
        'pydantic',
        'asyncio',
        'tracardi-plugin-sdk'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    keywords=['tracardi', 'plugin'],
    python_requires=">=3.8",
    include_package_data=True
)