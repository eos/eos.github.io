---
layout: post
title: New release (btopipilnu-qcdf)
author: Danny van Dyk
---

I have tagged the
[btopipilnu-qcdf](https://github.com/eos/eos/releases/tag/btopipilnu-qcdf)
release of EOS, which was used to produce the numerical results in
<a href="publications#EOS-2016-04">EOS-2016-04</a>. Noteworthy on the physics
side are

* Adding one-to-two-body form factors, with the B &#8594; &pi; &pi;
  form factors being their first implementation.
* Adding the four-body decay B &#8594; &pi; &pi; &#8467; &nu; to the list
  of available decays, both for new observables (e.g. `B->pipilnu::BR`) and one
  new signal PDF (`B->pipilnu::d^3Gamma@QCDF`).

On the usability side, the new Python interface allows to produce publication-quality
plots. One such plot has been published in <a href="publications#EOS-2016-04">EOS-2016-04</a>,
and shows contours of the pionic forward-backward asymmetry in B &#8594; &pi; &pi; &#8467; &nu; decays.
<img src="images/EOS-2016-04-fig-afb.png"/>
The Python script that was used to produce this plot has been made available as an
<a href="https://github.com/eos/eos/tree/master/manual/examples/plot-btopipilnu-a-fb">example</a>.
