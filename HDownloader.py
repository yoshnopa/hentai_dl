#!/usr/bin/env python3

#Prerequisites:
#sudo apt-get install python3
#pip3 install robobrowser requests

#A wait variable to get on fair footing with the providers, also in the scrapers

from HTemplates import *
from robobrowser import RoboBrowser
import requests, os, shutil, argparse, time, imghdr
import warnings
warnings.filterwarnings("ignore")

#Waittime to spare the hosters. Only used for the download, not the scraping (yet)
sleep=2

browser = RoboBrowser(
history=True,
user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Chromium/42.0'
)

def download(adress):
	#This gets all Objects inside the HTemplates
	scrapers=[]
	while True:
		try:
			for key, value in globals().items():
				if "HTemplates" in str(value) and key != "value":
					scrapers.append(key)
		except RuntimeError:
			continue
		break

	#Adresses are cut for easier working
	if adress[-1] == "/":
		adress = adress[:-1]
	if adress[0:7] == 'http://':
		adress = adress[7:]
	elif adress[0:8] == 'https://':
		adress = adress[8:]

	#A fitting Scraper is searched
	for scraper in scrapers:
		if globals()[scraper].suited(adress):
			scrape=scraper
			break
	if "scrape" not in locals():
		print('The adress ' + adress + ' does not match any downloader')
		exit()

	#Scraping is done, Folder is created
	dlData = globals()[scrape].resolve(adress, browser)
	hname = dlData[0]
	linkData = dlData[1]
	if not imgnumber:
		mkdir(hname)
	else:
		hname='.'

	#Files get downloaded
	imagecount=0
	c = 0
	for chapter in linkData:
		c = c + 1
		p = 0
		for link in chapter:
			imagecount = imagecount +1
			p = p + 1
			name=str(p)
			while len(name) < 3:
				name='0' + name
			name= str(c) + name + '.' + link.split(".")[-1].split("?")[0]

			if not imgnumber > imagecount:
				r = requests.get(link, stream=True)
				with open(hname + "/" + name, 'wb') as f:
					r.raw.decode_content = True
					shutil.copyfileobj(r.raw, f)
				time.sleep(sleep)


def mkdir(name):
    if os.path.exists(name):
        if args.force:
            shutil.rmtree(name)
        else:
            print("Error: The Folder '" + name + "' already exists! If you want to overwrite anyway, use the -f or --force option")
            exit()
    os.makedirs(name)


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', action='store_true', dest='force', help='overwrite existing folders if necessary, this deletes all content of those folders! Folder name is the name of the Hentai from the site')
parser.add_argument('-p', '--proxy', dest='proxy', help='you may provide a http proxy here. Example: -p http://127.0.0.1:8118')
parser.add_argument('-o', '--output', dest='directory', help='write the output directory here. If not set, the directory your in is used')
parser.add_argument('-i', '--input', dest='linkfile', help='you may provide a textfile containing download Links. You may seperate them with any combination of whitespaces, tabs and new Lines. Combining this with default Link input is possible.')
parser.add_argument('-u', '--update', dest='oldFile', help='you may take an already downloaded Comic and get newer material from the same source. This cannot be used with multiple input, only one update can be done at a time. ')
parser.add_argument('-d', '--deleted', dest='deleted', help='only used in combination with update. Provide a number that resembles the amount of files you deleted from the original download. This number will be recognized in all future updates and can be changed with this command.')
parser.add_argument('links', metavar='Downloadlink', nargs='*', help='Add Links to download, links are accepted from 8muses, Pururin, Hentai2read, Hitomi, Hentaifox, nhentai, hentaihere, hbrowse, doujin, e-Hentai and porncomix')
args = parser.parse_args()


adresses=args.links
if args.linkfile:
    with open(args.linkfile, 'r') as myfile:
        filelinks = myfile.read()
    filelinks = filelinks.replace('\n', ' ').replace('\t', ' ').split(' ')
    filelinks = list(filter(None, filelinks))
    adresses = adresses + filelinks
if args.directory:
    os.chdir(args.directory)
imgnumber=0
if args.oldFile:
	if len(adresses) > 1:
		print("The update Option cannot be used with multiple source links. Please specify only one link from any source.")
		exit()
	else:
		os.chdir(args.oldFile)
		files = os.listdir()
		for file in files:
			if imghdr.what(file):
				imgnumber=imgnumber + 1
		if args.deleted:
			imgnumber=int(args.deleted) + imgnumber
			file = open('.deleted', 'w+')
			file.write(args.deleted)
			file.close()
		else:
			if os.path.isfile('.deleted'):
				file = open('.deleted', 'r+')
				imgnumber = int(file.read()) + imgnumber
				file.close()
if args.proxy:
    os.environ['HTTP_PROXY'] = args.proxy
    os.environ['HTTPS_PROXY'] = args.proxy


for adress in adresses:
	download(adress)
