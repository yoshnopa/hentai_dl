def suited(adress):
	return 'hentaifox.com' in adress

def resolve(adress, browser):
	Input = adress.replace('hentaifox.com/gallery/', '').replace('/', '')
	browser.open('http://hentaifox.com/gallery/' + Input + '/')
	header = browser.find(class_='info')
	name = header.h1.string

	links=[[]]
	p=1
	while True:
		browser.open('http://hentaifox.com/g/' + Input + '/' + str(p) + '/')
		#When the last possible number is already overcome, stop the iteration
		if int(browser.find_all('option')[-1].text) < p:
			break
		pic = browser.find(class_='lazy no_image')
		links[0].append('http:' + pic['src'])
		p=p+1

	return [name, links]
