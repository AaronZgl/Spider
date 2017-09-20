# beautifulsoup库的使用

标签（空格分隔）： python 爬虫

---

[Beautiful Soup 4.2.0 文档][1]

# 1.功能
网页解析器：从网页中提取有价值的数据

# 2.原理 
结构化解析：将HTML网页解析成DOM树（Document Object Model），以节点为单位进行查找。

# 3.安装
* pip install beautifulsoup4

# 4.方法

* find_all：寻找所有符合要求的元素
* find：寻找第一个符合要求的元素


# 5.使用
 `1.创建BeautifulSoup对象` 

```python
    # 导入BeautifulSoup包
    from bs4 import BeautifulSoup
        
    # 创建BeautifulSoup对象
    soup = BeautifulSoup(html, 'html.parser' from_encoding = 'utf-8')
```

`2.搜索节点（find_all, find）`

```python
    # 寻找div节点
    node = soup.find_all('div')
        
    # 寻找所有class属性为a的div节点
    node = soup.find_all('div', class='a')  
        
    # 寻找所有内容为p，class属性为a的div节点
    node = soup.find_all('div', class='a', string='p')
```
  
 `3.访问节点信息`

```python
     # 获得节点的标签名称
     name = node.name
     
     # 获得节点的href属性
     href = node['href']
     
     # 获得节点的文本内容
     text = node.get_text()
```

# 6.实例
 `代码`

```python
        # -*- coding: utf-8 -*-
        
        # 导入包
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
        soup = BeautifulSoup(html_doc, 'html.parser' from_encoding = 'utf-8')
        
        # 寻找所有a节点
        a1_nodes = soup.find_all('a')
        
        # 寻找id为‘link1’的a节点
        a2_nodes = soup.find_all('a', id='link1')
        
        # 寻找class为story，内容为‘...’的节点
        # class为python的保留字，所以这里下一个下斜杠使用class_
        p_nodes = soup.find_all('p', class_='story', string='...')
        
        # 打印信息
        for node in a1_nodes:
            print node['id']
        for node in a2_nodes:
            print node['href']
        for node in p_nodes:
            print node.get_text()
```
 

  [1]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html

