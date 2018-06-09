def suited(adress):
	return '8muses.com' in adress

def resolve(adress, browser):

	def getLinks(Input):
		linkout=[]
		pageNum=1
		while True:
			browser.open("https://www.8muses.com/comics/picture/" + Input + "/" + str(pageNum))
			imgid = browser.find(id="imageName")["value"]
			#If the imagename is empty, this comic is at its end; break loop
			if imgid == ".jpg" or not imgid:
				break
			domain =  browser.find(id="imageHost")["value"]
			if not domain:
				domain = "https://8muses.com"
			#The domain does not provide the URL in a simple way, but its scattered. The values are found by IDs, so here they are remerged
			linkout.append(domain + "/image/fl/" + imgid)
			pageNum = pageNum + 1
		return linkout
			
			

	Input = adress.split("album/")[1]
	#Maybe correct this, extraction from url is not exactly perfect...
	name = list(filter(None, Input.split("/")))[-1]
	
	links=[]
	browser.open("https://www.8muses.com/comics/album/" + Input + "/")
	#We have to check whether this comic has issues, if so, multiple chapters have to be returned	
	chapters=browser.find_all("span", {"class" : "title-text"})
	if chapters:
		for chapter in range(len(chapters)):
			Input=chapters[chapter].parent.parent["href"].split("album/")[1]
			links.append(getLinks(Input))
	else:
		links.append(getLinks(Input))

	return [name, links]