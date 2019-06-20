[![Build Status](https://travis-ci.org/bob16795/autormd.svg?branch=master)](https://travis-ci.org/bob16795/autormd)

# installing

## Dependencys:

- Python 3.7
- R
- texlive-full / texlive-most
- pandoc

## install

Run the following commands

```
> sudo python3 setup.py install
> R -e 'install.packages("rmarkdown")'
> autormd setup
```

# Usage
## adding documents

Create _at least_ one document with:

```
> autormd add [document\_name] [document\_section]
```

- document\_name cannot contain spaces, underscores will be converted to spaces in the compiling process.
- document\_section is one word

## compiling documents

```
> autormd compile
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

Essay files are prefixed with the contents of (Cfgdir)/essay\_header.
The compiled pdf files are then imported to the end of the main Document before the index.

### .doc (Document file)

Document files are prefixed with the contents of (Cfgdir)/doc\_header.

# Markdown Refrences

[Github Markdown Guide](https://guides.github.com/features/mastering-markdown/)

# License

The project is licensed under the BSD license.
