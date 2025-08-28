---
layout: page
title: About
---

EOS is a software package that addresses several use cases in the field of
high-energy flavor physics:

 1. [theory predictions of and uncertainty estimation for flavor observables](https://eoshep.org/doc/user-guide/predictions.html)
   within the Standard Model or within the Weak Effective Theory;
 2. [Bayesian parameter inference](https://eoshep.org/doc/user-guide/inference.html)
    from both experimental and theoretical constraints; and
 3. [Monte Carlo simulation of pseudo events](https://eoshep.org/doc/user-guide/simulation.html) for flavor processes.

An up-to-date list of publications that use EOS can be found [here](https://eos.github.io/publications/).

EOS is written in C++17 and designed to be used through its Python 3 interface,
ideally within a Jupyter notebook environment.
It depends on as a small set of external software:

 - the GNU Scientific Library (libgsl),
 - a subset of the BOOST C++ libraries,
 - the Python 3 interpreter.

For details on these dependencies we refer to the [online documentation](https://eos.github.io/doc/installation.html#installing-the-dependencies-on-linux).

Installation
------------

EOS supports several methods of installation. For Linux users, the recommended method
is installation via PyPI:
```
pip3 install eoshep
```
Development versions tracking the master branch are also available via PyPi:
```
pip3 install --pre eoshep
```

For instructions on how to build and install EOS on your computer please have a
look at the [online documentation](https://eos.github.io/doc/installation.html).

Authors and Contributors
------------------------

If you use EOS in a scientific publication, please cite it using the following BibTeX entry:

    @article{vanDyk:2021sup,
      author        = "van Dyk, Danny and others",
      title         = "{EOS - A Software for Flavor Physics Phenomenology}",
      eprint        = "2111.15428",
      archivePrefix = "arXiv",
      primaryClass  = "hep-ph",
      reportNumber  = "EOS-2021-04, TUM-HEP 1371/21, P3H-21-094, SI-HEP-2021-32",
      month         = "11",
      year          = "2021"
    }


The main authors are:

 * Frederik Beaujean,
 * Christoph Bobeth,
 * Carolina Bolognani <carolinabolognani@gmail.com>,
 * Nico Gubernari <nicogubernari@gmail.com>,
 * Florian Herren <florian.s.herren@gmail.com>,
 * Matthew J. Kirk <matthew.j.kirk@durham.ac.uk>,
 * Meril Reboud <merilreboud@gmail.com>,
 * Danny van Dyk <danny.van.dyk@gmail.com>,

with further code contributions by:

 * Marzia Bordone,
 * Thomas Blake,
 * Lorenz Gaertner,
 * Elena Graverini,
 * Stephan Jahn,
 * Ahmet Kokulu,
 * Viktor Kuschke,
 * Stephan Kürten,
 * Philip Lüghausen,
 * Bastian Müller,
 * Filip Novak,
 * Stefanie Reichert,
 * Eduardo Romero,
 * Rafael Silva Coutinho,
 * Ismo Tojiala,
 * K. Keri Vos,
 * Christian Wacker.

We would like to extend our thanks to the following people whose input and
support were most helpful in either the development or the maintenance of EOS:

 * Gudrun Hiller
 * Gino Isidori
 * David Leverton
 * Thomas Mannel
 * Ciaran McCreesh
 * Hideki Miyake
 * Konstantinos Petridis
 * Nicola Serra
 * Alexander Shires

Contact
-------

For additional information, please contact any of the main authors. If you want to report an
error or file a request, please file an issue [here](https://github.com/eos/eos/issues).
