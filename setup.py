from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

os.makedirs(os.environ['HOME'] + '/Documents/src')
os.makedirs(os.environ['HOME'] + '/Documents/inf')
os.makedirs(os.environ['HOME'] + '/Documents/cit')
os.makedirs(os.environ['HOME'] + '/Documents/pdf')

setup(
    name = "autormd",
    version = "4.1",
    scripts=['autormd/autormd'],
    keywords = "example documentation tutorial",
    packages=['autormd'],
    long_description=read('README'),
    data_files=[(os.environ['HOME'] + '/Documents/inf', ['inf/doc_header', 'inf/essay_header']),
                (os.environ['HOME'] + '/Documents/src', ['src/main.rmd'])],
    install_requires=[
        'click',
        'pathlib',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
