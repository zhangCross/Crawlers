#!/usr/bin/python
#coding=utf-8

import os
import re
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

reload(sys)
sys.setdefaultencoding('utf8')

home = "./"
MAX_PAGE = 120
log_format = '%(asctime)s [%(filename)s] [%(lineno)d] - %(levelname)s: %(message)s'

fetch_timeout = 100
INTERVAL = 5
SPECIAL_INTERVAL = 30
SR_INTERVAL = 10

url_reg_str = "(https?://)?[A-Za-z][-A-Za-z0-9+&@#/%?=~_|!:\.]+(com|net|cn|org|us)"
url_reg = re.compile(url_reg_str)
url_pre = "https://www.website.com/website?wd="
url_suf = "&tn=monline_dg&ie=utf-8"
agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
cookies = {
    'JSESSIONID':'aaaWxfWRfgAmLa5PSJxhw',
    'ABTEST':'0|1521010447|v1',
    'PHPSESSID':'7tfr07dcon4nmd6ac933lootu6',
    'IPLOC':'CN1100',
    'LCLKINT':'148456',
    'LSTMV''233%2C73'
    'SUIR':'92655AFF9095F7C847FA238C911D61BE',
    'SNUID':'43B58A2E4144261C2CB06296429900C3',
    'weixinIndexVisited': '1',
    'sct':'10',
    'pgv_si':'s4089101312',
    'pgv_pvi':'2003661824',
    'ld':'fkllllllll2z$y3ZlllllV$IlrllllllbDs1lkllll9lllllRklll5@@@@@@@@@@'
}

headers = {
    'User-Agent': agent,
    'Connection': 'keep-alive',
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
}


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

mlog = init_logger('crawl_website')

def msleep(interval):
    mlog.info("sleep %d s" % interval)
    time.sleep(interval)
    
def ls_search_result(data):
    try:
        url = url_pre + urllib.quote(data) + url_suf
        mlog.info(url)
        # r = requests.get(url, cookies=cookies, headers=headers, timeout=fetch_timeout)
        r = requests.get(url, headers=headers, verify=False, timeout=fetch_timeout)
        search_res = r.text
        return search_res
    except:
        mlog.error("get search_res fail")
        mlog.error(traceback.format_exc())
        return ""

def page_sleep(i):
    msleep(INTERVAL)

def get_content(search_res, query):
    content = []
    soup = BeautifulSoup(search_res, "lxml")
    left = soup.find("div", id="content_left")
    if not left:
        return content
    for id_pre in ["400", "300"]:
        for i in range(8)[1:]:
            id_str = "%s%d" % (id_pre, i)
            mdiv = left.find("div", id=id_str)
            if not mdiv:
                break
            title = mdiv.contents[0].text.replace("\n", "")
            body = mdiv.contents[1].text.replace("\n", "")
            match = url_reg.search(body)
            author = ""
            if match:
                author = match.group()
                body = body[0: match.start()]
            item = "website\t%s\t%s\t%s\t%s\n" % (query, title, body, author)
            content.append(item)
    return content

def load_products(fpath):
    products = []
    with open(fpath) as fp:
        for line in fp:
            products.append(line.strip())
    return products

def do_crawl_srlist():
    mlog.info("do crawl srlist")
    products = load_products("product_name.txt")
    des_f = open("result.txt", "w")
    for query in products:
        mlog.info(query)
        search_res = ls_search_result(query)
        # print search_res
        content = get_content(search_res, query)
        for item in content:
            des_f.write(item)
            des_f.flush()
        msleep(int(random.random() * 5))
    des_f.close()

def main():
    do_crawl_srlist()

if __name__ == '__main__':
    main()
