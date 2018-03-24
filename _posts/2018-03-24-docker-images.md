---
layout: post
title: docker.io images with EOS's built-time dependencies pre-installed
author: Danny van Dyk
---

In order to speed up build time of our TravisCI test cases, docker images
with the EOS build-time dependencies pre-installed are available over at
the docker hub in
[eoshep/build-essentials](https://hub.docker.com/r/eoshep/build-essentials).
These are used as for CI testing as of [commit 21f61a28](https://github.com/eos/eos/commit/21f61a284baf39b8e7637b67e507d21b78b95970).
Even though it is a small annoyance that docker does not permit three-letter organization
names, hence the ```eoshep``` name.

You can pull these images as you would pull any docker image using either

```
docker pull eoshep/build-essential:xenial
```

or

```
docker pull eoshep/build-essential:bionic
```


The source files for building these images are kept [here](https://github.com/eos/docker.io/).
Please feel free to contribute your own docker files for whatever architecture you build
EOS on.
