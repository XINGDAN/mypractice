import requests

#def get_top_stock():
myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
url = "https://xueqiu.com/service/v5/stock/screener/quote/list"
myproxies = {
    "http":"127.0.0.1:8888",
    "https":"127.0.0.1:8888",
}

payload = {'type':'sha','order_by':'percent','order':'desc','size':'10',"page":'1','_':'1557223888465'}
r = requests.get(url,verify=False,headers=myheaders,proxies=myproxies,params=payload)

#r = requests.get("https://xueqiu.com/hq")
#print(r.status_code)
print(r.json())
print(r.status_code)

# url = "https://xueqiu.com/service/v5/stock/screener/quote/list?type=sha&order_by=percent&order=desc&size=10&page=1&_=1555054946846"
# para = {'type':'sha','order_by':'percent','size':'10','page':'1','_':1555054946846}
#r = requests.get(url,verify=False,headers=myheaders,playod=para)