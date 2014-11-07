!/usr/bin/env python
import dbcomm

def insert(params={}):
	if not params:
		return
    cmd = "INSERT INTO btc_market  (%s,%s,%s,%s,%s,%s,%s)" % truple(params)
    return dbcomm.execCmd(cmd)

def update(params={}):
	if not params:
		return
	cmd = ""
	pass

def search(params={}):
	if not params:
		return
	pass

def delete(params={}):
	pass