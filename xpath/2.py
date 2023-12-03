# Задание 2: трансформировать содержимое movies.xml в
# формат json

import json
from lxml import etree as ET
import json

tree = ET.parse('movies.xml')
root = tree.getroot()


def xml_to_dict(element):
    element_dict = {}
    if element.text:  # у тегов  вида <X/> поле text = None
        text = element.text.strip(' \n')  # у тегов без текста поле text = '  \n'
        if text:  # добавляем поле текста в словарь только если он не пустой
            element_dict['text'] = text
    if element.attrib: element_dict['attrib'] = dict(element.attrib)
    for child in element:
        child_dict = xml_to_dict(child)
        if child.tag not in element_dict:
            element_dict[child.tag] = child_dict
        elif type(element_dict[child.tag]) == dict:
            element_dict[child.tag] = [element_dict[child.tag], child_dict]
        else:
            element_dict[child.tag].append(child_dict)
    return element_dict



dict_data = xml_to_dict(root)



json_data = json.dumps(dict_data, indent= 4)
print(json_data)

json_file = open("movies.json", 'w')
json.dump(dict_data, json_file)