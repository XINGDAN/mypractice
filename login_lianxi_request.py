import pytest
import requests

@pytest.mark.parametrize("username,password",[(18715626526,123456)])
def test_xinshetong_login(username,password):
    url = 'https://www.xinshetong.com/apis/login'
    myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0','Conternt-Type':'application/x-www-form-urlencoded'}
    payload = {'username':str(username),'password':str(password),'vcode':'','customerType':'enterprise'}
    res = requests.post(url,headers=myheaders,verify=False,data=payload)

    print(res.status_code)


    tishi = (res.json().get("msg"))
    sussess_yanzhen = (res.json().get("success"))
    assert tishi == "登录成功"
    #assert sussess_yanzhen == "true"
