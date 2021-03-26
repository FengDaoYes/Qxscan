import requests
import re
import socket

def getIP(domain):
	ip = socket.gethostbyname(domain)
	return ip

def wzcx(ip):
	header={
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
	'Accept':'*/*',
	'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Accept-Encoding':'gzip, deflate',
	'Referer':'https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=ip',
	'Connection':'close'}
	url="""http://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query="""+ip+"""&co=&resource_id=6006&t=1594534781056&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery110206818778002992059_1594534767480&_=1594534767481"""
	url=url.replace("%0A%09%09","")
	r = requests.get(url,headers=header)
	w = r.text
	q = re.findall("\"location\":\".*?\"",w)
	e = q[0]
	t = e.replace("\"location\":\"","")
	y = t.replace('"',"")
	return y

def dzcx_main(host):
	if "/" in host:
		host = host.replace("/","")
	try:
		ips = getIP(host)
		dizhi = wzcx(ips)
	except:
		dizhi = "查询失败！"
	return dizhi