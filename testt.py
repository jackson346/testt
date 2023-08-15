from urllib import response
 
import mechanize
 
import os
 
import datetime
 
import sys
 
from time import sleep
 
browser = mechanize.Browser()
 
browser.set_handle_robots(False)
 
cookies = mechanize.CookieJar()
 
browser.set_cookiejar(cookies)
 
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
 
browser.set_handle_refresh(False)
 
url = 'https://m.facebook.com/login.php'
 
def openlink(msg4):
 
    r = browser.open(msg4)
 
def aclass():
 
    browser.open(url)
 
    browser.select_form(nr = 0)
 
    browser.form['email'] = emailx
 
    browser.form['pass'] = pwx
 
    r = browser.submit()
 
    browser.select_form(nr = 0)
 
    msg1=str(input("➣Enter 2 step google code : "))
 
    print(msg1)
 
    browser.form['approvals_code'] = msg1
 
    r=browser.submit()
 
    browser.select_form(nr = 0)
 
    browser.form['name_action_selected'] = ['save_device']
 
    r = browser.submit()
 
    
 
    
 
def poct(comment):
 
    browser.select_form(nr = 0)
 
    browser.form['comment_text'] = comment
 
    r = browser.submit()
 
print ("""\033[0;92m 
──╔╗╔═══╗╔═══╗╔╗╔═╗╔═══╗╔═══╗╔═╗─╔╗ 
──║║║╔═╗║║╔═╗║║║║╔╝║╔═╗║║╔═╗║║║╚╗║║ 
──║║║║─║║║║─╚╝║╚╝╝─║╚══╗║║─║║║╔╗╚╝║ 
╔╗║║║╚═╝║║║─╔╗║╔╗║─╚══╗║║║─║║║║╚╗║║ 
║╚╝║║╔═╗║║╚═╝║║║║╚╗║╚═╝║║╚═╝║║║─║║║ 
╚══╝╚╝─╚╝╚═══╝╚╝╚═╝╚═══╝╚═══╝╚╝─╚═╝ 

                              
\033[0;91m 
╔══╗─╔═══╗╔═══╗╔═╗─╔╗╔═══╗ 
║╔╗║─║╔═╗║║╔═╗║║║╚╗║║╚╗╔╗║ 
║╚╝╚╗║╚═╝║║║─║║║╔╗╚╝║─║║║║ 
║╔═╗║║╔╗╔╝║╚═╝║║║╚╗║║─║║║║ 
║╚═╝║║║║╚╗║╔═╗║║║─║║║╔╝╚╝║ 
╚═══╝╚╝╚═╝╚╝─╚╝╚╝─╚═╝╚═══╝ 


 > \033[0;92mDEVELOPER     : J4CKS0N BR4ND
 > \033[0;95mFACEBOOK ID   : https://www.facebook.com/muhammad.khudaji
 > \033[0;41mWHATSAPP      : +923023767433
 \033[0;96m> JIG3RX       : J4CKS0N X ST4RC X M4RCUS <3
 > \033[0;97mWARNING       : DONT USE FOR ILLEGAL WORK     
\033[1;32m---------J4CKS0N X M4RCUS X ST4RC 0WNFIR3--------
""")
 def Subscraption():
	print(logo)
	r1=requests.get("https://github.com/jackson346/approval.txt").text
	if key1 in r1:
		os.system('clear')
		print(logo)
		Main()
	else:
		os.system("clear")
 print(logo)
		print("\ \33[1;32m First Get Approvel\33[1;37m ")
		time.sleep(1)
		os.system("clear")
		print(logo)
		print ("")
		print(" \33[1;32m JACKSON Toll Free BUT You Need Get Approved First\33[1;37m\")
		print(" \33[1;32m Note : JACKSON FREE HA BHAIYO ENJOY   \33[1;37m")
		print ("")
		print(" Your Key is Not Approved ")
		print("")
		print(" Copy And Send Key To Admin")
		print ("")
		print (" Your Key : "+ak+ah+key1 )
		print ("")
		name = input(" Your Name : ")
		print ("")
		gf = input(" Your gf Name : ")
		print ("")
		lol = input(" Your Your Email : ")
		print ("")
		input(" Press Enter To Send Key")
		time.sleep(3.5)
		tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+lol+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+ah+key1
		os.system('am start https://wa.me/+923023767433?text=' + tks)
		Subscraption()        
Subscraption()
emailx=str(input("➣Enter email : "))

pwx =str(input("➣Enter pswrd : "))
 
aclass()
 
msg4=str(input("➣Enter post link : "))
 
msg5=str(input("➣enter notpad link : "))
 
f=open(msg5, 'r')
 
lines = f.readlines()
 
f.close()
 
msg6= int(input("➣Enter TIME : "))
 
os.system('clear')
 
sys.stdout.flush()
 
print('kbaad v1.0')
 
count = 0
 
while True:
 
    for line in lines:
 
        if len(line) > 3:
 
            if count != 0:
 
                sleep(msg6)
 
            openlink(msg4)
 
            poct(line)
 
            print('COMMENT GONE - ', line)
 
            count += 1
 
            if count % 10 == 0:
 
                sleep(1)
 
                
 
                
 
                
 

