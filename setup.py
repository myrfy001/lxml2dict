# coding=utf-8
from setuptools import setup, find_packages
setup(
    name='lxml2dict',
    version='0.0.1',
    description='Convert lxml tree to python dict format with flexible namespace support.',
    long_description="Convert lxml tree to python dict format with flexible namespace support. Use loop structure instead of recursive structure to achieve a higher speed.",
    author='myrfy001',
    url='https://github.com/myrfy001/lxml2dict',
    license='Apache',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.6',
    ],
    keywords='lxml dict json',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[],
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={}
)
