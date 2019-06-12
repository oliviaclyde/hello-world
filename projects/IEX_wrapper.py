#Writing my own wrapper to connect to IEX API
#Websites have APIs to give out their data and allow your web application to communication directly to their data
#Log into a website. I am using IEX. Create an account. Find API key

#All endpoints are prefixed with: https://api.iextrading.com/1.0
#url = 'https://api.iextrading.com/1.0/stock/aapl/company'


class IEX:
#3 python modules to access http site: urllib, urlib2, requests. Requests uses urllib3
    import requests
    import json

IEX_api = 'ce20f91b2dc84a899ff1e0387a002aee'
url = 'https://api.iextrading.com/1.0/stock/api_key=' +api_key +'/company'


json_obj = urllib2.urlopen(url)

data = json.load(json_obj)

for item in data:
    print item['symbol']
    print item['companyname']
    print item['industry']

api_key = print(input('Enter a ticker symbol: '))
url = 'https://api.iextrading.com/1.0/stock/api_key=' +api_key +'/company'




"""
def connection:
    #authenticate user
    authenticate.authenticate(request)
    return true
"""
