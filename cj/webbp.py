import os
import requests
import threading
import queue
import time


def lujin():
	x = os.getcwd()
	b = x+"/zd/blpj/"

	q = os.listdir(b)
	for i in q:
		i = i.replace('.txt','')
		print(i)

def zid(wenjian):
		
	words = queue.Queue()
	
	try:
		with open(wenjian,encoding='gbk') as zd:
			for i in zd:
				words.put(i)
	except:
		with open(wenjian,encoding='utf-8') as zd:
			for i in zd:
				words.put(i)
				
	return words

def qqq(zidian,url):
	jishu = 0
	while True:
		if zidian.empty():
			return
		else:
			i = zidian.get()
			header = {
    			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:76.0) Gecko/20100101 Firefox/76.0',
    			'Accept': 'application/json, text/plain, */*',
    			'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    			'Accept-Encoding': 'gzip, deflate',
    			'Content-Type': 'application/x-www-form-urlencoded',
    			'Connection': 'close'}
			i = i.replace("%0a","")
			i = i.replace("%0A","")
			i = i.replace("\n","")
			i = i.replace("\r","")
			i.strip()
			urls = url+i
			try:
				requests.adapters.DEFAULT_RETRIES = 5
				s = requests.session()
				r = s.head(urls,timeout=5,headers=header)
				if r.status_code != 404 and r.status_code != 405 and r.status_code != 400:
					print("\n[+]"+urls+"\nResponse code: ["+str(r.status_code)+"]")
				s.close()
			except:
				jishu+=1
				print("错误")
				if jishu > 10:
					exit()
				pass
def zidian():
	global lujins
	wenjian = input("\n==>请输入需要的字典文件: ")
	wenjian = wenjian.strip()
	lujins = "./zd/blpj/"+wenjian+'.txt'


def webbp_main(host,port):
	threads = []
	print("==进入web路径爆破项==\n")
	pdssl = input("请问是否为https[y](否则直接回车): ")
	if pdssl == "y":
		url = "https://"+host+":"+port+"/"
	else:
		url = "http://"+host+":"+port+"/"
	xc = input("请输入线程数： ")
	if xc:
		xc = xc
	else:
		xc = '10'
	print("============================")
	lujin()
	zidian()
	while True:
		panduan=os.path.isfile(lujins)
		if panduan:
			x = zid(lujins)	
			for i in range(int(xc)):
				t = threading.Thread(target=qqq,args=(x,url,))
				threads.append(t)
				t.start()
			
			for t in threads:
				t.join()
			break
		else:
			print("文件不存在，请重新输入..")
			zidian()
	
	print("\n=======扫描完成=======\n")
