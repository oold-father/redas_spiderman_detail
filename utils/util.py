#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 下午12:50
# @Author  : yinxin
# @File    : util
# @Software: PyCharm

import inspect
import base64
from common import api_config
from common import hlog
from common import PLATFORM_MAP
import requests
import uuid
import re
import os
import json


def send_data(source_url, htmlString):
    if "" == htmlString:
        return
    spider_uuid = uuid.uuid1()

    encodedBytes = base64.b64encode(htmlString.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")

    data = {
        "url": source_url,
        "spiderUuid": str(spider_uuid),
        "platform": PLATFORM_MAP[get_platfrom(source_url)],
        "htmlString": encodedStr
    }

    headers = {
        "content-type": "application/json"
    }

    url = "http://%s:%s%s"%(
        api_config.host,
        api_config.port,
        api_config.uri
    )
    requests.post(url=url, data= json.dumps(data), headers= headers)

def crawl_url(url):

    output = os.popen("node spider.js %s" % url).read()
    jsonString = json.loads(output)
    html = ""
    if "success" == jsonString["code"]:
        html = jsonString["data"]
    else:
        hlog.debug("爬虫爬取有误")
        crawl_url(url)

    return html

def get_platfrom(url):
    """
    根据url获取网站域名主体
    :param url: 网址
    :return:
    """
    func_name = inspect.stack()[0][3]
    hlog.enter_func(func_name)
    hlog.var("url", url)
    try:
        domain = url.split("/")[2]
        platfrom = domain.split(".")[1]
        hlog.var("platfrom", platfrom)
    except:
        hlog.debug("获取网站域名主体失败")

    hlog.info("获取网站域名主体成功")
    hlog.exit_func(func_name)
    return platfrom