# -*- coding: utf-8 -*-
import cj.dksm
import cj.cdsm
import cj.webbp
import cj.whois
import cj.ipjx
import cj.zymcx
import cj.zymbp
import cj.options
import cj.dzcx
import cj.zwsb
import cj.chjc
import cj.webjc
import cj.urlcj

def xiugai():
	#修改ip与端口
	global host
	global port
	host = input("请输入目标ip或域名： ")
	port = input("请输入目标端口: ")
	if "http://" in host:
		host = host.replace("http://","")
	if "https://" in host:
		host = host.replace("https://","")
	if "/" in host:
		host = host.replace("/","")
		

def biaoti():
	print("################################################################################################")
	print("""  ___                            
 / _ \\ __  _____  ___ __ _ _ __  	########################################################
| | | |\\ \\/ / __|/ __/ _` | '_ \\ 	###############[+]Qxscan扫描器[+]  v1.7#################
| |_| | >  <\\__ \\ (_| (_| | | | |	###############====BY:F_Dao||====###########
 \\__\\_\\/_/\\_\\___/\\___\\__,_|_| |_|       ########################################################
                                 """)
	xinxi = "\t\t\tPS：-本工具仅供测试 违法后果自负-"
	print(xinxi)
	print("################################################################################################")
def kaitou(host,port):
	dizhi = cj.dzcx.dzcx_main(host)
	#打印绑定ip与端口以及选项
	xinxi = "HOST： "+host+" PORT: "+port+"\n"
	xinxi +="物理地址： "+dizhi+"\n"
	xinxi += "选项： \n"
	xinxi += "[0]-更改ip与端口-\n"
	xinxi += "[1]-端口扫描-\n"
	xinxi += "[2]-c段扫描-\n"
	xinxi += "[3]-web爆破-\n"
	xinxi += "[4]-whois查询-\n"
	xinxi += "[5]-ip解析-\n"
	xinxi += "[6]-子域名查询-\n"
	xinxi += "[7]-子域名爆破-\n"
	xinxi += "[8]-http方法查询-\n"
	xinxi += "[9]-web指纹识别-\n"
	xinxi += "[10]-存活检测-\n"
	xinxi += "[11]-扫描web资产-\n"
	xinxi += "[12]-百度url采集-\n"
	xinxi += "\n[exit]-退出-"
	
	print(xinxi)
	global xuanxiang
	xuanxiang = input("\n请输入操作编号：")
	
def main():
	#程序入口
	biaoti()
	xiugai()
	while True:
		print("=======================================")
		kaitou(host,port)
		global xuanxiang
		if xuanxiang == "1":
			cj.dksm.dksm_main()
		if xuanxiang == "exit":
			exit(0)
		if xuanxiang == "0":
			xiugai()
		if xuanxiang == "2":
			cj.cdsm.cdsm_main(host)
		if xuanxiang == "3":
			cj.webbp.webbp_main(host,port)
		if xuanxiang == "4":
			cj.whois.whois_main(host)
		if xuanxiang == "5":
			cj.ipjx.ipjx_main(host)
		if xuanxiang == "6":
			cj.zymcx.zymcx_main(host)
		if xuanxiang == "7":
			cj.zymbp.zymbp_main(host)
		if xuanxiang == "8":
			cj.options.options_main(host)
		if xuanxiang == "9":
			cj.zwsb.zwsb_main(host)
		if xuanxiang == "10":
			cj.chjc.chjc_main(host)
		if xuanxiang == "11":
			cj.webjc.webjc_main()
		if xuanxiang == "12":
			cj.urlcj.urlcj_main()

if __name__ == "__main__":
	main()
