#original code for using beautiful soup
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# url = input('Enter - ')
# html = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm').read()
# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the anochor tags
# tags = soup('a')
# for tag in tags:
# 	print(tag.get('href', None))

#worked example using ssl
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
	print(tag.get('href', None))