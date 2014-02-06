#! /usr/bin/env python

import json
from urllib import quote_plus
from urllib2 import urlopen

APITOKEN = 'http://api.twitch.tv/api/channels/%s/access_token'
USHERPLAYLIST = 'http://usher.twitch.tv/api/channel/hls/%s.m3u8?token=%s&sig=%s'

def grab(channel):
	channel = channel.lower()

	tokenurl = APITOKEN % quote_plus(channel)
	tokenjson = urlopen(tokenurl).read()
	tokenarray = json.loads(tokenjson)
	token = tokenarray['token']
	sig = tokenarray['sig']

	playlisturl = USHERPLAYLIST % (quote_plus(channel), quote_plus(token), quote_plus(sig))
	playlist = urlopen(playlisturl).read().split("\n")

	for line in playlist:
		if line.startswith("http://"):
			return line
	return None

from sys import argv, exit

if __name__ == "__main__":
	if len(argv) < 2:
		print "Usage: %s channel" % argv[0]
		exit(2)
	channel = argv[1]
	print grab(channel)
