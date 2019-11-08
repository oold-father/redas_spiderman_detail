from happy_python import HappyConfigBase

class MqConfig(HappyConfigBase):
    """
    配置文件模板
    """
    def __init__(self):
        super().__init__()

        self.section = 'mq_config'
        self.host = "127.0.0.1"
        self.port = 9092
        self.group = ""
        self.topic = ""