#!/usr/bin/python2.7

import requests
import sys

#Asing for MAC address input
macaddr = raw_input("Please enter your MAC address:")
print "Your MAC address is: ", macaddr
type(macaddr)

#API Call

# api-endpoint
URL = "https://api.macaddress.io/v1?apiKey=at_0GqnvodFXhE5KY3ni1XNlqztaFzYv&output=json&"


# defining a params dict for the parameters to be sent to the API
PARAMS = {'search':macaddr}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()

companyName=data['vendorDetails']['companyName']

# printing the output
print("vendorDetails:%s\ncompanyName:%s"
      %(macaddr, companyName))

