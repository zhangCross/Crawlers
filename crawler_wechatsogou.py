#!/usr/bin/python
#coding=utf-8

import os
import sys
import time
import json
import logging
import datetime
import requests
import traceback
import random
import urllib
from bs4 import BeautifulSoup
from logging.handlers import RotatingFileHandler
import wechatsogou

reload(sys)
sys.setdefaultencoding('utf8')

home = "./"
ws_api = None
log_format = '%(asctime)s [%(filename)s] [%(lineno)d] - %(levelname)s: %(message)s'

fetch_timeout = 100
INTERVAL = 5
SPECIAL_INTERVAL = 30
SR_INTERVAL = 10

proxies = {
        'http': 'http://172.1.1.1:8080'
}


def init_logger(name):
    file_name = name + '.log'
    mlog = logging.getLogger(name)
    mlog.setLevel(logging.DEBUG)
    rthandler = RotatingFileHandler(os.path.join(home, file_name), maxBytes=100*1024*1024, backupCount=5)
    formatter = logging.Formatter(log_format)
    rthandler.setFormatter(formatter)
    mlog.addHandler(rthandler)
    return mlog

mlog = init_logger('crawl')

def msleep(interval):
    mlog.info("sleep %d s" % interval)
    time.sleep(interval)
    
def ls_search_result(data, i):
    try:
        mlog.info("%s\t%d"% (data, i))
        search_res = ws_api.search_article(data, i)
        return search_res
    except:
        mlog.error("get search_res fail")
        mlog.error(traceback.format_exc())
        return []

def check_and_mkdir(fold):
    if not os.path.exists(fold):
        mlog.debug("create %s"%fold)
        os.mkdir(fold)
        return 0
    else:
        return 1

def init():
    global ws_api
    ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=5)

def page_sleep(i):
    msleep(INTERVAL)

def get_content(search_res, query):
    content = []
    for article in search_res:
        # print json.dumps(article, indent=4, ensure_ascii=False)
        title = article["article"]["title"]
        describe = article["article"]["abstract"]
        author = article["gzh"]["wechat_name"]
        item = "website\t%s\t%s\t%s\t%s\n" % (query, title, describe, author)
        content.append(item)
    return content

def load_products(fpath):
    products = []
    with open(fpath) as fp:
        for line in fp:
            products.append(line.strip())
    return products

def do_crawl():
    mlog.info("crawl")
    products = load_products("product_name.txt")
    des_f = open("result.txt", "w")
    for query in products:
        break_flag = False
        mlog.info(query)
        num = 0
        for i in range(8)[1:]:
            search_res = ls_search_result(query, i)
            # print search_res
            content = get_content(search_res, query)
            for item in content:
                des_f.write(item)
                des_f.flush()
                num += 1
                if num == 50:
                    break_flag = True
                    break
            if break_flag:
                break
            msleep(0.5)
        msleep(0.5)
    des_f.close()

def main():
    init()
    do_crawl()

if __name__ == '__main__':
    main()
