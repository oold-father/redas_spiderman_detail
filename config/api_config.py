#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 下午5:17
# @Author  : yinxin
# @File    : ApiConfig
# @Software: PyCharm

from happy_python import HappyConfigBase

class ApiConfig(HappyConfigBase):
    """
    配置文件模板
    """
    def __init__(self):
        super().__init__()

        self.section = "api_config"
        self.host = "127.0.0.1"
        self.port = 8080
        self.uri = ""