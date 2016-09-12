---
layout: page
title: About
---

EOS is a software framework for use in High Energy Physics, specifically Quark Flavor Physics.
Its use cases include

  - accurate and precise prediction of flavor observables,
  - parameter inference from both experimental and theoretical constraints using Baysian statistics,
  - production of Monte Carlo samples from signal PDF of flavor processes.

The above can be achieved through use of existing client programs. Beyond those, EOS features
both a C++ and a Python interface.

For information on installation, usage and the library interface, we refer to the
<a href="/manual/manual.pdf">manual</a>.

## Attributions

If you use EOS for your own work, please remember to not only cite EOS, but also
all the theoretical works whose numerical implementations you use. If in doubt,
please contact one of the authors. To cite eos, you can use this bibtex snippet

    @misc{EOS,
          author         = "van Dyk, Danny and others",
          title          = "{EOS --- A HEP program for Flavor Observables}",
          note           = "\url{https://eos.github.io}",
          year           = "2016",
    }

## Contributors

The following people are actively involved in the development of EOS:

<table>
    <tr>
        <th>Name</th>
        <th>eMail</th>
    </tr>
    {% for c in site.data.contributors %}
        {% if c.status == 'active' %}
        <tr>
            <td>{{ c.name }}</td>
            <td><a href="mailto:{{ c.mail | encode_email }}">link</a></td>
        </tr>
        {% endif %}
    {% endfor %}
</table>

The following people have formerly contributed to the EOS development:

<table>
    <tr>
        <th>Name</th>
    </tr>
    {% for c in site.data.contributors %}
        {% if c.status == 'retired' %}
        <tr>
            <td>{{ c.name }}</td>
        </tr>
        {% endif %}
    {% endfor %}
</table>
