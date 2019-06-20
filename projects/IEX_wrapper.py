#Writing my own wrapper to connect to IEX API
#Websites have APIs to give out their data and allow your web application to communication directly to their data
#Log into a website. I am using IEX. Create an account. Find API key

#Questions
#What is best practice for storing your API token? Not in the source file?


import requests
import json


#Basic API wrapper

#api_token  = 'pk_2ce3dd5ed10d46ba9d9f306e2971be3d'
#response = requests.get("https://cloud.iexapis.com/v1/stock/AAPL/price/2?token=" +api_token)

#Sandbox API wrapper
#Couldn't connect sucessfully to sandbox_url
sandbox_token = 'Tpk_506f3a9b406f4477bdaf53f923bf2265'
response = requests.get("https://sandbox.iexapis.com/beta/stock/AAPL/2?token=Tpk_506f3a9b406f4477bdaf53f923bf2265")



#Test-Driven Development (TDD)
#Write a test then design the code so it passes the Test
#Here we want to test whether or not we have a connection to the API]
#We can accomplish this by seeing if a query will return data

if response.status_code == 200:
    #return json.loads(response.content)
    print("Connecton Successful.")
    print(response.content)
else:
    print('Connection Error. Try again.')

"""
#Create API wrapper to swtich between sandbox and production
api_token  = 'pk_2ce3dd5ed10d46ba9d9f306e2971be3d'
response = requests.get("https://cloud.iexapis.com/v1/stock/AAPL/price/2?token=" +api_token)
sandbox_token = 'Tpk_506f3a9b406f4477bdaf53f923bf2265'
api_url = 'https://cloud.iexapis.com/'
sandbox_url = 'https://sandbox.iexapis.com'

#Create an API wrapper using headers
#Getting a JSON error
#headers = {"Authorization": "token pk_2ce3dd5ed10d46ba9d9f306e2971be3d"}
#Couldn't get headers=headers inisde requests.get to work
headers = {"Authorization": "pk_2ce3dd5ed10d46ba9d9f306e2971be3d", "User-Agent": "oliviaclyde"}
response = requests.get("https://cloud.iexapis.com/v1/stock/AAPL/price/", headers=headers)
data = response.json()
status = response.status_code
print(response.url)


#Create API wrapper using variables for endpoints





#Create API wrapper using OOP
class IEX:
    pass

#self.secret_token
#self.api_token
#self.sandbox_token
#self.sandbox_url
#self.api_url


"""








"""
#Class Attributes
api_url = 'https://cloud.iexapis.com/'
sandbox_url = 'https://sandbox.iexapis.com'
#publishable token

api_key = 'pk_2ce3dd5ed10d46ba9d9f306e2971be3d'
#sandbox token
sandbox_key  = 'Tpk_506f3a9b406f4477bdaf53f923bf2265'

"""
"""
#instatiate IEX class
class IEX:
#3 python modules to access http site: urllib, urlib2, requests. Requests uses urllib3
    import requests
    import json
    def __init__(self, api_url, api_key,sandbox=' '):
        if sandbox=True:
            self.sandbox_url = sandbox_url
            self.sandbox_key = sandbox_key
        else:
            #use api_key
            self.api_url = api_url
            self.api_key = api_key

    def connect:




parameters =
response = requests.get('https://cloud.iexapis.com/' + params=parameters)
status_code = response.status_code
content = response.content






class connect(self, is_connected, not_connected):
    self.is_connected = is_connected
    self.not_connected = not_connected
        if is_connected:
            def data:

                print("Connection established")
        else:
            print("Not connected. Please try again.")

#Could make two APIs, one for sandbox and one live


#I need to establish a connection then test that connection by calling a function of the class
#I need to be able to switch between live connection and sandbox mode







#    self.symbol = symbol
#    self.companyname = companyname
#    self.industry = industry


"""
"""
api_key = print(input('Enter a ticker symbol: '))
url = 'https://api.iextrading.com/1.0/stock/api_key=' +api_key +'/company'
"""



"""
def connection:
    #authenticate user
    authenticate.authenticate(request)
    return true
"""
#json_obj = urllib2.urlopen(url)

#data = json.load(json_obj)
