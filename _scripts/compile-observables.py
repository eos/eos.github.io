#!/usr/bin/python3
# vim: set sw=4 sts=4 et tw=120 :

from collections import OrderedDict
import eos
import sys
import yaml

''' Hacks to allow for ordered output to YAML '''
def represent_ordereddict(dumper, data):
    value = []

    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)

        value.append((node_key, node_value))

    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)
yaml.add_representer(OrderedDict, represent_ordereddict)

observables = eos.Observables()

all_data = []
for section in observables.sections():
    section_data = OrderedDict()
    section_data['title']  = section.name()
    section_data['groups'] = []
    for group in section:
        group_data = OrderedDict()
        group_data['title']   = group.name()
        group_data['desc']    = group.description()
        group_data['entries'] = []
        for qn, entry in group:
            latex = entry.latex()
            if 0 == len(latex):
                continue
            entry_data = OrderedDict()
            entry_data['qn']    = str(qn)
            entry_data['latex'] = latex
            group_data['entries'].append(entry_data)

        section_data['groups'].append(group_data)

    all_data.append(section_data)

print(yaml.dump(all_data))
