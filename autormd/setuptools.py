#!/usr/bin/python3
def setup(docdir, cfgdir):
    Docdir  = Path(docdir)
    Cfgdir  = Path(cfgdir)
    Srcdir  = Docdir / "src"
    Pdfdir  = Docdir / "pdf"
    Tmpdir  = Docdir / "tmp"
