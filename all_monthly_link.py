import requests
from bs4 import BeautifulSoup

############### 获取 html 及转码 ############################

base_url = 'http://mysql.taobao.org'            # type(base_url) == <class 'str'>
response = requests.get(base_url + '/monthly')

# print(response.content.decode('utf-8'))

# 同上
print('response.encoding : ' + response.encoding)
print('response.apparent_encoding : ' + response.apparent_encoding)
response.encoding = response.apparent_encoding
print('after set encoding, response.encoding : ' + response.encoding)
# print(response.text)
##########################################################


soup = BeautifulSoup(response.text, 'html.parser')          # 'html.parser' 为python 内置的解析器，还有 'lxml'、'html5lib'等
# print(soup.body.div.contents[3].ul.find_all('a'))

# 所有 <a> tag
# resultSet 为所有 <a> tag 的集合，
# resultSet[i] 为 <a herf='...'>somthing</a>,
# resultSet[i].string 为标签里的内容 somthing
resultSet = soup.body.div.contents[3].ul.find_all('a')
print("type :", type(resultSet))     # 找出所有标题，标题格式： [数据库内核月报 － 2020/02]
# month_list 存放 http://mysql.taobao.org/monthly 下所有周报的链接
month_list = []
for i in resultSet:
    url = ''
    url = url.join(i.get('href').strip())
    url = base_url + url
    month_list.append(url);
print(month_list)



# 存放周报链接和周报标题的集合 {'链接':'标题', ...}
all_dict = {}
for i in month_list:
    ret = requests.get(i)
    ret.encoding = 'utf-8'
    soup2 = BeautifulSoup(ret.text, 'html.parser')
    lis = soup2.body.div.contents[3].ul.find_all('a')

    for i in lis:
        title = ''
        title = title.join(i.string.strip())

        url = ''
        url = url.join(i.get('href').strip())
        url = base_url + url
        all_dict[url] = title
print(all_dict)