from autodocx.docedmain import *
from autodocx.docedtools import *


def make_sub(doc, file, section, header_cmd):
    title = ".".join(file.name.replace("The_", "")
                     .replace(f"{section}_", "")
                     .replace(f"_", " ").split(".")[:-1])
    tags = {
        "Lastname": "Precourt",
        "Author": "Preston Precourt",
        "Prof": "Olhson",
        "Class": "Ela 9",
        "Date": "5 April 2017"
    }
    header_cmd(doc, title, tags)
    with open(file, encoding='utf-8') as filew:
        file_cached = ""
        for i in filew:
            file_cached = f"{file_cached}{i}"
    file_cached = file_cached.split("\n")
    #p = None
    #mode = 0
    # for i in file_cached:
    #    if i == '':
    #        p = doc.add_paragraph()
    #    p, mode = parse_text(doc, mode, i, p, False, 0)
    tokens = tokenize(file_cached)
    parsed = parse(tokens, file)
    add_to_doc(doc, parsed, file, False)
