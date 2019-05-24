#coding:utf-8
import requests,json
class RunMain:
    def __init__(self,url,headers,method,data=None):
        self.r=self.run_main(url,headers,method,data)
    def send_get(self,url,data,header,):
        r=requests.get(url=url,headers=header,data=data).json()
        return json.dumps(r,indent=2,sort_keys=True)
    def send_post(self,url,data,header,):
        r=requests.post(url=url,headers=header,data=data).json()
        return json.dumps(r,indent=2,sort_keys=True)
    def run_main(self,url,headers,method,data=None):
        r=None
        if method=="GET":
            r=self.send_get(url,data,headers)
        else:
            r=self.send_post(url,data,headers)
        return json.loads(r)
if __name__=='__main__':
    url="http://test.weifenghr.com/wf-login/api/user/login"
    header={"email": "ceshi@ctgtmo.com",
                        "Content-Type": "application/json"}
    data="{\"email\":\"yunpeng.zhang@ctgtmo.com\",\"password\":\"42f2c22d3a955b210c10d16d43472b30\",\"validateCode\":\"4567\",\"time\":1553852672532}"
    run=RunMain(url,header,"POST",data)
    print(run.r)
print(dir(RunMain))