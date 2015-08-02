ext
===

[![PyPi](http://img.shields.io/pypi/v/ext-util.svg?style=flat)](https://pypi.python.org/pypi/ext-util)
[![License](http://img.shields.io/badge/license-MIT-red.svg)](https://github.com/KoffeinFlummi/ext/blob/master/LICENSE)

Extract archives without having to worry about different `tar` parameters, or whether you should use a subdirectory or not.

ext extracts files to your CWD if there's only one directory or file in there, and to a subfolder if there's more.


### Setup

```
$ pip3 install ext
```


### Usage

```
$ ext [pathtoarchive]
```

Supports rars, zips and tarballs.
