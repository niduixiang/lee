#coding:utf-8
import unittest
import json
from base.demo import RunMain
from mock import mock
import yaml
# from common.re_token import get_token
yaml.warnings({'YAMLLoadWarning': False})


class TestMethod(unittest.TestCase):

    def setUp(self):
        url="http://test.weifenghr.com/wf-login/api/user/login"
        header= {"email": "yunpeng.zhang@ctgtmo.com",
                  "Content-Type": "application/json"}
        data = "{\"email\":\"yunpeng.zhang@ctgtmo.com\",\"password\":\"42f2c22d3a955b210c10d16d43472b30\",\"validateCode\":\"4567\",\"time\":1553852672532}"
        self.run = RunMain(url,header,data)
    def tearDown(self):
        print('yes')
    def test_01(self):

        url="http://test.weifenghr.com/wf-login/api/user/login"
        header = {"email": "yunpeng.zhang@ctgtmo.com",
                  "Content-Type": "application/json"}
        data=json.dumps({"email":"yunpeng.zhang@ctgtmo.com","password":"42f2c22d3a955b210c10d16d43472b30","validateCode":"dddd","time":1555660278811})
        # print(type(data))
        r=self.run.run_main(url,header,'Post',data)
        print(r)
        print(r['result']['token'])





    # def test_02(self):
    #     url='http://test.weifenghr.com/qthl-wf-busi/api/insurApplyManager/insurApplyInfo/list'
    #     header={"email": "yunpeng.zhang@ctgtmo.com",
    #               "Content-Type": "application/json"}
    #     data=json.dumps({"keyWord":"","companyId":None,"contractId":None,"projectId":None,"insuranceType":None,"type":None,"inProvince":None,"inCity":None,"packageId":None,"applyMonthBegin":None,"applyMonthEnd":None,"beginMonthBegin":None,"beginMonthEnd":None,"isCall":None,"isAttach":None,"saleId":None,"befId":None,"backId":None,"sumDateBegin":None,"sumDateEnd":None,"endDateBegin":None,"endDateEnd":None,"feedback":None,"overCheck":None,"status":None,"checkStatus":None,"source":None,"isAccept":None,"payStatus":None,"pageNum":1,"pageSize":10,"orderBy":""})
    #     mock_data=mock.Mock(return_value=data)
    #     r=self.run.run_main(url, header, 'Post', data)
    #     print(r)

    def test_03(self):
        url = "http://test.weifenghr.com/qthl-wf-busi/api/insurApplyManager/insurApplyInfo/list"
        header = {"email": "ceshi@ctgtmo.com",
                  "Content-Type": "application/json"}

        data = "{\"email\":\"ceshi@ctgtmo.com\",\"password\":\"42f2c22d3a955b210c10d16d43472b30\",\"validateCode\":\"4567\",\"time\":1553852672532}"
        mock_data=mock.Mock(return_value=data)
        self.run.run_main=mock_data
        r = self.run.run_main(url,header,'POST',data)
        print(r)
        self.assertEqual(r["time"],1553852672532,"测试成功")
        # print(json.dumps(r))
# #
#
#
if __name__=='__main__':
    unittest.main()
# f=open('C:\\test2\\login.yaml',encoding='utf-8')
# res=yaml.load(f)
# print(res)
# print(type(res))



