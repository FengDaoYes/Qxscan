import optparse
import socket
import queue
import threading

duankou = {"20":"ftp-data","21":"ftp服务[允许匿名的上传、下载、爆破和嗅探操作]","22":"ssh远程连接[爆破、SSH隧道及内网代理转发、文件传输、OpenSSL漏洞]","23":"telnet远程连接[爆破、嗅探、弱口令]","25":"smtp邮件服务[用户名枚举、邮件伪造]",
			"53":"dns域名系统[允许区域传送、DNS劫持、缓存投毒、欺骗]","80":"http协议","81":"hosts2-ns","135":"msrpc","8080":"http协议","137":"Samba服务[爆破、未授权访问、远程代码执行漏洞]",
			"139":"netbios-ssn服务[爆破、未授权访问、远程代码执行]","443":"https协议","445":"smb协议","1723":"pptp服务",
			"3306":"mysql数据库[注入、提权、爆破]","3389":"rdp远程桌面连接[shift后门、爆破]","1433":"mssql数据库[注入、提权、SA弱口令、爆破]","888":"宝塔面板","8888":"宝塔面板",
			"69":"TFTP服务[允许匿名的上传、下载、爆破和嗅探操作]","2049":"NFS服务[配置不当、未授权访问]","389":"LDAP目录访问协议[注入、允许匿名访问、弱口令]","5900":"VNC[弱口令爆破、拒绝服务攻击、权限提升]",
			'5632':'PcAnywhere服务[抓取密码、代码执行、拒绝服务攻击、提权]','7001':'WebLogic控制台[Java反序列化、弱口令]','7002':'WebLogic控制台[Java反序列化、弱口令]','8089':'http','9090':'WebSphere控制台[java反序列化、弱口令]',
			'4848':'GlassFish控制台[弱口令]','1352':'Lotus Domino邮件服务[弱口令、信息泄露、爆破]','10000':'webmin控制台[弱口令]',
			'1521':'Oracle数据库[TNS爆破、注入、反弹shell]','5432':'PostgreSQL数据库[爆破、注入、弱口令]','27017':'MongoDB数据库[爆破、未授权访问]',
			'27018':'MongoDB数据库[爆破、未授权访问]','6379':'Redis数据库[可尝试未授权访问、弱口令爆破]','5000':'Sysbase/DB2数据库[爆破、注入]',
			'110':'POP3协议[爆破、嗅探]','143':'IMAP协议[爆破]','67':'DHCP服务[劫持、欺骗]','68':'DHCP未授权访问服务[劫持、欺骗]','161':'SNMP协议[爆破、收集目标内网信息]',
			'2181':'ZooKeeper服务[未授权访问]','8069':'Zabbix服务[远程执行、SQL注入]','9200':'Elasticsearch服务[远程执行、未授权访问]',
			'9300':'Elasticsearch服务[远程执行]','11211':'Memcached服务[未授权访问]','512':'Linux rexec服务[爆破、远程登录]',
			'513':'Linux rexec服务[爆破、远程登录]','514':'Linux rexec服务[爆破、远程登录]','873':'rsync服务[匿名访问、文件上传]','3690':'SVN服务[SVN泄露、未授权访问]',
			'50000':'SAP Management[远程执行]',"9080":"Websphere[爆破、弱口令、任意文件泄漏、Java反序列化]","9081":"Websphere[爆破、弱口令、任意文件泄漏、Java反序列化]","9090":"Websphere[爆破、弱口令、任意文件泄漏、Java反序列化]",
			'5984':'CouchDB[未授权访问]','2375':'Docker Remote API[未授权访问]','8161':'ActiveMQ[未授权访问]','5985':'WinRM[弱口令, 远程执行, 后门植入]',
			'1099':'JAVA RMI[反序列化利用]','8500':"ColdFusion[文件读取漏洞]"}


def qqq(zidian):
	words = queue.Queue()
	for i in zidian:
		words.put(i)
	return words

