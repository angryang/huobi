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
ACCESS_KEY=""
SECRET_KEY=""
#API_URL=r"https://api.huobi.com/apiv2.php"

import httplib, urllib
import hashlib
import time
import collections

def httpRequest(params):
    body=urllib.urlencode(params)
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    conn = httplib.HTTPSConnection("api.huobi.com")
    conn.request("POST", r"/apiv2.php", body, headers)
    response = conn.getresponse()
##    print response.status, response.reason
    data = response.read()
    print data
    conn.close()

def sortDict(params):
    return collections.OrderedDict(sorted(params.items()))

def md5(info):
    m = hashlib.md5()
    m.update(info)
    return m.hexdigest()

def createSign(params):
    params['secret_key']=SECRET_KEY
    params=sortDict(params)
    preSign=urllib.urlencode(params)
    sign=md5(preSign)
    return sign.lower()

def sendToApi(params, extras):
    params['access_key'] = ACCESS_KEY;
    params['created'] = int(time.time()+0.5);
    params['sign'] = createSign(params);
##    if(extras):
##    	params = array_merge(params, extras);
##    print params
    return httpRequest(params)

def getAccountInfo():
    params={}
    extras={}
    params["method"]="get_account_info"
    result=sendToApi(params,extras)
    print result

getAccountInfo()
