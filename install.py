# 爬取网站中PDF资源

import urllib.request
import re
import os


# open the url and read
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    page.close()
    return html


# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    reg = r'(\d\d\.pdf)'  # 正则匹配
    url_re = re.compile(reg)
    url_lst = url_re.findall(html.decode('UTF-8', 'ignore'))  # 匹配的数组
    return (list(set(url_lst)))  # 把重复项去掉


def getFile(url):
    file_name = url.split('/')[-1]
    try:
        u = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        # 碰到了匹配但不存在的文件时，提示并返回
        print(url, "url file not found")
        return
    block_sz = 8192
    with open(file_name, 'wb') as f:
        while True:
            buffer = u.read(block_sz)
            if buffer:
                f.write(buffer)
            else:
                break

    print("Sucessful to download" + " " + file_name)


root_url = 'https://pages.cs.wisc.edu/~remzi/OSTEP/Chinese/'  # 下载地址中相同的部分
raw_url = 'https://pages.cs.wisc.edu/~remzi/OSTEP/Chinese/'  # 检索匹配名字的源网址

html = getHtml(raw_url)
url_lst = getUrl(html)
print("url_lst", url_lst)

if not os.path.exists('pdf_download'):
    # 文件夹不存在时，再进行创建
    os.mkdir('pdf_download')
os.chdir(os.path.join(os.getcwd(), 'pdf_download'))

for url in url_lst[:]:
    url = root_url + url  # 形成完整的下载地址
    getFile(url)
