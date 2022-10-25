from setuptools import setup
from searcher.version import __version__
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='duples_searcher',
    version=__version__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='Search information about duplicates in files',
    author='Evgeny Dmitriev',
    author_email="zenka712@mail.ru",
    download_url='https://github.com/MBHuman/duples_searcher/archive/refs/tags/' + __version__ + '.tar.gz',
    url='https://github.com/MBHuman/duples_searcher',
    install_requires=[
        'pydantic==1.10.2'
    ],
    license="MIT",
    packages=['searcher', 'searcher.models', 'searcher.enums'],
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