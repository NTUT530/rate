import urllib.request as request
from bs4 import BeautifulSoup as sp 
import math

#正損值
difference_tw=[-430,160]
difference_us=[0,0]
#buy_in
data_tw=(1749,10,1803,10)
data_us=(1997.5,3.67)
data_USD=(28.075,2000,28.06,5345.69)
li1=[]
li2=[]
i=0
while i<len(data_tw):
	value=(data_tw[i]*data_tw[i+1])
	li1.append(value)
	i+=2
buy_in_tw=sum(li1)

i=0
while i<len(data_tw):
	value=(data_tw[i+1])
	li2.append(value)
	i+=2
g_buy_tw=sum(li2)

#sell_out
sell_data_tw=()
li3=[]
li4=[]
i=0
while i<len(sell_data_tw):
	value=(sell_data_tw[i]*sell_data_tw[i+1])
	li3.append(value)
	i+=2
sell_out_tw=sum(li3)

i=0
while i<len(sell_data_tw):
	value=(sell_data_tw[i+1])
	li4.append(value)
	i+=2
g_sell_tw=sum(li4)

gram_tw=g_buy_tw-g_sell_tw

#gold
url="https://rate.bot.com.tw/gold?Lang=zh-TW" #台銀黃金利率網
with request.urlopen(url) as response :
	data=response.read().decode("utf-8")
root=sp(data,"html.parser")
gold_in_tw=int(root.find_all("td")[5].text.replace("回售","").strip())
gold_out_tw=int(root.find_all("td")[2].text.replace("買進","").strip())

now_sell_tw=gold_in_tw*gram_tw+sell_out_tw
earn_tw=now_sell_tw-buy_in_tw

print("銀行買進",gold_in_tw,"NTD/g")
print("已買入",g_buy_tw,"g ,NT$ %8.2f"%buy_in_tw)
print("已賣出",g_sell_tw,"g ,NT$ %8.2f"%sell_out_tw)
print("剩餘g數",gram_tw,"g")
print("現在可賣 NT$ %8.2f" % now_sell_tw)
print("進賺 NT$ %7.2f" % earn_tw)
print("正損值NTD$",sum(difference_tw))




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

if gram_tw==0:
	pass
elif earn_tw<0:
	g_increase=(-earn_tw/gram_tw)
	g_increase=math.ceil(g_increase)
	stEx=int(gold_in_tw)+g_increase
	us_stEx=round(stEx*31.1035/USD_out,2)
	print("再",g_increase,"(",stEx,"NTD/g)塊會賺錢")
	print("      (",us_stEx,"USD/ozt)")
	
print("\n-----------我是分隔線-----------\n")
father=math.floor(15000/buy_in_tw*earn_tw)
mother=math.floor(20000/buy_in_tw*earn_tw)
mine=earn_tw-father-mother
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
print("\n-----------我是分隔線-----------\n")

li1=[]
li2=[]
i=0
while i<len(data_us):
	value=(data_us[i]*data_us[i+1])
	li1.append(value)
	i+=2
buy_in_us=sum(li1)

i=0
while i<len(data_us):
	value=(data_us[i+1])
	li2.append(value)
	i+=2
ozt_buy_us=sum(li2)

#sell_out
sell_data_us=()
li3=[]
li4=[]
i=0
while i<len(sell_data_us):
	value=(sell_data_us[i]*sell_data_us[i+1])
	li3.append(value)
	i+=2
sell_out_us=sum(li3)

i=0
while i<len(sell_data_us):
	value=(sell_data_us[i+1])
	li4.append(value)
	i+=2
ozt_sell_us=sum(li4)

gram_us=ozt_buy_us-ozt_sell_us

now_sell_us=usd_ozt_in*gram_us+sell_out_us
earn_us=now_sell_us-buy_in_us
tw_earn_us=earn_us*USD_in

print("銀行買進",usd_ozt_in,"USD/ozt")
print("已買入",ozt_buy_us,"ozt ,USD$ %8.2f"%buy_in_us)
print("已賣出",ozt_sell_us,"ozt ,USD$ %8.2f"%sell_out_us)
print("剩餘ozt數",gram_us,"ozt")
print("現在可賣 USD$ %8.2f" % now_sell_us)
print("進賺 USD$ %7.2f" % earn_us)
print("     NTD$ %8.2f" % tw_earn_us)
print("正損值USD$",sum(difference_us))
print("      NTD$",sum(difference_us)*USD_in)

if gram_us==0:
	pass
elif earn_us<0:
	ozt_increase=(-earn_us/gram_us)
	ozt_increase=math.ceil(ozt_increase)
	stEx=int(usd_ozt_in)+ozt_increase
	print("再",ozt_increase,"(",stEx,"USD/ozt)塊會賺錢")
 
print("\n-----------我是分隔線-----------\n")

print("           美金 ")
print("即期本行買入 ",USD_in,"\n即期本行買出 ",USD_out)
li1=[]#total price
li2=[]#total USD
i=0
while i<len(data_USD):
	value=(data_USD[i]*data_USD[i+1])
	li1.append(value)
	i+=2
buy_in_USD=sum(li1)

i=0
while i<len(data_USD):
	value=(data_USD[i+1])
	li2.append(value)
	i+=2
buy_USD=sum(li2)

#sell_out
sell_data_USD=()
li3=[]
li4=[]
i=0
while i<len(sell_data_USD):
	value=(sell_data_USD[i]*sell_data_USD[i+1])
	li3.append(value)
	i+=2
sell_out_USD=sum(li3)

i=0
while i<len(sell_data_USD):
	value=(sell_data_USD[i+1])
	li4.append(value)
	i+=2
sell_USD=sum(li4)

print("\n剩餘USD$",buy_USD-sell_USD)
print("買入價格NTD$",round(buy_in_USD,4))
print("現在賣可賺NT$",round(((buy_USD-sell_USD)*USD_in)-buy_in_USD,4))
