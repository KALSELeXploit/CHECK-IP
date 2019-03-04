# baru belajar python
import json, sys
import requests, time, os
os.system("clear")
def restart_progr():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir= os.getcwd()
try:
   from termcolor import colored
except Noo:
   print ("BEELOM DI INSTALL")
def data():
    url = 'https://api.myip.com'
    y = json.loads(requests.get(url).text)
    o =y["ip"]
    os =y["cc"]
    country=y['country']
    print (o)
    print (os)
    print (country)

if __name__ == "__main__":
  print(colored('''
====================================
         CHECK IP
    Create By : Widhisec
    Team : KalselXploit
====================================
''','green'))
try:
   data()
except KeyError:
      exit("\033[1;31merorr")
try:
  ndasmu = input("Lagi Gan (y/n) => ")
except KeyboardInterrupt:
	print("[!] KeyboardInterrupt: Exiting...\n")
	time.sleep(1)
	sys.exit(1)
if ndasmu == "y":
  restart_progr()
if ndasmu == "n":
   print ("Byee")
   sys.exit(2)
