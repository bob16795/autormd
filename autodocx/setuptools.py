#!/usr/bin/python3
from pathlib import Path
import os
def setup(docdir, cfgdir):
    Docdir  = Path(docdir)
    Cfgdir  = Path(cfgdir)
    Srcdir  = Docdir / "src"
    Pdfdir  = Docdir / "pdf"
    Tmpdir  = Docdir / "tmp"
    os.makedirs(Docdir, exist_ok=True)
    os.makedirs(Cfgdir, exist_ok=True)
    os.makedirs(Srcdir, exist_ok=True)
    os.makedirs(Pdfdir, exist_ok=True)
    os.makedirs(Tmpdir, exist_ok=True)