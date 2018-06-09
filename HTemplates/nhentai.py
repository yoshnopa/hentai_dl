import time

def suited(adress):
	return "nhentai.net" in adress

def resolve(adress, browser):
	Input="https://" + adress
	browser.open(Input)
	name = browser.find(id="info").find("h1").text

	links = [[]]
	imgNum = 1
	while True:
		browser.open(Input + "/" + str(imgNum))
		if browser.response.status_code == 404:
			break
		links[0].append(browser.find(id="image-container").find("img")["src"])
		time.sleep(2)
		imgNum = imgNum +1

	return [name, links]
