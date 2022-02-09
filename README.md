# Overview

This module provides SAX-like functionality for reading MarkDown syntax.
Uses reading of tokens separately. Therefore the text below will be confusing for it.

```
ThisText[Name](link)
```

Addiotionally support for embedding was added. It is translated into iframe.
```
$[Name](link)
```

There is also a special case of embedding YouTube. YT has to be specified before the brackets. A YouTube video name can be specified inside of the first brackets. The YouTube video id has to be specified later.
```
$YT[](id)
```

Notice: It is still under heavy development.

# API

## class PyMarkDownSax

### Reading a file

```
def parse(self, file_name):
```
Parses a file name.

```
def parse_string(self, data = None):
```
Parses string of data.

### Parse functions

```
def startElement(self, tag, attributes):
```
Indicates start of a block.

```
def endElement(self, tag):
```
Indicates end of a block.

```
def characters(self, token):
```
Indicates that characters were processed. Every word is called separately. Whitespaces are called separately.


## class PyPanDoc2Html

### Reading a file

```
def __init__(self):
```

The class goal is to translate MarkDown files to HTML.

```
def to_html(self, from_md_file_name, to_html_file_name):
```

```
def to_string(self, string):
```

# Limitations

The implementations uses regular expressions here and there, which might not necessarily be
the best way to process the text.

## PyMarkDownSax

Uses reading of tokens separately. Therefore the text below will be confusing for it.

```
ThisText[Name](link)
```

## PyMarkDownSax2Html

An image inside of link is supported, however it only uses link name from link and link name from image.

```
[ ![](img_link) ](a_link)
```
