def suited(adress):
	return "doujins.com" in adress

def resolve(adress, browser):
	browser.open("https://" + adress)
	name=browser.find(class_="folder-title").findAll("a")[-1].text

	links=[[]]
	images = browser.find(id="image-container").findAll("img")
	for image in images:
		links[0].append(image["data-file"])
	return(name, links)
