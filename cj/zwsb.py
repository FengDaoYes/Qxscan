# -*- coding: utf-8 -*-
import re
import requests
import threading
import queue
import socket


def zwzd():
	zwlb = []
	with open('./zd/zwsb/cms.txt',encoding='utf-8') as txt:
		for i in txt:
			i.strip()
			i.strip('\n')
			i.strip('\r')
			q = re.findall('.*?\|',i)
			zwlb.append(q)
	return zwlb



def zid(lb):
		
	words = queue.Queue()
	
	for i in lb:
		words.put(i)
			
	return words

def guol(i):
	i = i.replace("%0a","")
	i = i.replace("%0A","")
	i = i.replace("%0d","")
	i = i.replace("%0D","")
	i = i.replace("\n","")
	i = i.replace("\r","")
	i.strip()
	return i

def zwsb(host,port,que,pd):
	while not que.empty():
		if pd == "1":
			url = "https://"+host+":"+port+"/"
		else:
			url = "http://"+host+":"+port+"/"
		header = {
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
			'Connection': 'close'
			}
		i = que.get()
		w = i[0]
		e = i[1]
		w = w.replace("|","")
		e = e.replace("|","")
		w = guol(w)

		urls = url+w
		requests.adapters.DEFAULT_RETRIES = 5
		s = requests.session()
		r = s.head(urls,timeout=5,headers=header)
		if r.status_code == 200:
			print("使用cms为："+e+"\n验证文件为："+urls)
		s.close()

	

	


def message():
	global pdhost
	global pddk

	pdhost = input('请输入要识别的域名或ip[当前则回车]: ')
	pddk = input("请输入目标的端口[80则直接回车]: ")

#获取域名的ip
def getIP(domain):
	ip = socket.gethostbyname(domain)
	return ip

def saomiao(host,port):
	try:
		socket.setdefaulttimeout(1)
		lianjie = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		ip = getIP(host)
		lianjie.connect((ip,int(port)))
		lianjie.close()		
		return True
	except:
		return False


def zwsb_main(host):
	global pdhost
	global pddk

	print("==========进入指纹识别项==========")
	ip = input('请输入要识别的域名或ip[当前则回车]: ')
	dk = input("请输入目标的端口[80则直接回车]: ")
	pd_https = input("是否为https？否则直接回车[y]: ")
	xc = input("请输入线程[默认10]: ")
	

	if ip:
		pdhost = ip
	else:
		pdhost = host
		
	if dk:
		pddk = dk
	else:
		pddk = "80"
		
	if pd_https:
		pdhttps = "1"
	else:
		pdhttps = "0"
	if xc:
		pdxc = xc
	else:
		pdxc = 10

	while True:
		panduan = saomiao(pdhost,pddk)
		if panduan == True:
			break
		else:
			print("目标无法连接，请重新输入......")
			message()
	print("==开始识别==")
	zwzds = zwzd()

	zwzdqueu = zid(zwzds)
	
	threadings = []


	for i in range(0,int(pdxc)):
		t = threading.Thread(target=zwsb,args=(pdhost,pddk,zwzdqueu,pdhttps,))
		threadings.append(t)
		t.start()

	for t in threadings:
		t.join()

	print("==========扫描完成==========")

