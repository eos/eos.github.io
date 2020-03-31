---
layout: post
title: Installing from the Python Package Index (PyPI)
author: Danny van Dyk
---

The current master branch has just been updated with changes that allow to automatically build and deploy
EOS to the [Python Package Index](https://pypi.org/project/eoshep/). Binaries (so-called 'wheels') corresponding to version 0.3.1+
have been uploaded there, supporting the ```manylinux2014_x86_64``` platform with CPython versions 3.6, 3.7 and 3.8.
If you are running Linux with one of these Python versions, feel free to give the pre-buit EOS a try:

```
pip3 install eoshep
```
The Python interface to EOS is documented [here](https://eos.github.io/doc). Binaries built against more recent
CPython versions will be made available once the Python Packaging Authority (PyPA) updates their docker image.

Many thanks to Martin Ritter for both technical and moral support in adding this feature!
