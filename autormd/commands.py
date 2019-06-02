from .functions import *
from .setuptools import *
from .compilers import _doc,_ess
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


def _compile(compile, cleanup, proccount, docdir, cfgdir, verbose):
    """Compiles docments using RMarkdown."""
    compiles = compile
    cleanup = cleanup

    Docdir  = Path(docdir)
    Cfgdir  = Path(cfgdir)
    Srcdir  = Docdir / "src"
    Pdfdir  = Docdir / "pdf"
    Tmpdir  = Docdir / "tmp"

    check(Docdir)
    check(Srcdir)
    check(Cfgdir)
    check(Pdfdir)
    clean(Tmpdir)
    purge(Srcdir, "*_master.rmd")

    with open(f"{Srcdir}/essay_master.rmd", "w") as em:
        em.write("\\phantomsection\n\\addcontentsline{toc}{section}{Esseys}")
    mm = open(Srcdir / "main_master.rmd", "w+")

    with open(Cfgdir / "sections", "r") as file:
        sections = file.read()[:-1].split("\n")

    with open(Cfgdir / "index.csv", "r") as file:
        read = file.read()[:-1].split("\n")
        index = {}
        for i in read:
            data = i.split(",")
            index[data[0]] = data[1:]

    os.chdir(Tmpdir)
    queue = []
    filedict = {
            "doc" : _doc,
            "ess" : _ess}
    for section in sorted(sections):
        print(f"started compiling {section}")
        sm = open(f"{Srcdir}/{section}_master.rmd", "w+")
        sm.write(f"\\newpage\n\n# {section}")
        add_rmd(f"{section}_master.rmd", mm)
        for file in sorted(Path(Srcdir).glob(f"{section}_*")):
            if file != Path(f"{Srcdir}/{section}_master.rmd"):
                type = file.name.split(".")[-1]
                if type in filedict:
                    p = filedict[type](docdir, cfgdir)
                    p.comp(file, section, sm, index)
                    p = p.finish(compile)
                else:
                    print(f"bad file type {file}")
                if not p is None:
                    queue.append(p)
                if proccount > 0:
                    if proccount <= len(queue):
                        out = queue[-1].communicate()
                        if verbose:
                            print(out)
                        del queue[-1]
        sm.close()
    for i in queue:
        i.communicate()
    mm.close()
    finish(compiles, cleanup, docdir)
