---
layout: page
title: About
---

EOS is a software package that addresses several use cases in the field of
high-energy flavor physics:

 1. [theory predictions of and uncertainty estimation for flavor observables](https://eos.github.io/doc/use-cases.html#theory-predictions-and-their-uncertainties)
   within the Standard Model or within the Weak Effective Theory;
 2. [Bayesian parameter inference](https://eos.github.io/doc/use-cases.html#parameter-inference)
    from both experimental and theoretical constraints; and
 3. [Monte Carlo simulation of pseudo events](https://eos.github.io/doc/use-cases.html#pseudo-event-simulation) for flavor processes.

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

    @manual{EOS,
        title     = "{\texttt{EOS} v1.0 --- A software for flavor physics phenomenology}",
        DOI       = {10.5281/zenodo.5730384},
        journal   = {Zenodo},
        author    = "Danny van Dyk and
                     Frederik Beaujean and
                     Thomas Blake and
                     Christoph Bobeth and
                     Marzia Bordone and
                     Eike Eberhard and
                     Elena Graverini and
                     Nico Gubernari and
                     Ahmet Kokulu and
                     Stephan Kürten and
                     Domagoj Leljak and
                     Philip Lüghausen and
                     Méril Reboud and
                     Martin Ritter and
                     Eduardo Romero and
                     Ismo Toijala and
                     K.~Keri Vos
                    ",
        year      = "2021",
        month     = "Nov"
    }


The main authors are:

 * Danny van Dyk <danny.van.dyk@gmail.com>,
 * Frederik Beaujean,
 * Christoph Bobeth <christoph.bobeth@gmail.com>,
 * Nico Gubernari <nicogubernari@gmail.com>,
 * Meril Reboud <reboud@gmail.com>,

with further code contributions by:

 * Marzia Bordone,
 * Thomas Blake,
 * Elena Graverini,
 * Stephan Jahn,
 * Ahmet Kokulu,
 * Stephan Kürten,
 * Philip Lüghausen,
 * Bastian Müller,
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