from setuptools import setup
from searcher.version import __version__


setup(
    name='duples_searcher',
    version='0.1.0',
    description='Search information about duplicates in files',
    author='Evgeny Dmitriev',
    download_url='https://github.com/MBHuman/duples_searcher/archive/refs/tags/' + __version__ + '.tar.gz',
    url='https://github.com/MBHuman/duples_searcher',
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