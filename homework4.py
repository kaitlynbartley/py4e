# # To run this, you can install BeautifulSoup
# # https://pypi.python.org/pypi/beautifulsoup4

# # Or download the file
# # http://www.py4e.com/code3/bs4.zip
# # and unzip it in the same directory as this file


# # this code scrapes and sums numbers from HTML page using Beautiful Soup 
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
numbers = []

# Retrieve all of the span tags
spans = soup('span')
for span in spans:
	numbers.append(int(span.string))
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
print(sum(numbers))
    #print('Attrs:', tag.attrs)




