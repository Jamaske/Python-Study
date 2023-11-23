# Задание 2: трансформировать содержимое movies.xml в формат json

import json
from lxml import etree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()

def xml_to_dict(element):
    element_dict = {}
    #if element.text: element_dict['text'] = element.text
    if element.attrib: element_dict['attrib'] = element.attrib
    for child in element:
        child_dict = xml_to_dict(child)
        if child.tag not in element_dict:
            element_dict[child.tag] = child_dict
        elif type(element_dict[child.tag]) == dict:
            element_dict[child.tag] = [element_dict[child.tag], child_dict]
        else:
            element_dict[child.tag].append(child_dict)
    return element_dict

print(xml_to_dict(root))