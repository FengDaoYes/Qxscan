# -*- coding: utf-8 -*-
import os
import sys
import platform
import threading
import re
import queue


def xitong():
	pd = platform.system()
	return pd

def guol(i):
	i = i.replace("%0a","")
	i = i.replace("%0A","")
	i = i.replace("%0d","")
	i = i.replace("%0D","")
	i = i.replace("\n","")
	i = i.replace("\r","")
	i.strip()
	return i

def zid(liebiao):
		
	words = queue.Queue()
	for i in liebiao:
		i.strip()
		words.put(i)
				
	return words


def saomiao(ipz):
	if xitong() == "Linux":
		pingz = "c"
	elif xitong() == "Windows":
		pingz = "n"
	else:
		print("当前操作系统不支持")
		sys.exit()

	while not ipz.empty():
		i = ipz.get()
		i = guol(i)
		output = os.popen('ping -'+pingz+' 1 '+i)
		for w in output:
			if str(w).upper().find('TTL')>=0:   
				print('[+]存活IP:'+i+'\n')

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
		xxx = q[0]+"."+q[1]+"."+str(i)
		for x in range(0,256):
			qqq = xxx+"."+str(x)
			liebiao.append(qqq)

	return liebiao

def ipcl_8(ip):
	ip = ip.replace("/8","")
	ip.strip()
	q = ip.split(".")
	liebiao = []
	for i in range(0,256):
		xxx = q[0]+"."+str(i)
		for x in range(0,256):
			qqq = xxx+"."+str(x)
			for f in range(0,256):
				fff = qqq+"."+str(f)
				liebiao.append(fff)
	return liebiao

def chjc_main(host):
	print("==========进入存活主机检测项==========")
	ip = input("请输入要检测的ip或ip段: ")
	xc = input("请输入线程[默认为10]: ")
	if ip:
		ip = ip
	else:
		ip = host

	if xc:
		xc = xc
	else:
		xc = 10



	if '/24' in ip:
		ips = ipcl_24(ip)
	elif '/16' in ip:
		ips = ipcl_16(ip)
	elif '/8' in ip:
		ips = ipcl_8(ip)
	else:
		ips = []
		ips.append(ip)
	ipq = zid(ips)

	threads = []

	for i in range(0,int(xc)):
		t = threading.Thread(target=saomiao,args=(ipq,))
		threads.append(t)
		t.start()
	for t in threads:
		t.join()
	print("==========检测完成==========")



