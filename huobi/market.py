# -*- coding: UTF-8 -*-
#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      dell
#
# Created:     14/10/2014
# Copyright:   (c) dell 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import httplib, urllib
import json, time, sys
from threading import Thread, Lock

lock = Lock()

def httpRequest(url, params={},headers={}):
    #print url
    body=None
    if params:
        body=urllib.urlencode(params)

    protocol="http"
    index=0
    if (r"http://" in url):
        url=url.replace("http://","")
    elif (r"https://" in url):
        protocol="https"
        url=url.replace("https://","")
    else:
        pass

    ##print url
    if (".com" in url):
        index=url.find(".com")+4
    elif(".cn" in url):
        index=url.find(".cn")+3
    elif(".net" in url):
        index=url.find(".net")+4

    ##print url[:index+4]
    if (protocol=="http") :
        conn=httplib.HTTPConnection(url[:index])
    else:
        conn=httplib.HTTPSConnection(url[:index])
    conn.request("GET", url[index:], body, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return json.loads(data)

def getCurrentMarket(website):
    if (website=="huobi") :
        return getHuobiCurrentMarket()
    else :
        pass

def getRate():
    return 6.11
##    headers = {"Content-type":"application/json"}
##    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36"
##    params = {"from":"USD","to":"CNY"}
##    return httpRequest(r"http://rate-exchange.appspot.com/currency", params, headers)

def getHuobiCurrentMarket():
    return httpRequest(r"http://market.huobi.com/staticmarket/ticker_btc_json.js")

def getOkCoinCurrentMarket():
    return httpRequest(r"https://www.okcoin.cn/api/ticker.do")

def getBtStempCurrentMarket():
    #headers = {"Content-type":"text/html"}
    return httpRequest(r"https://www.bitstamp.net/api/ticker/")

class GrabData(Thread):
    def __init__(self):
        super(GrabData, self).__init__(name="GrabData")
        self.setDaemon(True)

    def run(self):
        super(GrabData, self).run()
        self.working=True
        while self.working:
            lock.acquire()
            self.worker()
            lock.release()
            time.sleep(10)

    def worker(self):
        huobiInfo=getHuobiCurrentMarket()
        #print(huobiInfo)
        btStempInfo=getBtStempCurrentMarket()
        #print(btStempInfo)
        if huobiInfo and btStempInfo:
            priceOfHuoBi = huobiInfo["ticker"]["last"]
            priceOfBtStemp =  btStempInfo["last"]
            priceBetweenHuoBiAndBtStemp = float(priceOfBtStemp) * rate - float(priceOfHuoBi)
            sys.stdout.write("\n"+time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time())) + "  ")
            sys.stdout.write(u"火币网：%s BtStemp: %s 最新差价: %s" % (priceOfHuoBi, priceOfBtStemp, priceBetweenHuoBiAndBtStemp))

    def join(self):
        self.working=False
        super(GrabData, self).join()

##infoOfHuobi=getHuobiCurrentMarket()
##infoOfOkcoin=getOkCoinCurrentMarket()
##print infoOfHuobi
##print infoOfOkcoin

rate = getRate()
grab = GrabData()
grab.start()

import os
os.system("pause")
sys.stdout.write(u"正在结束线程，请稍等。。。")
grab.join()

##info=r"http://market.huobi.com/staticmarket/ticker_btc_json.js"
##index1=0
##if (".com" in info):
##    index1=info.find(".com")
##print info[:index1+4]
##print info[index1+4:]


