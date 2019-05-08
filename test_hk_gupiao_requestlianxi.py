import pytest
import requests

@pytest.mark.parametrize("size,order",[(10,"desc"),(20,"asc")])
def test_hk_gupiao_requestlianxi(size,order):
    #?page=1&size=30&order=desc&orderby=percent&order_by=percent&market=HK&type=hk&_=1557303482022
    url = 'https://xueqiu.com/service/v5/stock/screener/quote/list'

    myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
    payload = {'page':'1','size':str(size),'order':order,'orderby':'percent','order_by':'percent','market':'HK','type':'HK','_':'1557303482022'}
    res = requests.get(url,headers=myheaders,verify=False,params=payload)

    #res.json.get("data").get("list")[0].get("percent")
    #print(res.json())
    print(res.status_code)
    #j = print(res.json.get("data").get("list")[0].get("percent"))
    assert res.status_code == 200


