from lxml import etree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()
#print(f'{tree = }    {root = }   {root.tag = }') # имя корневого тега
#print(ET.tostring(root, pretty_print=True)) # строковое представление корневого элемента содержит информацию об имени элемента и адресе в памяти

for char in root.attrib: print(char)

'''
print("писок всех тегов с именем movie")
for i in root.findall('Movie'): print(i)

entries_movie = tree.xpath("/Movies/Movie")
print("список всех тегов с путём /Movies/Movie")
for i in entries_movie: print(i)

entries_movie = tree.xpath("//Movie")
print("список всех тегов с именем movie?")
for i in entries_movie: print(i)

entries_title = tree.xpath("//Title")
print("все теги с названием titile")
for i in entries_title: print(i)

print("содержимое первого в тексте тега с названием Title")
print(entries_title[0].text)

print("название первого в тексте тега с названием Title, как то тупо")
print(entries_title[0].tag)

print("аттрибуты второго тега Title, и только значения аттрибутов")
print(entries_title[1].attrib)
print(entries_title[1].values())

entries_title_runtime = tree.xpath("//Title[@runtime]/text()")
print("содержимое тегов с названием Title имеющих аттрибут runtime\nзамечание содержимое и аттрибуты тега, тоже имеют свой путь")
print(entries_title_runtime)

entries_title_runtime = tree.xpath("//Title[@runtime='142']/text()")
print("тоже самое, но только те, где runtime = 142 ")
print(entries_title_runtime)

print('итерирумся по всем фильмам и рекурсивно получаем всё содежащиеся теги')
for elem in entries_movie:
    all_descendants = list(elem.iter())
    elem.iter()
    print(all_descendants)




'''


# Документация для стандартного модуля json: https://docs.python.org/3/library/json.html
# Неофициальный перевод с примерами записи в json https://python-scripts.com/json?ysclid=lac4k0btwt466481369