from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "autormd",
    version = "4.1",
    scripts=['autormd/autormd'],
    keywords = "example documentation tutorial",
    packages=['autormd'],
    long_description=read('README'),
    data_files=[(os.env['HOME'] + '/Documents/inf', ['inf/doc_header', 'inf/essay_header']),
                (os.env['HOME'] + '/Documents/src', ['src/main.rmd'])],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
