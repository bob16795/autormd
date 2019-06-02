import click
import os,sys,re
import subprocess
import time
from .test import _test
from .commands import _compile, _list, _add, _setup
from pathlib import Path


@click.group()
def main():
    """Document Manager"""

@main.command()
def test(tolist, docdir, cfgdir):
    """sets up the config files"""
    _test(tolist, docdir, cfgdir)

@main.command()
@click.argument('tolist', type=click.Choice(['docs', 'index']))
@click.option('--docdir', '-d', default=str(Path.home() / "Documents"), show_default=True,
        help="Directory of the documents (default=$home/Documents)")
@click.option('--cfgdir', '-c', default=str(Path.home() / "Documents" / "inf"),
        help="Directory of the configuration files")
def list(tolist, docdir, cfgdir):
    """sets up the config files"""
    _list(tolist, docdir, cfgdir)

@main.command()
@click.option('--docdir', '-d', default=str(Path.home() / "Documents"), show_default=True,
        help="Directory of the documents (default=$home/Documents)")
@click.option('--cfgdir', '-c', default=str(Path.home() / "Documents" / "inf"), show_default=True,
        help="Directory of the configuration files")
def setup(docdir, cfgdir):
    """sets up the config files"""
    _setup(docdir, cfgdir)

@main.command()
@click.option('--docdir', '-d', default=str(Path.home() / "Documents"), show_default=True,
        help="Directory of the documents")
@click.option('--cfgdir', '-c', default=str(Path.home() / "Documents" / "inf"), show_default=True,
        help="Directory of the configuration files")
@click.argument('name')
@click.argument('section')
@click.argument('index', nargs=-1)
@click.option('--docdir', '-d', default=str(Path.home() / "Documents"), show_default=True,
        help="Directory of the documents")
@click.option('--cfgdir', '-c', default=str(Path.home() / "Documents" / "inf"), show_default=True,
        help="Directory of the configuration files")
def add(name, section, index, docdir, cfgdir):
    """Creates a document and adds it to index"""
    _add(name, section, index, docdir, cfgdir)

@main.command()
@click.option('--docdir', '-d', default=str(Path.home() / "Documents"), show_default=True,
        help="Directory of the documents")
@click.option('--cfgdir', '-c', default=str(Path.home() / "Documents" / "inf"), show_default=True,
        help="Directory of the configuration files")
@click.option('--compile/--nocompile',    default=True, is_flag=True,
        help="dont compile the documents")
@click.option('--cleanup/--nocleanup',    default=True, is_flag=True,
        help="dont cleanup after compiling")
@click.option('--proccount',    default=0, show_default=True,
        help="maximum documents to compile at once")
@click.option('--verbose', '-v' , default=False, is_flag=True,
        help="print unneeded information")
def compile(compile, cleanup, proccount, docdir, cfgdir, verbose):
    """Compiles docments using RMarkdown."""
    _compile(compile, cleanup, proccount, docdir, cfgdir, verbose)

def start():
    main(obj={})


if __name__ == "__main__":
    start()
