from .functions import *
from .setuptools import *
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

def _list():
    """Lists the documents"""

def _compile(nocompile, nocleanup, proccount, docdir, cfgdir, index):
    """Compiles docments using RMarkdown."""
    compiles = not nocompile
    cleanup = not nocleanup

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
    for section in sorted(sections):
        print(f"started compiling {section}")
        sm = open(f"{Srcdir}/{section}_master.rmd", "w+")
        sm.write(f"\\newpage\n\n# {section}")
        add_rmd(f"{section}_master.rmd", mm)
        for file in sorted(Path(Srcdir).glob(f"{section}_*")):
            if file != Path(f"{Srcdir}/{section}_master.rmd"):
                if "doc" == file.name.split(".")[-1]:
                    subsecname = file.name.replace("The", "")\
                            .replace(f"{section}_", "")\
                            .replace(f".doc", "")\
                            .replace(f"_", " ")
                    sm.write(f"\n## {subsecname}")
                    try:
                        for i in index[file.name]:
                            indexadd(sm, i)
                    except:
                        print(f"add {file.name} to index.csv")
                    add_rmd(file.name, sm)
                    newfile=file.name.replace("doc", "rmd")
                    with open(f"{Tmpdir}/{newfile}", "w+") as tmpfile:
                        with open(f"{Cfgdir}/doc_header", "r") as header:
                            for line in header:
                                addline = line.replace("<Title>", subsecname)
                                tmpfile.write(addline)
                        with open(file, "r") as srcfile:
                            for line in srcfile:
                                lineadd = line
                                tmpfile.write(lineadd)
                    p = comp(newfile, compiles)
                    if not p is None:
                        queue.append(p)
                    if proccount != 0:
                        if proccount <= len(queue):
                            queue[-1].communicate()
                            del queue[-1]
                elif "ess" == file.name.split(".")[-1]:
                    newfile=file.name.replace("ess", "rmd")
                    filetitle = file.name.replace("The", "")\
                            .replace(f"{section}_", "")\
                            .replace(f".doc", "")\
                            .replace(f"_", " ")
                    with open(f"{Tmpdir}/{newfile}", "w+") as tmpfile:
                        with open(f"{Srcdir}/essay_master.rmd", "a") as em:
                            em.write(f"\n\\includepdf[pages=-]({file})\n".replace("(","{").replace(")","}"))
                        with open(f"{Cfgdir}/essay_header", "r") as header:
                            for line in header:
                                addline = line.replace("<Title>", subsecname)
                                tmpfile.write(addline)
                        with open(file, "r") as srcfile:
                            for line in srcfile:
                                lineadd = line
                                tmpfile.write(lineadd)
                    p = comp(newfile, compiles)
                    if not p is None:
                        queue.append(p)
                    if proccount != 0:
                        if proccount <= len(queue):
                            queue[-1].communicate()
                            del queue[-1]
                else:
                    print(f"bad file type {file}")
        sm.close()
    for i in queue:
        i.communicate()
    mm.close()
    finish(compiles, cleanup, docdir)
