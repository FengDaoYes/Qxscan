import socket
import requests
import re

def yumings(xinxi):
	lb = xinxi.split(".")
	yuming = lb[-2]+"."+lb[-1]
	return yuming


def cx(host):
	hosts=yumings(host)
	header = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'
		}
	hosts = hosts.strip()
	url = "https://site.ip138.com/"+hosts+"/whois.htm"
	x = requests.get(url,headers=header)
	
	txt = x.text
	
	liebiao = re.findall("<p>(.*?)</p>",txt)
	try:
		liebiao.pop()
		liebiao.pop()
		print("whois查询： ")
		for i in liebiao:
			print(i)
	except:
		print("未查询到信息..")

def whois_main(host):
	print("==进入whois查询项==\n")
	yuming = input("==>请输入要查询的域名(若当前域名则直接回车)： ")
	if yuming:
		cx(yuming)
	else:
		cx(host)
	
	print("==查询完成==\n")
