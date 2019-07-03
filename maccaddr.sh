#!/bin/bash

#Reading User input for Mac address
read -p "Enter your MAC Address: " macaddr
#echo "you have entered $macaddr"

#Querying https://api.macaddress.io/
#We can use simple curl or wget calls
RESULT=$(curl -XGET --silent "https://api.macaddress.io/v1?apiKey=at_0GqnvodFXhE5KY3ni1XNlqztaFzYv&output=vendor&search="$macaddr"")
#RESULT="`wget -qO- https://api.macaddress.io/v1?apiKey=at_0GqnvodFXhE5KY3ni1XNlqztaFzYv&output=vendor&search="$macaddr"`"
echo "MAC Address - Vendor: $macaddr - $RESULT"
