# -*- coding: utf-8 -*-
import socket
import requests
import queue
import re
import threading

ipkf_lb = []


def xxx(ipdss):
	while not ipdss.empty():
		host = ipdss.get()
		host = host.strip()
		url = "http://"+host
		try:
			qingqiu = requests.get(url,timeout=2)
		except:
			print('[-]'+host+"端口开放但连接错误...")
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
		xinxi = ""
		try:
			if w['server']:
				xinxi += "服务器："+w['server']
		except:
			pass
		try:
			if w['X-Powered-By']:
				xinxi += "\n信息："+w['X-Powered-By']
		except:
			pass
		try:
			if title:
				biaoti = title[0]
				biaotis = biaoti.replace("<title>","") 
				biaotiss = biaotis.replace("</title>","")
				xinxi += "\n标题:"+biaotiss
		except:
			pass
		xinxi += "\n==========================================="
		print("[+]"+url+"\t+开启+"+"\n"+xinxi)


def getnwip():
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		s.connect(('8.8.8.8',80))
		ip = s.getsockname()[0]
		s.close()
		return ip
	finally: 
		s.close()
		return False


def ipcl_24(ip):
	ip = ip.replace("/24","")
	ip.strip()
	q = ip.split(".")
	liebiao = []
	for i in range(0,256):
		xxx = q[0]+"."+q[1]+"."+q[2]+"."+str(i)
		liebiao.append(xxx)
	return liebiao


def ipcl_16(ip):
	ip = ip.replace("/16","")
	ip.strip()
	q = ip.split(".")
	liebiao = []
	for i in range(0,256):
		xxx = q[0]+"."+q[1]+"."+i
		for x in range(0,256):
			qqq = xxx+"."+x
			liebiao.append(qqq)

	return liebiao

def ipcl_8(ip):
	ip = ip.replace("/8","")
	ip.strip()
	q = ip.split(".")
	liebiao = []
	for i in range(0,256):
		xxx = q[0]+"."+i
		for x in range(0,256):
			qqq = xxx+"."+x
			for f in range(0,256):
				fff = qqq+"."+f
				liebiao.append(fff)
	return liebiao

def zid(liebiao):
		
	words = queue.Queue()
	for i in liebiao:
		i.strip()
		words.put(i)
				
	return words

def saomiao(ipq):
	global ipkf_lb
	dk = ['80','8080','8081','8082','443','888','8888','88']
	while not ipq.empty():
		ip = ipq.get()
		ip = ip.strip()
		for i in dk:
			try:
				socket.setdefaulttimeout(2)
				lianjie = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				lianjie.connect((ip,int(i)))
				xinxi = ip+":"+str(i)
				xinxi.strip()
				ipkf_lb.append(xinxi)
				lianjie.close()
			except:
				pass

def webjc_main():
	print("==========进入检测存活web项==========")
	ipd = input("请输入要检测存活的ip或ip段: ")
	xc = input('请输入线程数[默认为10]： ')
	while True:
		if ipd:
			ipd = ipd.strip()
			if '/24' in ipd:
				ipds = ipcl_24(ipd)
				break
			elif '/16' in ipd:
				ipds = ipcl_16(ipd)
				break
			elif '/8' in ipd:
				ipds = ipcl_8(ipd)
				break
			else:
				ipds = []
				ipds.append(ipd)
				break

		else:
			ipd = getnwip()
			if ipd:
				ipd.strip()
				ipds = ipcl_24(ipd)
				break
			else:
				print('无法获取当前IP的值......')
				ipd = input("请输入要检测存活的ip或ip段: ")
			

	if xc:
		xc = int(xc)
	else:
		xc = 10


	ipdd = zid(ipds)
	print('开始扫描......')
	threads = []

	for i in range(0,int(xc)):
		t = threading.Thread(target=saomiao,args=(ipdd,))
		threads.append(t)
		t.start()
	for t in threads:
		t.join()
	global ipkf_lb
	
	print('开始识别......')
	threadings = []

	iplbs = zid(ipkf_lb)
	for i in range(0,int(xc)):
		t = threading.Thread(target=xxx,args=(iplbs,))
		threadings.append(t)
		t.start()
	
	for t in threadings:
		t.join()

	print('==========扫描完成==========')



