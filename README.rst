Extract archives without having to worry about different ``tar``
parameters, or whether you should use a subdirectory or not.

ext extracts files to your CWD if there's only one directory or file in
there, and to a subfolder if there's more.

Setup
~~~~~

::

    $ pip3 install ext-util

Usage
~~~~~

::

    $ ext [pathtoarchive]

Supports rars, zips and tarballs.
