import time

def suited(adress):
	return "hbrowse.com" in adress

def resolve(adress, browser):
	Input="http://" + adress
	browser.open(Input)
	name = browser.find(class_="listTable").find("tr").find(class_="listLong").text

	links=[]
	raw = browser.find(id="main").findAll(class_="listTable")[2].findAll(class_="listMiddle")
	chapters = []
	for data in raw:
		chapters.append(data.find("a")['href'])
	c=0
	for chapter in chapters:
		c=c+1
		links.append([])
		browser.open("http://www.hbrowse.com" + chapter)
		imglinks = browser.find(id="jsPageList").findAll("a")[1:]
		for imglink in imglinks:
			img= browser.find(id="mangaImage")["src"]
			links[c-1].append("http://www.hbrowse.com" + img)
			time.sleep(2)
			browser.open("http://www.hbrowse.com" + imglink["href"])
		img= browser.find(id="mangaImage")["src"]
		links[c-1].append("http://www.hbrowse.com" + img)
	return [name, links]
