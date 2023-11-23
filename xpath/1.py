# Задание 1: вывести на экран словарь, ключи которого - названия фильмов, значения - содержимое "runtime"
from lxml import etree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()


runtimes = {}
for movie in root.xpath('/Movies/Movie'):
    title = movie.find("Title").text
    if runtime := movie.attrib.get('runtime', False):
        runtimes[title] = runtime
    elif (runtime := movie.find(".*[@runtime]")) is None:
        runtimes[title] = None
    else:
        runtime = runtime.attrib['runtime']
        runtimes[title] = runtime


for i in runtimes.items(): print(i)