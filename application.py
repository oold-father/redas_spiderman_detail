#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 下午3:48
# @Author  : yinxin<yinxin666ccyy@gmail.com>
# @Site    : 
# @File    : application
# @Software: PyCharm

from kafka import KafkaConsumer
from utils import Consumer
from time import sleep




# def main():
#     consumer = KafkaConsumer('yinxin', bootstrap_servers=['192.168.0.6:9092'])
#     print("lianjiewanc1")
#     for msg in consumer:
#         for i in range(3):
#             print(i)
#             sleep(1)
#         print(msg)

def main():
    consumer = Consumer.get_consumer()
    if not consumer:
        for msg in consumer.consumer:
            for i in range(3):
                print(i)
                sleep(1)
            print(msg)



if __name__ == '__main__':
    main()