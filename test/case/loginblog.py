#coding:utf-8
import unittest
import json
import requests
from common.logger import Log
class Blog(unittest.TestCase):
    log = Log()
    def login(self,email,password,validateCode,time):
        url = "http://test.weifenghr.com/wf-login/api/user/login"
        header = {"email": "ceshi@ctgtmo.com",
                       "Content-Type": "application/json"}
        payload = {
            "email":email,
            "password":password,
            "validateCode":validateCode,
            "time":time
        }

        r = requests.post(url, json=payload, headers=header).json()
        # print(type(r))
        # return r
        # print(r)
        self.log.info("登录成功返回200")
        return r
    def test_login1(self):
        u'''系统登录测试'''
        email="ceshi@ctgtmo.com"
        password="42f2c22d3a955b210c10d16d43472b31"
        validateCode="gayd"
        time="1553047195562"
        result2=self.login(email,password,validateCode,time)
        self.assertEqual(result2['type'],'failed')
        print(result2)
if __name__ == "__main__":
    unittest.main()
