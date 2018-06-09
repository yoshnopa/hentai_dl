def suited(adress):
	return 'hentai2read.com' in adress


def resolve(adress, browser):
	Input = adress.replace('hentai2read.com/', '').replace('/', '')
	name = Input.replace("_", " ")

	links=[[]]
	c=1
	p=1
	browser.open('http://hentai2read.com/' + Input)
	chapters = browser.find(class_="nav-chapters").findAll(class_="pull-left")[::-1]
	for chapter in chapters:
		while True:
			browser.open(chapter['href'] + str(p))
			pic = browser.find(id='arf-reader')

			if not pic:
				break

			#If Code is Standard Pic, the next Chapter, is reached, reset Page and increment Chapter
			if pic['src'] !="https://static.hentaicdn.com/hentai":
				links[c-1].append(pic['src'])
				p=p+1
			else:
				p=1
				c=c+1
				links.append([])
				break
	links = links[:-1]
	return [name, links]
