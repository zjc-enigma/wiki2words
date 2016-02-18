#coding:utf8
from bs4 import BeautifulSoup
import re
import sys

disease_name = str(sys.argv[1])
html_file = "../data/" + disease_name + ".html"
html = open(html_file).read()

soup = BeautifulSoup(html)

mw_content = soup.find('div', id='mw-content-text')

all_a_list = mw_content.findAll('a')

res_list = []

for a_item in all_a_list:
    a_text = a_item.get_text()
    if a_text == "":
        continue
    if re.match(ur'^\d', a_text):
        continue
    if re.search(ur'[\u2E80-\u9FFF]{2,3}', a_text):
        res_list.append(a_text)

res_list = list(set(res_list))
res = "\n".join(res_list)
print res.encode('utf8')
