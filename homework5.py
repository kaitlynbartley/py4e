# this code follows links in html using BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
count = int(input('Enter count - '))
position = int(input('Enter position - '))

def parseHtml(url, position):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')

	# Retrieve anchor tags in a for-loop
	tags = soup('a')
	i = 0
	for tag in tags:
		i += 1
		if i == position:
			return tag.get('href', None)

current_num = 0
while current_num < count:
	print('retrieving:', url)
	url = parseHtml(url, position)
	current_num += 1
print('retrieving:', url)