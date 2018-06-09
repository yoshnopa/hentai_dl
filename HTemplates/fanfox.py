def suited(adress):
	return "fanfox.net" in adress

def resolve(adress, browser):
	browser.open("http://" + adress)
	name = browser.find(id="title").find("h1").text

	links=[]
	chapters=browser.find(class_="chlist").findAll(class_="tips")[::-1]
	c=0
	for chapter in chapters:
		c=c+1
		links.append([])
		browser.open("http:" + chapter["href"])
		imagelinks=browser.find(class_="m").findAll("option")[:-1]
		for imagelink in imagelinks:
			browser.open("http:" + chapter["href"].replace("1.html", imagelink.text) + ".html")
			links[c-1].append(browser.find(id="image")["src"])
	return [name, links]
