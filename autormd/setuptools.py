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

    with open(f"{Cfgdir}/doc_header", "w+") as header:
        header.write("---\ntitle: <Title>\noutput:\n    pdf_document\nheader-includes:\n  - \\usepackage{multicol}\n  - \\usepackage{indentfirst}\n---")
    with open(f"{Cfgdir}/essay_header", "w+") as header:
        header.write("---\noutput:\n  pdf_document:\nheader-includes:\n  - \\usepackage[margin=1in]{geometry}\n  - \\usepackage{times}\n  - \\usepackage{setspace}\n  - \\doublespacing  - \\usepackage{fancyhdr}\n  - \\pagestyle{fancy}\n  - \\lhead{}\n  - \\chead{}\n  - \\rhead{<LastName> \\thepage}\n  - \\lfoot{}\n   - \\cfoot{}\n  - \\rfoot{}\n  - \\renewcommand{\\headrulewidth}{0pt}\n  - \\renewcommand{\\footrulewidth}{0pt}\n  - \\setlength\headsep{0.333in}\n---\n\n\\begin{flushleft}\n\n<Author> \\\\\n<Instructor>\\\\\n<Subject>\\\\\n<Date>\\\\\n\\end{flushleft}\n\n\\begin{center}\n<Title>\n\end{center}\n\n\\setlength{\\parindent}{0.5in}")
    with open(f"{Srcdir}/main.rmd", "w+") as main:
        main.write("---\nnumbersections: true\noutput:\n    pdf_document:\n      highlight: pygments\nheader-includes:\n  - \\usepackage{times}\n  - \\usepackage[margin=1in]{geometry}\n  - \\usepackage{tocloft}\n  - \\usepackage{times}\n  - \\usepackage{indentfirst}\n  - \\usepackage[numbers]{natbib}\n  - \\usepackage{tabularx}\n  - \\usepackage[dvipsnames]{xcolor}\n  - \\usepackage{graphicx}\n  - \\usepackage{booktabs}\n  - \\usepackage{mwe}\n  - \\usepackage{imakeidx}\n  - \\usepackage{scrlayer-scrpage}\n  - \\usepackage{hanging}\n  - \\usepackage{hyperref}\n  - \\usepackage{tabto}\n  - \\usepackage[final]{pdfpages}\n  - \\makeindex[columns=2]\n  - \\newcolumntype{Y}{>{\\centering\\arraybackslash}X}\n  - \\pagestyle{scrheadings}\n  - \\renewcommand{\\cftsecfont}{\\large\\noindent\\break\\rule{.4\\textwidth}{1pt}\\tabto*{0cm}}\n  - \\setlength{\\columnsep}{2cm}\n  - \\renewcommand{\\cftsubsubsecfont}{\\footnotesize}\n  - \\clearpairofpagestyles\n  - \\ohead{\\rightmark}\n  - \\cfoot[\\pagemark]{\\pagemark}\n  - \\setcounter{tocdepth}{3}\n  - \\setlength{\\columnseprule}{1pt}\nfontsize: 12pt\n---")
        main.write("\n\\begin{titlepage}\n  \\begin{center}\n  \\hfill\n  \\parbox{\\linewidth}{\n    \\centering\n    <School>\\par\n  }\n  \\hfill\n  \\par\n    \\vspace{.05\\textheight}\n    {\\LARGE\\scshape NOTES\\par}\n    \\vspace{.05\\textheight}\n    \\par\n    {\\itshape\\large Every doc on my computer \\par}\n    \\vspace{.05\\textheight}\n    By \\textsc{<Author>}\\par\n    \\vspace{.05\\textheight}\n    \\begin{tabularx}{\\textwidth}{Y}\n      \\toprule\n      {\\Huge\\bfseries Notes 2018--2019 \\par} \\\\\n      \\bottomrule\n    \\end{tabularx}\n    \\vspace{.05\\textheight}\n    {\\large \\par}\n    \\vfill\n    \\noindent\\begin{tabularx}{\\textwidth}{XXXX}\n      \\toprule\n      Name & Grade & School & Class \\\\\n      \\midrule\n      <Firstname> & 10 & <School> & <Subject>\\\\\n  \\bottomrule\n  \\end{tabularx}\n\\end{center}\n\\end{titlepage}\n\n\\begin{multicols}{2}\n\n\\tableofcontents\n\n\\end{multicols}\n\n```{r child='main_master.rmd'}\n```\n\n\\clearpage\n\\phantomsection\n\\addcontentsline{toc}{section}{Index}\n\\printindex\n\\clearpage\n\\phantomsection\n\\addcontentsline{toc}{section}{refrences}\n\\bibliographystyle{plain}\n\\bibliography{/home/john/Documents/cit/uni}")

