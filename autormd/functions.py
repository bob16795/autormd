import os,sys,re
import subprocess
import time
from pathlib import Path

def add_rmd(File,To):
    To.write(f"\n```[r child=\"{File}\"]\n```\n".replace("[","{").replace("]","}"))

def check(Dir):
    if not Dir.is_dir():
        print(f"no such path {Dir}")
        sys.exit(1)

def clean(Dir):
    if not Dir.is_dir():
        os.mkdir(Dir)
    else:
        for the_file in os.listdir(Dir):
            file_path = os.path.join(Dir, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)

def comp(file, compiles):
    if compiles:
        result = subprocess.Popen(['R', '-e', f"library(rmarkdown);render(\"{file}\")"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result
    return None

def finish(compiles, cleanup, docdir):
    Docdir = Path(docdir)
    Srcdir = Docdir / "src"
    Pdfdir = Docdir / "pdf"
    Tmpdir = Docdir / "tmp"

    os.chdir(Srcdir)
    f = open(Srcdir / "main_master.rmd", "a")
    add_rmd("essay_master.rmd", f)
    f.close
    print("compiling main")
    p = comp("main.rmd", compiles)
    if not p is None:
        p.communicate()
    if cleanup:
        purge(Srcdir, "*.log")
        purge(Srcdir, "*_master.rmd")
    move(Srcdir, "main.pdf", Pdfdir)
    move(Tmpdir, "*.pdf", Pdfdir)
    move(Tmpdir, "*.log", Pdfdir)
    if cleanup:
        purge(Tmpdir, "*")
        os.rmdir(Tmpdir)

def indexadd(File, idx):
    File.write(f"\n\\index[{idx}]\n".replace("[", "{").replace("]", "}"))

def move(dir, pattern, to):
    for f in Path(dir).glob(pattern):
        os.rename(str(f), str(f).replace(str(dir), str(to)))

def purge(dir, pattern):
    for p in Path(dir).glob(pattern):
        p.unlink()
