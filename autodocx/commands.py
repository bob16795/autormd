from autodocx.functions import clean, finish, check, close_word, purge
from autodocx.setuptools import *
from autodocx.compilers import _doc,_ess
from pathlib import Path

def _setup(docdir, cfgdir):
    """sets up the config files"""
    setup(docdir, cfgdir)

def _add(name, section, index, docdir, cfgdir):
    """Creates a document and adds it to index"""
    Docdir  = Path(docdir)
    Cfgdir  = Path(cfgdir)
    Srcdir  = Docdir / "src"

    filename = f"{section}_{name}.doc"
    open(f"{str(Srcdir)}/{filename}", 'w+').close()
    indexstr = ",".join(index)
    with open(str(Cfgdir / "index.csv"), 'a') as idx:
        idx.write(f"{filename},{indexstr}")
    found = False
    with open(str(Cfgdir / "sections"), "r") as sections:
        for line in sections:
            if line == f"{section}\n":
                found = True
    if not found:
        with open(str(Cfgdir / "sections"), "a") as sections:
            sections.write(f"{section}\n")

def _list(tolist, docdir, cfgdir):
    """Lists the documents or index"""


def _compile(compile, docdir, cfgdir):
    """Compiles docments using RMarkdown."""
    compiles = compile
    close_word()

    Docdir  = Path(docdir)
    Cfgdir  = Path(cfgdir)
    Srcdir  = Docdir / "src"
    Pdfdir  = Docdir / "pdf"
    Imgdir  = Docdir / "img"

    check(Docdir)
    check(Srcdir)
    check(Cfgdir)
    check(Pdfdir)
    purge(Srcdir, "*_master.rmd")
    purge(Imgdir, "*")

    with open(Cfgdir / "sections", "r") as file:
        sections = file.read()[:-1].split("\n")

    with open(Cfgdir / "index.csv", "r") as file:
        read = file.read()[:-1].split("\n")
        index = {}
        for i in read:
            data = i.split(",")
            index[data[0]] = data[1:]

    filedict = {
            "doc" : _doc,
            "ess" : _ess}
    for section in sorted(sections):
        print(f"compiling {section}")
        for file in sorted(Path(Srcdir).glob(f"{section}_*")):
            if file != Path(f"{Srcdir}/{section}_master.rmd"):
                type = file.name.split(".")[-1]
                if type in filedict:
                    p = filedict[type](docdir, cfgdir)
                    p.comp(file, section, index)
                    p.finish(compile)
                else:
                    print(f"bad file type {file}")
    finish(compiles, docdir, cfgdir)