def dksm(host,port):
	try:
		socket.setdefaulttimeout(2)
		lianjie = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		lianjie.connect((host,int(port)))
		return "1"
		lianjie.close()
		
	except:
		return "0"
	
	
def duankous(port):
	ports = port.split("-")
	portss = [list(range(int(ports[0]),int(ports[1])+1))]
	return portss
	
def ipy(host):
	l = host.find("/")
	s = host[0:l]
	q = s.split(".")
	liebiao = []
	for i in range(0,256):
		f = q[0]+"."+q[1]+"."+q[2]+"."+str(i)
		liebiao.append(f)
		
	return liebiao





def csxinxi():
	global port
	global xiancheng
	global ports
	global host
	
	port = input("[-]请输入要扫描的端口： ")

	xiancheng = input("[-]请输入线程： ")
	
	host = input("[-]请输入域名或ip: ")
	if port:
		if "-" in port:
			ports = duankous(port)
		else:
			ports = False
	else:
		port = False
		ports = False





	

def dksm_main():
	print("==进入端口扫描项==\n")
	
	csxinxi()
	if "/" in host:
		hosts = ipy(host)
	else:
		hosts = False
	threads = []
	if hosts:
		if ports:
			for ip in hosts:
				t=threading.Thread(target=main_a,args=(ip,ports,))
				threads.append(t)
				t.start()
		if port and (not ports):
			for ip in hosts:
				t=threading.Thread(target=main_b,args=(ip,port,))
				threads.append(t)
				t.start()
		if (not port) and (not ports):
			for ip in hosts:
				t=threading.Thread(target=main_d,args=(ip,duankou,))
				threads.append(t)
				t.start()
	if host and (not hosts):
		if ports:
			for dks in ports:
				dkq = qqq(dks)
				if xiancheng:
					for i in range(0,int(xiancheng)):
						t=threading.Thread(target=main_c,args=(host,dkq,))
						threads.append(t)
						t.start()
				else:
					t=threading.Thread(target=main_c,args=(host,dkq,))
					threads.append(t)
					t.start()
		if port and (not ports):
			t=threading.Thread(target=main_b,args=(host,port,))
			threads.append(t)
			t.start()
		if (not port) and (not ports):
			dks = []
			for p,fuwu in duankou.items():
				dks.append(p)
			dkp = qqq(dks)
			if xiancheng:
				for i in range(0,int(xiancheng)):
					t=threading.Thread(target=main_e,args=(host,dkp,duankou,))
					threads.append(t)
					t.start()
			else:
				t=threading.Thread(target=main_e,args=(host,dkp,duankou,))
				threads.append(t)
				t.start()
	for t in threads:
		t.join()
	print("==扫描完成==\n")

		
		
def main_a(ip,dks):
	for dk in dks:
		for d in dk:
			panduan = dksm(ip,d)
			if panduan == "1":
				print("[+]"+ip+":"+str(d))
					
def main_b(ip,dk):
	panduan = dksm(ip,dk)
	if panduan == "1":
		print("[+]"+ip+":"+str(dk))

def main_c(ip,dkq):
	while not dkq.empty():
		dk = dkq.get()
		dk_list =[]
		dk_list.append(dk)
		for d in dk_list:
			panduan = dksm(ip,d)
			if panduan == "1":
				print("[+]"+ip+":"+str(d))
		
	
def main_d(ip,duankou):
	for port,fuwu in duankou.items():
		panduan = dksm(ip,port)
		if panduan == "1":
			print("[+]"+ip+":"+str(port)+"\t"+fuwu)

def main_e(ip,dkp,zidian):
	while not dkp.empty():
		dk = dkp.get()
		dk_list =[]
		dk_list.append(dk)
		for d in dk_list:
			panduan = dksm(ip,d)
			if panduan == "1":
				print("[+]"+ip+":"+str(d)+"\t"+zidian[str(d)])
		
if __name__ == '__main__':
	dksm_main()

