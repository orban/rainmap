import urllib2
import json

response = urllib2.urlopen('http://s3.amazonaws.com/static.m2i.stamen/latest_images.json')
data = json.load(response)

for datum in data['items']:
	print datum['coords']