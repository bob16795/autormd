#!/usr/bin/python3
from pathlib import Path
import os, sys

def copy_config_files(cfgdir, which):
    import shutil
    from errno import EEXIST

    def copy(cfgdir, src, dest):
        if os.path.exists(Path(cfgdir) / dest):
            sys.stderr.write("already exists: %s\n" % (Path(cfgdir) / dest))
        else:
            sys.stderr.write("creating: %s\n" % (Path(cfgdir) / dest))
            try:
                os.makedirs(cfgdir)
            except OSError as err:
                if err.errno != EEXIST:  # EEXIST means it already exists
                    print("This configuration directory could not be created:")
                    print(cfgdir)
                    print("To run ranger without the need for configuration")
                    print("files, use the --clean option.")
                    raise SystemExit
            try:
                shutil.copy(relpath(cfgdir, src), cfgdir)
            except OSError as ex:
                sys.stderr.write("  ERROR: %s\n" % str(ex))
    if which == 'maintemp' or which == 'all':
        copy(cfgdir, 'data/main.docx', 'main.docx')
    elif which == 'subtemp' or which == 'all':
        copy(cfgdir, 'data/sub.docx', 'sub.docx')
    elif which == 'indexcsv' or which == 'all':
        copy(cfgdir, 'data/empty', 'index.csv')
    elif which == 'essayscsv' or which == 'all':
        copy(cfgdir, 'data/empty', 'essays.csv')
    else:
        sys.stderr.write("Unknown config file `%s'\n" % which)

def relpath(cfgdir, *paths):
    """returns the path relative to the autodocx library directory"""
    return os.path.join(os.path.dirname(__file__), *paths)

def setup(docdir, cfgdir):
    Docdir = Path(docdir)
    Cfgdir = Path(cfgdir)
    Srcdir = Docdir / "src"
    Pdfdir = Docdir / "pdf"
    Tmpdir = Docdir / "tmp"
    os.makedirs(Docdir, exist_ok=True)
    os.makedirs(Cfgdir, exist_ok=True)
    os.makedirs(Srcdir, exist_ok=True)
    os.makedirs(Pdfdir, exist_ok=True)
    os.makedirs(Tmpdir, exist_ok=True)
    copy_config_files(cfgdir, "all")
