from WikiParser import get_links
import PathFinder



Math = "/wiki/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0"
FormalScience = "/wiki/%D0%98%D0%B4%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F"
Glossary = "/wiki/%D0%9F%D1%80%D0%BE%D0%B5%D0%BA%D1%82:%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0/%D0%A1%D0%BF%D0%B8%D1%81%D0%BA%D0%B8/%D0%93%D0%BB%D0%BE%D1%81%D1%81%D0%B0%D1%80%D0%B8%D0%B9_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D0%B9_%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B8"
FormalSystem = "/wiki/%D0%A4%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0"
Philosofy = "/wiki/%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F"
Logic = "/wiki/%D0%9B%D0%BE%D0%B3%D0%B8%D0%BA%D0%B0"
Expirience = "/wiki/%D0%9E%D1%89%D1%83%D1%89%D0%B5%D0%BD%D0%B8%D0%B5"
AC_DC = "/wiki/AC/DC"

start = Math
target = Logic
links_cource = get_links()
try:
    tree, dist = PathFinder.BFS(start, target, links_cource)
    if dist!= None:
        path = PathFinder.TreeNodeToRootPath(tree, target)
        print(f"distance: {dist},  web requests made: {get_links.web_request_count},  cache hits: {get_links.cach_hit_count}")
        get_links.Batch_tab_open(path)
    else:
        print(f"can't find target. web requests made: {get_links.web_request_count},  cache hits: {get_links.cach_hit_count}")
except Exception:
    print("some error. IDK bro")
