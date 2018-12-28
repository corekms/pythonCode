import requests
import re

def findAllLinks(urlStr):
	# connect to the url
	website = requests.get(urlStr)

	# read HTML
	html = website.text

	# use re.findall to grab all the links
	links = re.findall('"((http|ftp)s?://.*?)"', html)

	# output links
	for link in links:
		yield link

if __name__ == "__main__":
	for link in findAllLinks("startUrl goes here"):
		print(link)
