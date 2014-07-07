#!/usr/bin/env python3
from lxml import etree
import urllib.request
import urllib
import os

url = "http://gewiss.uni-leipzig.de:8282/"
url_all = "http://gewiss.uni-leipzig.de:8282/gewiss/webresources/ListSubcorpora"
url_corp = "http://gewiss.uni-leipzig.de:8282/gewiss/webresources/ListCommunications?cor-name="
url_trans = "http://gewiss.uni-leipzig.de:8282/gewiss/webresources/ViewTranscript?tra-name="

username = ''
password = ''
	

def getTranscript(link, dir_output, file_name):
	if not os.path.exists(dir_output):
	    os.makedirs(dir_output)
	
	password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
	password_mgr.add_password(None, url, username, password)
	handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
	opener = urllib.request.build_opener(handler)
	opener.open(link)
	urllib.request.install_opener(opener)
	urllib.request.urlretrieve(link, dir_output + file_name)
	print(link)
			
def getSite(link):
	try:			
		site = etree.parse(link, parser = etree.HTMLParser())
		return site			
	except OSError:
		return None	
				

all_corp = getSite(url_all)
for corp_name in all_corp.iter('data'):
	corp_addr = getSite(url_corp + corp_name.text)
	if corp_addr:
		for transcript in corp_addr.iter('data'):
			dir_output = "gewiss/" + corp_name.text +"/"
			file_name = transcript.text + ".xml"
			getTranscript(url_trans + transcript.text, dir_output, file_name) 
print("finish")
		 	
