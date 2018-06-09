import re, json

def suited(adress):
	return "bato.to" in adress

def resolve(adress, browser):
	browser.open("https://" + adress)
	name=browser.find(class_="item-title").text.replace("\n", "")

	links=[]
	chapters = browser.find(class_="chapter-list").findAll(class_="chapt")[::-1]
	c=0
	for chapter in chapters:
		c=c+1
		links.append([])
		browser.open("https://bato.to" + chapter["href"])
		#Get image list out of the javascript
		jscript=browser.find_all("script")[-5].text
		jvar = re.search('var images = (.*?);', jscript).group(0)
		jsonned=json.loads(jvar[:-1].replace("var images = ", ""))
		#and read them into the images variable
		for key, value in sorted(jsonned.items(), key=lambda x: int(x[0])):
			links[c-1].append(value)
	return [name, links]
