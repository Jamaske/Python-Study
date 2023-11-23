from lxml import etree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()
#print(f'{tree = }    {root = }   {root.tag = }') # имя корневого тега
print(ET.tostring(root, pretty_print=True)) # строковое представление корневого элемента содержит информацию об имени элемента и адресе в памяти

