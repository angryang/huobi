!/usr/bin/dev python
improt MySQLdb

def open():
	return MySQLdb.connect(host='localhost',user='root',passwd='root',db='mysql',port=3306)

def set(cmd):
	conn = open()
	try:
		cur = conn.cursor()
		cur.execute(cmd)
		cur.close()
		conn.commit()
		return datas
	except Exception,ex:
		conn.rollback()
		return (500, ex.message)
	finally:
		conn.close()

def get(cmd):
	conn = open()
	try:
		cur = conn.cursor()
		cur.execute(cmd)
		datas = cur.fetchall()
		cur.close()
		return (0, datas)
	except Exception,ex:
		return (500, ex.message)
	finally:
		conn.close()

def __test__():
	pass

if __name__ = "__main__":
	__test__()