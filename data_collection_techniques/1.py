from bs4 import BeautifulSoup

html = "<html><body><h1>Hello</h1></body></html>"
soup = BeautifulSoup(html, "html.parser")

print(soup.h1.text)

import bs4
print(bs4.__version__)