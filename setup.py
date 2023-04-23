from setuptools import setup, find_packages

setup(
    name='app',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'numpy>=1.20.1',
        'pandas>=1.2.2'
    ]
)