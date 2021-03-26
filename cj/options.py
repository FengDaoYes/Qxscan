import requests

def ffhq(url):
	pd = input("请问是否为https？[y/n]: ")
	if pd =="y":
		ht="https://"
	else:
		ht="http://"
	ym = input("请输入域名若为当前域名请输[y]: ")
	
	if ym == "y":
		urls=ht+url
	else:
		urls=ht+ym

	txt = requests.options(urls)

	zd = txt.headers
	if 'Access-Control-Allow-Methods' in zd.values():
		print("开启的http方法："+zd['Access-Control-Allow-Methods'])
	else:
		print("无法查看！！")
		

def options_main(url):
	print("==进入http方法查询项==\n")
	ffhq(url)
	print("==查询结束==\n")
