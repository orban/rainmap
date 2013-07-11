#!/usr/bin/env python

from math import cos, sin, atan2, pi, sqrt
from collections import namedtuple
import urllib2
import json


Point = namedtuple('Point', 'lat lon')
	

def center_geolocation(geolocations):
	"""
	Provide a relatively accurate center lat, lon returned as a list pair,
	givena list of list pairs.
	ex: in: geolocations = ((lat1,lon1), (lat2,lon2),)
		out: (center_lat, center_lon)
	"""
	x = 0
	y = 0
	z = 0

	for lat, lon in geolocations:
		lat = float(lat) * pi/180
		lon = float(lon) * pi/180
		x += cos(lat) * cos(lon)
		y += cos(lat) * sin(lon)
		z += sin(lat)

	x = float(x / len(geolocations))
	y = float(y / len(geolocations))
	z = float(z / len(geolocations))

	return Point(atan2(z, sqrt(x * x + y * y)) * 180/pi, atan2(y, x) * 180/pi)
	
def main():
	response = urllib2.urlopen(
		'http://s3.amazonaws.com/static.m2i.stamen/latest_images.json')
	data = json.load(response)
	
	for record in data['items']:
		coords = record['coords'].split(":")
		if len(coords) > 2:
			pt1 = Point(coords[0], coords[1])
			pt2 = Point(coords[2], coords[3])
			print pt1, pt2, center_geolocation([pt1, pt2])
		
if __name__ == '__main__':
	main()