#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 下午5:13
# @Author  : yinxin
# @File    : __init__.py
# @Software: PyCharm


from config.api_config import ApiConfig
from config.mq_config import MqConfig

__all__ = [
    "ApiConfig",
    "MqConfig"
]