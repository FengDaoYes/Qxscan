import requests
import json
import base64


def b64bm(strs):
	try:
		strs = strs.encode('utf-8')
		strsb = base64.encodebytes(strs)
		strsb = strsb.decode('utf-8')
		return strsb
	except:
		return 0

def fofaapi_main():
	print("==进入fofa信息采集项==")
	emails = ""
	keys = ""
	if emails == "":
		email=input("请输入邮箱:").strip()
	else:
		email=emails
	if keys == "":
		key =input("请输入key:")
	else:
		key = keys
	grammar = input("请输入查询语法:").strip()
	qbase64 = b64bm(grammar)
	size = input("请输入获取数目[默认1000]:").strip()
	filename = input("输出文件名[否则回车]:").strip()
	if size:
		pass
	else:
		size="1000"

	url="https://fofa.so/api/v1/search/all?email="+email+"&key="+key+"&qbase64="+qbase64+"&size="+size
	requests.packages.urllib3.disable_warnings()
	s = requests.session()
	t = s.get(url,verify=False)
	j = json.loads(t.text)
	if j['error']:
		print("查询错误,请检查语法！")
		return 0
	print(">>>>>>>>>>正在输出结果>>>>>>>>>")
	if filename:
		file_path = ".\\file\\"+filename+".txt"
		with open(file_path,"w",encoding="utf-8") as txt:
			for i in j['results']:
				host = i[0]
				ip_port = i[1]+":"+i[2]
				txt.write(host+"\t"+ip_port+"\n")
				print("域:"+i[0])
				print("IP/端口:"+i[1]+":"+i[2])
				print("================================")
	else:
		for i in j['results']:
			print("域:"+i[0])
			print("IP/端口:"+i[1]+":"+i[2])
			print("================================")
	print(">>>>>>>>>>结果查询完成>>>>>>>>>")

if __name__ == "__main__":
	fofaapi_main()