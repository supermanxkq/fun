
"""
# ======思路=======

1.读取配置的网站地址
2.根据关键字查找对应的资源  (正则表达式)
3.下载相应的资源


"""
import re
import ssl
import json
import binascii
import random
from urllib.parse import quote
from urllib import request
import time
from tkinter import *

ssl._create_default_https_context = ssl._create_unverified_context

headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}

with open('source_url.json', 'r') as f:
    config = json.load(f)

key_words = config['key_words']
seed_search_url = config['seed_search_url']


def get_html(site_url):
    req = request.Request(url=site_url, headers=headers)
    return request.urlopen(req).read()


total = 0
for key_word in key_words.split(','):
    with open(key_word + '.txt', 'a') as f:
        print('搜索...', key_word)
        for i in range(5):
            seed_search_url_decode = binascii.a2b_hex(seed_search_url).decode("utf8")
            html = get_html(seed_search_url_decode+'list/'+quote(key_word)+'/%d' % (i+1)).decode('utf-8')
            r = r'magnet:\?xt=urn:btih:\w+'
            re_mp4 = re.compile(r)
            mp4List = (re.findall(re_mp4, html))
            mp4List = list(set(mp4List))
            for url in mp4List:
                total += 1
                print('写入', url)
                f.write(url + '\n')
            time.sleep(random.uniform(1, 1.1))  # 为了保证服务器reset，多延迟一会儿，随机值防 ban
    print('写入', key_word, '的种子完毕！')
print('=========共写入'+str(total)+'个种子！======')

