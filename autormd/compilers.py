import subprocess
from pathlib import Path
from .functions import add_rmd, indexadd

class comper:
    def __init__(self, docdir, cfgdir):
        self.Docdir  = Path(docdir)
        self.Cfgdir  = Path(cfgdir)
        self.Srcdir  = self.Docdir / "src"
        self.Pdfdir  = self.Docdir / "pdf"
        self.Tmpdir  = self.Docdir / "tmp"
    def comp(self):
        pass
    def finish(self, compiles):
        if compiles:
            result = subprocess.Popen(['R', '-e', f"library('rmarkdown');render(\"{self.newfile}\")"],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result
        return None

class _ess(comper):
    def comp(self, file, section, sm, index):
        newfile=file.name.replace("ess", "rmd")
        filetitle = file.name.replace("The_", "")\
                .replace(f"{section}_", "")\
                .replace(f".ess", "")\
                .replace(f"_", " ")
        with open(f"{self.Tmpdir}/{newfile}", "w+") as tmpfile:
            with open(f"{self.Srcdir}/essay_master.rmd", "a") as em:
                em.write(f"\n\\includepdf[pages=-]({file})\n".replace("(","{").replace(")","}").replace(".ess", ".pdf").replace("/src/", "/pdf/"))
            with open(f"{self.Cfgdir}/essay_header", "r") as header:
                for line in header:
                    addline = line.replace("<Title>", filetitle)
                    tmpfile.write(addline)
            with open(file, "r") as srcfile:
                for line in srcfile:
                    lineadd = line
                    tmpfile.write(lineadd)
        self.newfile=newfile

class _doc(comper):
    def comp(self, file, section, sm, index):
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
        with open(f"{self.Tmpdir}/{newfile}", "w+") as tmpfile:
            with open(f"{self.Cfgdir}/doc_header", "r") as header:
                for line in header:
                    addline = line.replace("<Title>", subsecname)
                    tmpfile.write(addline)
                tmpfile.write("\n")
            with open(file, "r") as srcfile:
                for line in srcfile:
                    lineadd = line
                    tmpfile.write(lineadd)
        self.newfile=newfile
