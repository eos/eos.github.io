---
layout: page
title: About
---

EOS is a software framework for use in High Energy Physics, specifically Quark Flavor Physics.

## Attributions

If you use EOS for your own work, please remember to not only cite EOS, but also
all the theoretical works whose numerical implementations you use. If in doubt,
please contact one of the authors.

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
