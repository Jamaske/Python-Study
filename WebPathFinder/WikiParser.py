import requests
import re
import webbrowser
from lxml import html

browser = "C:/Users/Master/AppData/Local/Chromium/Application/chrome.exe"

def get_all_links(url):
    global webbrowser
    links = set()
    content = html.fromstring(requests.get(url).content).xpath("/html/body/div[3]/div[3]/div[5]/div[1]")[0]
    for sub in content:
        if sub.xpath(".//span[@id='Примечания']"):break
        for href in sub.xpath(".//a[@href!='']/@href"):
            if re.fullmatch("/wiki/.*", href) and re.fullmatch(".*[^.]...", href):
                links.add(href)
    
    for i in links:
        print(i)
    print(len(links))
    return links

    
    






math_URL = "https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0"
pic_URL = "https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:Caesar3.svg"
links = get_all_links(math_URL)
#for url in links: webbrowser.open_new("https://ru.wikipedia.org/"+url)