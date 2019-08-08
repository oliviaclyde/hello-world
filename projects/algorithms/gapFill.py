#Hypothesis: Stocks that gap up/down will fill the gap the majority of the time.
#If we are short after a gap up and long after a gap down we will be profitable.

#Recommendations: Play the S&P 500, daily bars over 5+ years.

#Ideas:
#- Have a training method that will take the data, and iterate through each day simulating the strategy. Have it record the gains/losses
#- Calculate the benchmark (If you had merely just bought and held throughout the entire dataset, what return would you have?)

#- If you wanna get more advanced, don't just record percentage gains/losses but compound the returns
#(ie. start with a portfolio balance of 30k, and each time your algo wants to buy or sell it does the maximum number of shares.
#This effectively compounds your returns and could increase your performance vs the benchmark)


#---------------------------------------------------------------------------------------------#
#Webscrape using Beautiful Soup
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/SPY/history?period1=1564812000&period2=1565244000&interval=1d&filter=history&frequency=1d"
html = requests.get(url, verify=True)
soup = BeautifulSoup(html.content, 'lxml')
title = soup.title
print(title)
#tr = table rows; th = table headers; td = table cells

#rows = soup.find_all("tr", {"class": "BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)"})
rows = soup.find_all("table", {"class": "W(100%) M(0)"})
#print(rows)
#iterate through the rows to make the data into a list
for row in rows:
    #row_td = row.find_all("td")
    row_tr = (row.contents[0].find_all({"tr": "Fw(400) Py(6px)"}))
    row_td = (row.contents[1].find_all({"td": "Py(10px) Pstart(10px)"}))
#print(row_td)
#print(row_tr)
type(row_tr)
type(row_td)
#remove HTML tags
str_cells = str(row_tr) + str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
print(cleantext)

# df = pd.DataFrame(rows)
#df.head(10)
#Write API wrapper to connect to IEX to pull 5 yrs of SPY daily bars
#Need to hide API keys in environment  variables

#OOP import the wrapper into this file

#Create a class to store the retrived data

#Convert the file to JSON

#Convert the file to df using pandas

#Copy the df to new df using only open close bars

#Create benchmark to calc return of buy and hold
#Last data point - 1st data point / 1st data point = benchmark return

#Create a method of the class to iterate over the dataset

#Calculate the "gap"
#If gap up (open is higher than prior close, then short the stock)
#If gap down (open is lower than prior close, then buy)
#Record the gains/losses
#Do you then sell????? How do you capture the return?
#New - Old / Old = return
#Add this to a variable called total return

#Calculate the compounded return, assuming $30k investment
