# #since http is so common, we have a library that does all the socket work for us and makes web pages look like a file. 
# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# counts = dict()
# for line in fhand:
# 	print(line.decode().strip())

#to read a web page:
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
	print(line.decode().strip())