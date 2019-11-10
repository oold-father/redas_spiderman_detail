#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 下午5:02
# @Author  : yinxin
# @File    : common
# @Software: PyCharm

from pathlib import PurePath
from happy_python import HappyConfigParser
from happy_python import HappyLog
from config import ApiConfig, MqConfig

# 配置文件位置
CONFIG_DIR = PurePath(__file__).parent / 'configs'
CONFIG_FILENAME = str(CONFIG_DIR / 'common.ini')
LOG_CONFIG_FILENAME = str(CONFIG_DIR / 'log.ini')

# 加载api配置
api_config = ApiConfig()
HappyConfigParser.load(CONFIG_FILENAME, api_config)

# 加载mq配置
mq_config = MqConfig()
HappyConfigParser.load(CONFIG_FILENAME, mq_config)

# 加载log配置
hlog = HappyLog.get_instance(LOG_CONFIG_FILENAME)

