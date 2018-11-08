import json   
import urllib.request, urllib.parse, urllib.error

place_name = input("Enter location: ")
url = "http://python-data.dr-chuck.net/geojson?sensor=false&"
address_param = urllib.parse.urlencode({'address': place_name})
target = url + address_param

print("Retrieving {0}".format(target))
connection = urllib.request.urlopen(target)
raw_data = connection.read()
print("Retrieved {0} characters".format(len(raw_data)))
parsed_data = json.loads(raw_data)

print("Place id:", parsed_data["results"][0]["place_id"])


# Welcome Kaitlyn Bartley from Using Python to Access Web Data

# Calling a JSON API

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
# API End Points

# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

# http://py4e-data.dr-chuck.net/geojson?
# This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.
# To call the API, you need to provide address that you are requesting as the address= parameter that is properly URL encoded using the urllib.urlencode() fuction as shown in http://www.py4e.com/code3/geojson.py

# Test Data / Sample Execution

# You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJJ8oO7_B_bIcR2AlhC8nKlok".

# $ python3 solution.py
# Enter location: South Federal University
# Retrieving http://...
# Retrieved 2101 characters
# Place id ChIJJ8oO7_B_bIcR2AlhC8nKlok
# Turn In

# Please run your program to find the place_id for this location:

# University of Texas at Austin
# Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The first seven characters of the place_id are "ChIJZe2 ..."
# Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work with the Google API - but the place_id may not match for this assignment.
