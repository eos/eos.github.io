---
layout: post
title: Specifying options in constraint and observable names
author: Danny van Dyk
---
A new class `QualifiedName` was added to EOS, in order

* to centralize parsing of `Constraint` and `Observable` names, and
* to ensure that these names follow the correct syntax everywhere they are used.

Beside centralizing and reducing the code, in the process the syntax
of these qualified names was changed in a backward-incompatible way.
As of [commit 348db60](https://github.com/eos/eos/commit/348db60b932c008a0f8d2017d9d7e3c2b0de1a4e),
a qualified name's list of options is separated from the rest of the name
by a `;` character, e.g.: `B->pipilnu::BR;model=CKMScan`.
The rationale for this change is that it makes the parsing a lot easier, and also
allows for the usage of `,` characters in observable names. The latter is
quite handy in order to distinguish between observables of the same basic name
but varying dependence on kinematic variables. For example, we can now
distinguish between three- and two-differential branching ratios
&#8492;(B &#8594; &pi; &pi; &#8467; &nu;) through the names `B->pipilnu::BR(q2,k2,cos(theta_pi))`
and `B->pipilnu::BR(q2,k2)`; see [commit c897932](https://github.com/eos/eos/commit/c897932f3d0f9a2b33ae1f2fede17344cdf58f5c). Also, the manual
was updated and can be found in the usual [place](manual/manual.pdf).

A big thank you to Rafael Silva Coutinho for help and discussions.
