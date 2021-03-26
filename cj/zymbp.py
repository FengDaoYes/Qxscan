import socket
import requests
import threading
import re
import queue

list_ip = []


def getIP(domain):
	ip = socket.gethostbyname(domain)
	return ip

def zid(wenjian):
		
	words = queue.Queue()
	
	with open(wenjian,encoding='gbk') as zd:
		for i in zd:
			words.put(i)
			
	return words


def saomiao(url):
	try:
		ip = socket.gethostbyname(url)
		return ip
	except:
		return "None"


def main_a(zym,yuming):
	while True:
		if zym.empty():
			return
		else:
			i = zym.get()
			i = i.strip()
			url = i+"."+yuming
			zhi = saomiao(url)
			if zhi != "None":
				urls = "http://"+url+"/"
				try:
					qingqiu = requests.get(urls,timeout=2)
				except:
					pass
				try:
					qingqiu.encoding = qingqiu.apparent_encoding
					wangye = qingqiu.text
					title = re.findall("<title>.*?</title>",wangye)
				except:
					pass
				try:
					w = qingqiu.headers
				except:
					pass
				try:
					if w['server']:
						zhi += "\n服务器："+w['server']
				except:
					pass
				try:
					if w['X-Powered-By']:
						zhi += "\n信息："+w['X-Powered-By']
				except:
					pass
				try:
					if title:
						biaoti = title[0]
						biaotis = biaoti.replace("<title>","") 
						biaotiss = biaotis.replace("</title>","")
						zhi += "\n标题:"+biaotiss
				except:
					pass
				zhi += "\n================================="
				print("[+]"+"http://"+url+"/\t-开启-\n解析IP为:"+zhi)



def zymbp_main(yuming):
	global list_ip
	threads = []
	print("==进入子域名爆破项==\n")
	pd = input("请输入要爆破的根域名(当前域名请直接回车):")
	if pd:
		yumings = pd
	else:
		yumings = yuming
	xcs = input("请输入线程: ")
	if xcs:
		xc = xcs
	else:
		xc = 10

	zym = zid("./zd/zymbp/zym.txt")

	for i in range(int(xc)):
		t = threading.Thread(target=main_a,args=(zym,yumings,))
		threads.append(t)
		t.start()
	
	for t in threads:
		t.join()
	print("==扫描完成==\n")