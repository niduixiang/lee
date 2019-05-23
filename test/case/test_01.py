#coding:utf-8
import unittest
import requests
from case.loginblog import Blog
from common.logger import Log
class Test(unittest.TestCase):
    log=Log()
    def setUp(self):
        self.blog=Blog()
    def test_login(self):
        email = "ceshi@ctgtmo.com"
        password = "42f2c22d3a955b210c10d16d43472b30"
        validateCode = "gayd"
        time = "1553047195562"
        self.log.info("------start------")
        result=self.blog.login(email,password,validateCode,time)
        # self.log.info(u"调用登录结果:%s","result")
        # self.log.info(u"获取是否登录成功:%s",result["type"])
        self.assertEqual(result["type"],"success")
        self.log.info("----end!----")