def suited(adress):
	return 'hentaihere.com' in adress

def resolve(adress, browser):
	Input = "https://" + adress
	browser.open(Input)
	name = browser.find(attrs={"href": Input}).text.replace("\n", "")

	links=[[]]
	c=1
	p=1
	while True:
		browser.open(Input + '/%s/%s' % (c, p))
		pic = browser.find(id='arf-reader-img')

    		#If there is no Picture Left, on the Site, the End is reached and the Loop breaks
		if not pic:
			break

		#If Code is Standard Pic, the next Chapter, is reached, reset Page and increment Chapter
		if pic['src'] !="https://hentaicdn.com/hentai":
			links[c-1].append(pic['src'])
			p=p+1
		else:
			p=1
			c=c+1
			links.append([])
	return [name, links]


