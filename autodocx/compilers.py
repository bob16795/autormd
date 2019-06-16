import subprocess
import docx
from autodocx.formaters.ess import setup as _ess_format
from autodocx.formaters.ess import header as _ess_header
from autodocx.formaters.doc import setup as _doc_format
from autodocx.formaters.doc import header as _doc_header
from docx.shared import Pt
from pathlib import Path
from autodocx.doced import make_sub
from autodocx.functions import *

class compiler:
    def __init__(self, docdir, cfgdir):
        self.Docdir  = Path(docdir)
        self.Cfgdir  = Path(cfgdir)
        self.Srcdir  = self.Docdir / "src"
        self.Pdfdir  = self.Docdir / "pdf"
        self.Tmpdir  = self.Docdir / "tmp"
    def comp(self):
        pass
    def finish(self, compiles):
        if compiles and self.cc:
            make_sub(self.doc, self.file, self.section, self.header)
            self.doc.save(self.Pdfdir / self.newfile)

class _ess(compiler):
    def comp(self, file, section, index):
        self.cc = True
        self.newfile = file.name.replace("ess", "docx")
        close_word(self.newfile)
        self.doc = docx.Document()
        self.file = file
        self.section = section
        self.header = _ess_header
        _ess_format(self.doc)

class _doc(compiler):
    def comp(self, file, section, index):
        self.cc = True
        self.newfile = file.name.replace("doc", "docx")
        close_word(self.newfile)
        self.doc = docx.Document(self.Cfgdir / "sub.docx")
        self.file = file
        self.section = section
        self.header = _doc_header
        _doc_format(self.doc)
