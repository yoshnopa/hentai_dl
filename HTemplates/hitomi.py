import re

def suited(adress):
	return 'hitomi.la' in adress

def resolve(adress, browser):
	Input = adress.replace('hitomi.la/galleries/', '').replace('.html', '')
	browser.open('http://hitomi.la/galleries/' + Input + '.html')
	header = browser.parsed.title.string
	if re.match(".* by ", header):
		name = re.match(".* by ", header).group(0)[:-4]
	else:
		name = header

	links=[[]]
	#The Reader is the gallery of the Website
	browser.open('http://hitomi.la/reader/' + Input + '.html')
	#All Images are preloaded, thats why we can read them all out of the reader site
	pics = browser.find_all(class_='img-url')
	for pic in pics:
		links[0].append('http://a' + pic.string[3:])
	return [name, links]