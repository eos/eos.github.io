---
layout: post
title: EOS support on MacOS X
author: Danny van Dyk
---

Thanks to a gratuitous donation of an iMac computer by [Prof. Leo van
Hemmen](http://www.professoren.tum.de/en/van-hemmen-leo/), we can now actively
support building and using EOS on Mac OS X. We thank Professor van Hemmen very
much for his donation!

The test hardware in use is limited to Mac OS 10.11 (El Capitan). We would be
happy to receive reports about EOS builds on more recent Mac OS versions. The
installation on MacOS via the Homebrew package manager is documented in the
[manual](manual/manual.pdf).  The minimal commands necessary to build the most
recent development version are

~~~bash
brew tap eos/homebrew-eos
brew install --HEAD eos
~~~
