!/usr/bin/env python
import dbcomm

def insert(params):
    cmd = "INSERT INTO btc_market  (%s,%s,%s,%s,%s,%s,%s)" % truple(params)
    return dbcomm.execCmd(cmd)

def update(params):
	cmd = 