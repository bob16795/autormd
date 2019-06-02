import click
import os,sys,re
import subprocess
import time
from .commands import _compile, _list, _add, _setup
from pathlib import Path


@click.group()
def main():
    """Document Manager"""


@main.command()
@click.option('--docdir', '-d', default=str(Path.home() / "Documents"),
        help="Directory of the documents (default=$home/Documents)")
@click.option('--cfgdir', '-c', default=str(Path.home() / "Documents" / "inf"),
        help="Directory of the configuration files (default=$home/Documents/inf)")
def setup(docdir, cfgdir):
    """sets up the config files"""
    _setup(docdir, cfgdir)

@main.command()
@click.option('--docdir', '-d', default=str(Path.home() / "Documents"),
        help="Directory of the documents (default=$home/Documents)")
@click.option('--cfgdir', '-c', default=str(Path.home() / "Documents" / "inf"),
        help="Directory of the configuration files (default=$home/Documents/inf)")
@click.argument('name')
@click.argument('section')
@click.argument('index', nargs=-1)
@click.option('--docdir', '-d', default=str(Path.home() / "Documents"),
        help="Directory of the documents (default=$home/Documents)")
@click.option('--cfgdir', '-c', default=str(Path.home() / "Documents" / "inf"),
        help="Directory of the configuration files (default=$home/Documents/inf)")
def add(name, section, index, docdir, cfgdir):
    """Creates a document and adds it to index"""
    _add(name, section, index, docdir, cfgdir)

@main.command()
def list():
    """Lists the documents"""
    _list()

@main.command()
@click.option('--docdir', '-d', default=str(Path.home() / "Documents"),
        help="Directory of the documents (default=$home/Documents)")
@click.option('--cfgdir', '-c', default=str(Path.home() / "Documents" / "inf"),
        help="Directory of the configuration files (default=$home/Documents/inf)")
@click.option('--nocompile',    default=False, is_flag=True,
        help="dont compile the documents")
@click.option('--nocleanup',    default=False, is_flag=True,
        help="dont cleanup after compiling")
@click.option('--proccount',    default=0,
        help="maximum documents to compile at once")
@click.option('--index', '-i' , default=False, is_flag=True,
        help="prints the index and exits")
def compile(nocompile, nocleanup, proccount, docdir, cfgdir, index):
    """Compiles docments using RMarkdown."""
    _compile(nocompile, nocleanup, proccount, docdir, cfgdir, index)

def start():
    main(obj={})


if __name__ == "__main__":
    start()
