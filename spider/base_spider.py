# coding:utf-8
from requests.utils import dict_from_cookiejar


class BaseSpider(object):
    """
    爬虫基类
    """
    def __init__(self):
        self.__username = None
        self.__password = None
        self._cookies = {}

    def login(self, username, password):
        """
        登录方法，需要重写
        :param username:
        :param password:
        :return:
        """
        pass

    def __get_check_code(self, *args, **kwargs):
        """
        获取验证码方法，可重写
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def handle_cookies(self, cookies):
        """
        处理cookies
        :param cookies:
        :return:
        """
        try:
            res = dict_from_cookiejar(cookies)
        except Exception as e:
            res = {}
        return res
