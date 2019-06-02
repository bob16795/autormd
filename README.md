# installing
## Dependencys:
[![Build Status](https://travis-ci.org/bob16795/autormd.svg?branch=master)](https://travis-ci.org/bob16795/autormd)
- R
- texlive-full / texlive-most
- pandoc

## install

Run the following commands

```console
$ sudo python3 setup.py install
$ R -e 'install.packages("rmarkdown")'
$ autormd setup
```

# Usage
## adding documents

Create _at least_ one document with:

```console
$ autormd add [document_name] [documentsection]
```
- document_name cannot contain spaces, underscores will be converted to spaces in the compiling process.
- documentsection is one word

##
```console
$ autormd compile
```

# Features

+ The documents are Created in markdown.
+ Master document containing all other Documents
+ Fully featured index.

# Misc.

## Index

to add items to the index

## Filetypes

### .ess (Essay file)

Essay files are prefixed with the contents of ~/doc/inf/essay_header.
The compiled pdf files are then imported to the end of the main Document before the index.

### .doc (Document file)

Document files are prefixed with the contents of ~/doc/inf/doc_header.

# Markdown Refrences

[Github Markdown Guide](https://guides.github.com/features/mastering-markdown/)

# License

The project is licensed under the BSD license.
