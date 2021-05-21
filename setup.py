#!/usr/bin/env python
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='polaris_api',
    version='0.1.5',
    author='VyStar',
    author_email='support@vystar.com',
    description='polaris_api is an API framework built to track and manage VyStar ML model lifecycle'
                'using MLFlow.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://vcuvs.visualstudio.com/ADA_Insight/_git/AAG_Polaris',
    install_requires=open('core-requirements.txt').readlines() + open('requirements.txt').readlines()[1:],
    tests_require=open('test-requirements.txt').readlines(),
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
          'polaris_api = polaris_api.__main__:cli'
        ]
    },
    data_files=[],
)