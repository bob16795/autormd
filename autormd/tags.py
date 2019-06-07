import os
def reptag(file, text):
    author="preston precourt"
    date=str(os.stat(file).st_mtime)
    #TODO:read essays.csv
    text = text.replace("<Author>", author)
    text = text.replace("<Date>", date)
    return text
