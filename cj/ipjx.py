import requests
import re

def dqcx(host):
	header = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'
		}
	url = "https://site.ip138.com/domain/read.do?domain="+host+"&time=1592209224418"
	
	x = requests.get(url,headers=header)
	
	txt = x.text
	#print(txt)
	liebiao = re.findall("\d+\.\d+\.\d+\.\d+",txt)
	print("当前解析ip:")
	for i in liebiao:
		print("\t"+i)

def lscx(host):
	header = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'
		}
	url = "https://site.ip138.com/"+host+"/"
	
	x = requests.get(url,headers=header)
	txt = x.text
	
	liebiao = re.findall("target=\"_blank\">\d+\.\d+\.\d+\.\d+</a>\s</p>",txt)
	print("历史解析ip：")
	for i in liebiao:
		
		i = i.replace("target=\"_blank\">","")
		i = i.replace("</a>","")
		i = i.replace("</p>","")
		i = i.strip()
		print("\t"+i)

def ipjx_main(host):
	print("==进入ip解析项==\n")
	yuming = input("==>请输入域名(若当前域名直接回车): ")
	
	if yuming:
		dqcx(yuming)
		lscx(yuming)
	else:
		dqcx(host)
		lscx(host)
	print("=======查询结束=======\n")
	
	
	
	
	
	
	
	
