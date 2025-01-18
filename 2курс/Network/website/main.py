#!/usr/bin/env python3
import cgi
params = cgi.FieldStorage()
ans = params.getvalue('ans')

print("Content-type: text/html\n")
if not params:
    page = open("query.html")
elif ans == 'null': 
    page = open("acceptable.html")    
else:
    page = open("nuked.html")
print(page.read())