def suited(adress):
	return 'www.porncomix.info/' in adress

def resolve(adress, browser):
	Input=adress.replace('www.porncomix.info/', '').replace('/', '')
	browser.open('http://www.porncomix.info/' + Input + '/')
	name = browser.find(class_='post-title').text

	links=[[]]	
	#Gallery is now scanned for the items, all items have links. Those are stored in piclinks
	galleryitems = browser.find_all(class_='gallery-item')
	piclinks = []
	for item in galleryitems:
		piclinks.append(item.find('a')['href'])

	#Now all Links are obtained, they are visited and the picture source extracted
	for link in piclinks:
		browser.open(link)
		pic = browser.find(class_='attachment-image')
		links[0].append(pic.find('img')['src'])
	
	return [name, links]