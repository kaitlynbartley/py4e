import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter location: ")
if len(url) < 1:
     url = "http://py4e-data.dr-chuck.net/comments_145161.xml"
print("Retrieving " + url)

xml = urllib.request.urlopen(url).read()
print("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)

counts =  tree.findall('.//count')
print("Count: " + str(len(counts)))

i = 0

for count in counts:
    i += int(count.text)
print("Sum:" + str(i))