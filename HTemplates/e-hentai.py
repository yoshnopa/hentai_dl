def suited(adress):
	return 'e-hentai.org' in adress

def resolve(adress, browser):
	Input="https://" + adress.split('?')[0]
	browser.open(Input)
	name = browser.find(id='gn').text

	links=[[]]
	#Get the last Number of Image Links (gets to browser bar, the last link, splits it behind the = to only get the number)
	maxNumber=browser.find(class_='ptt').find_all("td")[-2].a['href'].split("=")[-1]
	#When only one Page is there, there is no number behind the url, so set the number to 1
	try:
		int(maxNumber)
	except ValueError:
		maxNumber=0

	#First iteration is started through all pages to grab all image page Links	
	for i in range(int(maxNumber)+1):
		if i != 0:
			browser.open(Input + '/?p=' + str(i))
		imagelinks=browser.find(id='gdt').findAll('a')
		#After the Links are grabbed, they are iterated seperately
		for link in imagelinks:
			browser.open(link['href'])
			links[0].append(browser.find(id="i3").find('img')['src'])
	return [name, links]