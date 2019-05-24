import yaml
import os
yaml.warnings({'YAMLLoadWarning': False})
# cur=os.path.dirname(os.path.relpath(__file__))
# def get_token(yamlName="token.yaml"):
#     p=os.path.join(cur,yamlName)
#     f=open(p)
#     a=f.read()
#     t=yaml.load(a)
#     f.close()
#     return t["token"]
# if __name__=="__main__":
#     print(get_token())
# def get_token():
#     f = open('C:\\test2\\common\\token.yaml', encoding='utf-8')
#     # print(type(f))
#     res= yaml.load(f)
#     # print(type(res))
#     f.close()
#     return res["token"]
# if __name__=="__main__":
#     print(get_token())
def get_login():
    f = open('C:\\test2\\login.yaml', encoding='utf-8')
    # print(type(f))
    res= yaml.load(f)
    # print(type(res))
    f.close()
    return res["data"]
if __name__=="__main__":
    print(get_login())