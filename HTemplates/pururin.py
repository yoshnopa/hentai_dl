import json, re

def suited(adress):
	return 'pururin.io' in adress

def resolve(adress, browser):
	Input = adress.replace('pururin.io/gallery/', '').replace('/', '')
	cut=[(i,c) for i,c in enumerate(Input) if not c.isdigit()][0][0]
	Input=Input[:cut]
	
	browser.open('http://pururin.io/gallery/' + Input + '/')
	header = browser.find(class_='info')
	name = header.find(class_="title").text.split('/')[0].strip()
	
	links = [[]]
	#Get the read page and extract the javascript value containing all image links
	browser.open('http://pururin.io/read/' + Input + '/01/')
	jscript=browser.find_all("script")[-2].text
	jvar = re.search('var chapters = (.*?);', jscript).group(0)
	jsonned=json.loads(jvar[:-1].replace("var chapters = ", ""))
	#and read them into the images variable
	for key, value in sorted(jsonned.items(), key=lambda x: int(x[0])):
		links[0].append(value['image'])

	print(links)
	return [name, links]
		