from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
if os.name == 'nt':
    setup(
        name = "autodocx",
        version = "0.1.0",
        keywords = "example documentation tutorial",
        packages=['autodocx', 'autodocx.formaters', 'autodocx.data'],
        long_description=read('README.md'),
        install_requires=[
            'click',
            'pathlib',
            'python-docx',
            'matplotlib',
            'pygments',
            'pypiwin32'
        ],
        entry_points={
            'console_scripts': ['autodocx = autodocx.cli:start']
        },
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Topic :: Utilities",
            "License :: OSI Approved :: BSD License",
        ],
        package_data={
            'autodocx': [
                'data/*'
            ],
        },
        include_package_data=True,
    )
else:
    setup(
        name = "autodocx",
        version = "0.1.0",
        keywords = "example documentation tutorial",
        packages=['autodocx', 'autodocx.formaters', 'autodocx.data'],
        long_description=read('README.md'),
        install_requires=[
            'click',
            'pathlib',
            'python-docx',
            'matplotlib',
            'pygments'
        ],
        entry_points={
            'console_scripts': ['autodocx = autodocx.cli:start']
        },
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Topic :: Utilities",
            "License :: OSI Approved :: BSD License",
        ],
    )
