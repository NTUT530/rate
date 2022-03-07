import urllib.request as request
from bs4 import BeautifulSoup as sp 
import math

#正損值
difference=[-430,160]

#buy_in
#(1997.5,3.67)
data=(1749,10,1803,10)
li1=[]
li2=[]
i=0
while i<len(data):
	value=(data[i]*data[i+1])
	li1.append(value)
	i+=2
buy_in=sum(li1)

i=0
while i<len(data):
	value=(data[i+1])
	li2.append(value)
	i+=2
g_buy=sum(li2)

#sell_out
sell_data=()
li3=[]
li4=[]
i=0
while i<len(sell_data):
	value=(sell_data[i]*sell_data[i+1])
	li3.append(value)
	i+=2
sell_out=sum(li3)

i=0
while i<len(sell_data):
	value=(sell_data[i+1])
	li4.append(value)
	i+=2
g_sell=sum(li4)

gram=g_buy-g_sell

#gold
url="https://rate.bot.com.tw/gold?Lang=zh-TW" #台銀黃金利率網
with request.urlopen(url) as response :
	data=response.read().decode("utf-8")
root=sp(data,"html.parser")
gold_in=int(root.find_all("td")[5].text.replace("回售","").strip())
gold_out=int(root.find_all("td")[2].text.replace("買進","").strip())

now_sell=gold_in*gram+sell_out
earn=now_sell-buy_in

print("銀行買進",gold_in,"NTD/g")
print("已買入",g_buy,"g ,NT$ %8.2f"%buy_in)
print("已賣出",g_sell,"g ,NT$ %8.2f"%sell_out)
print("剩餘g數",gram,"g")
print("現在可賣 NT$ %8.2f" % now_sell)
print("進賺 NT$ %7.2f" % earn)
print("正損值",sum(difference))




#國際金價
#1troy ounce=31.1035g
url="https://www.goldlegend.com/international"
with request.urlopen(url) as response :
    data=response.read().decode("utf-8")
root=sp(data,"html.parser")
national_gold=float(root.find("h2").text)

#USD
url="https://rate.bot.com.tw/xrt?Lang=zh-TW"
with request.urlopen(url) as response :
  data=response.read().decode("utf-8")
root=sp(data,"html.parser")
USD_in=float(root.find_all("td")[3].text.strip())
USD_out=float(root.find_all("td")[4].text.strip())

if gram==0:
	pass
elif earn<0:
	g_increase=(-earn/gram)
	g_increase=math.ceil(g_increase)
	stEx=int(gold_in)+g_increase
	us_stEx=round(stEx*31.1035/USD_out,2)
	print("再",g_increase,"(",stEx,"NTD/g)塊會賺錢")
	print("      (",us_stEx,"USD/ozt)")
	
print("\n-----------我是分隔線-----------\n")
father=math.floor(15000/buy_in*earn)
mother=math.floor(20000/buy_in*earn)
mine=earn-father-mother
print("分益")
print("mine NT$ %6.2f" %mine)
print("father NT$" ,father)
print("mother NT$" ,mother)
print("\n-----------我是分隔線-----------\n")

print("國際金價",national_gold,"USD/ozt")		
						
print("美金即期賣出匯率",USD_out,"NTD/USD")

tw_oz_national=national_gold*USD_out
tw_g_national=round(tw_oz_national/31.1035,2)
tw_oz_national=round(tw_oz_national,2)
print('折合台幣',tw_oz_national,"NTD/ozt\n         ",tw_g_national,"NTD/g")
print("\n-----------我是分隔線-----------\n")

print("      外幣計價黃金存摺牌價 ")

import urllib.request as request
from bs4 import BeautifulSoup as sp
import requests

url="https://rate.bot.com.tw/gold/obu"
with request.urlopen(url) as response :
    data=response.read().decode("utf-8")
root=sp(data,"html.parser")
time=root.find_all("td")[0].text.strip()
usd_ozt_in=float(root.find_all("td")[3].text.strip())
usd_ozt_out=float(root.find_all("td")[4].text.strip())

tw_ozt_in=round(usd_ozt_in*USD_out,2)
tw_ozt_out=round(usd_ozt_out*USD_out,2)

print(" "*13+time)
print("銀行買進",usd_ozt_in,"USD/ozt\n        ",tw_ozt_in,"NTD/ozt\n")
print("銀行賣出",usd_ozt_out,"USD/ozt\n        ",tw_ozt_out,"NTD/ozt")
