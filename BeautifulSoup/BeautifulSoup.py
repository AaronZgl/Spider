# -*- coding: utf-8 -*-

# 导入BeautifulSoup包
from bs4 import BeautifulSoup

# html文档，来自官网文档
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 创建soup对象
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

# 寻找所有a节点
a1_nodes = soup.find_all('a', )

# 寻找id为‘link1’的a节点
a2_node = soup.find('a', id='link1')

# 寻找class为sister，内容为‘...’的节点
a3_node = soup.find('a', class_='sister', string='Tillie')

# 打印信息
for node in a1_nodes:
    print node['id']

print a2_node.get_text()

print a3_node['href']
