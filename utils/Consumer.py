#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 下午5:32
# @Author  : yinxin
# @File    : Consumer
# @Software: PyCharm


from kafka import KafkaConsumer
from common import mq_config, hlog

class Consumer:
    last_obj = None

    def __init__(self):
        hlog.info("初始化消息队列连接")

        hlog.var('mq_host', mq_config.host)
        hlog.var('mq_port', mq_config.port)
        hlog.var('mq_group', mq_config.group)
        hlog.var('mq_topic', mq_config.topic)

        self.consumer = KafkaConsumer(mq_config.topic,
                                        group_id= mq_config.group,
                                        bootstrap_servers=[
                                            '{}:{}'.format(mq_config.host, mq_config.port)
                                        ])


    @staticmethod
    def get_consumer():
        if not Consumer.last_obj:
            try:
                Consumer.last_obj = Consumer()
            except BaseException as e:
                hlog.debug("消息队列初始化连接异常:\n")
                hlog.debug(e)
                Consumer.last_obj = None
            else:
                hlog.info("消息队列连接完成")
        return Consumer.last_obj

    def get_msg(self):
        if not Consumer.last_obj:
            hlog.debug("未初始化消息队列连接")
            return ""
        return ""



