import os
import re
import subprocess
import sys
import time
from pathlib import Path

try:
        import win32con
        import win32gui
except:
        pass

from autodocx.doced import render_main


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
            except Exception as e:
                print(e)

def finish(linux, compiles, docdir, cfgdir):
    Docdir = Path(docdir)
    Srcdir = Docdir / "src"

    os.chdir(Srcdir)
    print("compiling main")
    if compiles:
        render_main(linux, docdir, cfgdir)

def move(dir, pattern, to):
    for f in Path(dir).glob(pattern):
        os.rename(str(f), str(f).replace(str(dir), str(to)))

def purge(dir, pattern):
    for p in Path(dir).glob(pattern):
        p.unlink()
        
def close_word(document=r'main.docx'):
    handle = win32gui.FindWindow(None, document+r' - Word')
    if handle != 0:
        win32gui.PostMessage(handle,win32con.WM_CLOSE,0,0)
        time.sleep(.2)
