#!/usr/bin/python

import urllib
import urllib2
import re
from cookielib import CookieJar
import sys

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))


def main():
	_, username, password = sys.argv
	fd1 = opener.open("http://www.google.com")
	metaLine = [l for l in fd1 if '<META HTTP-EQUIV="Refresh"' in l][0]
	if "login.tikona.in" not in metaLine:
		return
	url1 = metaLine[metaLine.index('URL=')+4:-3]
	print "Step #1: Done"
	fd2 = opener.open(url1)
	#print fd2.read()
	url2 = opener.open(urllib2.Request("https://login.tikona.in/userportal/" + 
			"login.do?requesturi=http%3A%2F%2Fwww.google.com%2F&act=null", ""))
	print "Step #2: Done"
	#print url2.read()
	url2 = opener.open(urllib2.Request(
			"https://login.tikona.in/userportal/newlogin.do?phone=0",
			urllib.urlencode({
				"type": 2,
				"username": username,
				"password": password,
				"rememberme": "on",
				"act": "null"
			})
	))
	print "Step #3: Done"
	resp = url2.read()
	if "You are logged in" in resp:
		print "Logged in! :-)"
	else:
		print "Something went wrong.. May be authentication failure?"
	
if __name__ == '__main__':
	main()
	
	