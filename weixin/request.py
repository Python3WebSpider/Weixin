from weixin.config import *


class WeixinRequest():
    def __init__(self, request, callback, need_proxy=False, fail_time=0, timeout=TIMEOUT):
        self.request = request
        self.callback = callback
        self.need_proxy = need_proxy
        self.fail_time = fail_time
        self.timeout = timeout
