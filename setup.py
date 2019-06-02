from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "autormd",
    version = "4.1",
    keywords = "example documentation tutorial",
    packages=['autormd'],
    long_description=read('README'),
    install_requires=[
        'click',
        'pathlib',
    ],
    entry_points={
        'console_scripts': ['autormd = autormd.cli:start']
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
