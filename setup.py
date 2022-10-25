from importlib.metadata import entry_points
from setuptools import setup


setup(
    name='duples_searcher',
    version='0.1.0',
    description='Search information about duplicates in files',
    author='Evgeny Dmitriev',
    install_requires=[
        'pydantic==1.10.2'
    ],
    packages=['searcher'],
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    entry_points={
        'console_scripts': [
            'duples_searcher = searcher.main:main'
        ]
    },
    include_package_data=True
)