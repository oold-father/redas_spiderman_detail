#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 下午3:48
# @Author  : yinxin<yinxin666ccyy@gmail.com>
# @Site    : 
# @File    : application
# @Software: PyCharm

from utils import Consumer,send_data,crawl_url
import time


# init consumer
consumer = Consumer.get_consumer()


def main():
    msg = consumer.get_msg()
    url = bytes.decode(msg.value)
    html = crawl_url(url)
    send_data(url, html)

if __name__ == '__main__':
    while True:
        main()
        time.sleep(5)
