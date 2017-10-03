---
layout: post
title: New release (lambdab-polarised)
author: Danny van Dyk
---

While working on their publication <a href="publications#EOS-2017-02">EOS-2017-02</a>,
<a href="https://www2.warwick.ac.uk/fac/sci/physics/staff/research/tomblake/">Tom Blake</a>
and <a href="https://www2.warwick.ac.uk/fac/sci/physics/staff/academic/kreps/">Michal Kreps</a>
derived the full set of angular observables for the decay
<span>&Lambda;<sub>b</sub> &rarr; &Lambda; &#8467;<sup>+</sup> &#8467;<sup>-</sup></span> in the case
of a polarised &Lambda;<sub>b</sub> baryon. They find a total of 34 angular observables
compared to the 10 observables in the unpolarised case (compare the theory paper
<a href="publications#EOS-2014-01">EOS-2014-01</a> and the fit to LHCb data in
<a href="publications#EOS-2016-02">EOS-2016-02</a>). The additional 24 observables
can be classified as:

1. A set of 2 observables that are copies of 2 of the unpolarised ones, diluted by the
   overall polarisation.
2. A set of 22 observables that are sensitive to the same combinations of Wilson
   coefficients as the unpolarised ones, but with a different dependence on the
   hadronic matrix elements.

They modified the existing EOS code such that now all angular observables can be predicted.
Their modifications have already been pushed to the master branch, and a corresponding
<a href="https://github.com/eos/eos/releases/tag/lambdab-polarised">tag</a> has been pushed as well.
A big thank you to Tom and Michal from my side for their contributions to EOS!
