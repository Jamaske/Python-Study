import requests
import re
from time import sleep
import webbrowser
from lxml import html



requests_count = 0
def get_all_links(url:str)->str:
    """pars wiki page with given url and return all pages urls from it"""
    WikiDomain = "https://ru.wikipedia.org"
    global requests_count
    requests_count += 1
    links = set()
    content = html.fromstring(requests.get(WikiDomain + url).content).xpath("/html/body/div[3]/div[3]/div[5]/div[1]")[0]
    for sub in content:
        if sub.xpath(".//span[@id='Примечания']"):break
        for href in sub.xpath(".//a[@href!='']/@href"):
            if re.fullmatch("/wiki/.*", href) and re.fullmatch(".*[^.]...", href):
                links.add(href)
    return links



def Batch_tab_open(urls:list[str])->None:
    """open all given urls in browser"""
    WikiDomain = "https://ru.wikipedia.org"
    browser = "C:/Users/Master/AppData/Local/Chromium/Application/chrome.exe"
    for url in urls:
        webbrowser.open_new(WikiDomain + url)
        sleep(0.3)



if __name__ == "__main__":
    math_URL = "/wiki/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0"
    pic_URL = "/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:Caesar3.svg"
    links = get_all_links(math_URL)
    #for url in links: 