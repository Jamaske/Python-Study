import requests
import re
from time import sleep
import webbrowser
from lxml import html
import pickle





class get_links:
    WikiDomain = "https://ru.wikipedia.org"
    web_request_count = 0
    cach_hit_count = 0
    page_parse_cache = "page_cahce.db"


    def __init__(self):
        try:
            with open(get_links.page_parse_cache, "rb") as file:
                self.storage = pickle.load(file)
                print(f"page cach with: {len(self.storage)} entrys is successfully loaded")
                print(type(self.storage))
        except Exception:
            self.storage = {}
            print("Can't open page cahce")
    

    def __call__(self, url:str)->str:
        if url in self.storage:
            get_links.cach_hit_count += 1
            return self.storage[url]
        links = get_links.request_and_parsr(url)
        self.storage[url] = links
        return links
    
        
    def __del__(self):
        with open(get_links.page_parse_cache, "wb") as file:
            pickle.dump(self.storage, file)
    

    @staticmethod
    def request_and_parsr(url:str)->str:
        """pars wiki page with given url and return all pages urls from it"""
        response = requests.get(get_links.WikiDomain + url).content
        get_links.web_request_count += 1
        content = html.fromstring(response).xpath("/html/body/div[3]/div[3]/div[5]/div[1]")[0]
        links = set()
        for sub in content:
            if sub.xpath(".//span[@id='Примечания']"):break
            for href in sub.xpath(".//a[@href!='']/@href"):
                if re.fullmatch("/wiki/.*", href) and re.fullmatch(".*[^.]...", href):
                    links.add(href)
        return links
    

    @staticmethod
    def Batch_tab_open(urls:list[str])->None:
        """open all given urls in browser"""

        for url in urls:
            webbrowser.open_new(get_links.WikiDomain + url)
            sleep(0.5)







if __name__ == "__main__":
    math_URL = "/wiki/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0"
    pic_URL = "/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:Caesar3.svg"
    links = get_links.request_and_parsr(math_URL)
    for i in links: print(i)