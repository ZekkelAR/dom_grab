import requests as zek
import os
import sys
import re as jeki


regexIP = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
	25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
	25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
	25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
  
valid = []
def ammud(domen):
	i = 1
	while(True):
		print("[?] Sedang Grab domain : {}" .format(domen))
		print("[!] Grabb page ke 	: {}" .format(i))
		url = "https://www.sitelinks.info/domains/{}/{}/" .format(domen,i)
		try:
			req = zek.get(url, timeout=10).text
			#print(req)
			mengent = jeki.findall(r"<strong>(.*?)</strong>", req)
			print("[!] Total grab : {}" .format(len(mengent)))
			if (len(mengent)==0):
				print("[+] Completed in page {}" .format(i))
				log = "Domain {} completed in page {}" .format(domen, i)
				open("log.txt", 'a').write(log+'\n')
				break
			for monyet in mengent:
				if(jeki.search(regexIP, monyet)):
					pass
				else:
					#print(monyet)
					saved = 'grabbed_{}.txt' .format(domen)
					open(saved, 'a').write(monyet+'\n')
		except KeyboardInterrupt:
			exit()
		except:
			print("[+] Request timeout, lemot")
		i+=1



def grabber_domen():
	url = "https://www.sitelinks.info/domain_extensions/"
	n = zek.get(url).text
	ha = jeki.findall("<a href=\"https://www.sitelinks.info/domains/(.*?)/\"", n)
	for i in ha:
		print(i)


if __name__ == "__main__":
	print("""
 ██████╗ ██████╗  █████╗      ███████╗
██╔════╝ ██╔══██╗██╔══██╗     ╚══███╔╝
██║  ███╗██████╔╝███████║█████╗ ███╔╝ 
██║   ██║██╔══██╗██╔══██║╚════╝███╔╝  
╚██████╔╝██║  ██║██║  ██║     ███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚══════╝
 [x] Grabber Domain 
 [x] Created by Zekkel AR
 [x] Family Attack Cyber
                                      
	""")
	print("masukin domen ny make titik, contoh .com")
	asu = input("[?] Masukin list yg isinya domain : ")
	haha = open(asu, 'r').read().splitlines()
	for i in haha:
		ammud(i)
	#grabber_domen()