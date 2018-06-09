# hentai_dl


Modular commandline downloader inspired by youtube-dl. Written to download comics in general with a focus on Hentai Pages. About a dozen pages currently supported!
It's written in python3 (tested 3.4-3.6), depends on robobrowser and the requests library.


## Installation:
First, you need [Python](https://www.python.org) in version 3. After that you need additional modules, installed like this:
```
python3 -m pip install requests robobrowser
```
Clone this repository. The HDownloader.py is good to go!


## Currently Supported:
* [8muses.com](https://8muses.com)
* [bato.to](http://bato.to)
* [doujins.com](http://doujins.com)
* [e-hentai.org](http://e-hentai.org)
* [fanfox.net](http://fanfox.net)
* [hbrowse.com](http://hbrowse.com)
* [hentai2read.com](https://hentai2read.com)
* [hentaifox.com](https://hentaifox.com)
* [hentaihere.com](http://hentaihere.com)
* [hitomi.la](http://hitomi.la)
* [nhentai.net](http://nhentai.net)
* [porncomix.info](http://www.porncomix.info)
* [pururin.io](http://pururin.io)

**Open an issue if you want another page to join the list**

The downloader works only with the url of the overview page. This means in general the page that has sometimes thumbnails, but never a fully fledged image. In case of doubt, the shortest url is always right.
The download always contains of a folder named by the sites comicname containing all images. The images are numbered through, along with the first number being the current chapter (if the page doesnt have chapters, the first number is always 1).

The downloader can use a http proxy and update an already downloaded folder.


### Options:
The script is triggered by running the HDownloader.py
For the quick download, just past any amount of urls behind it, they will be downloaded one after another. Further options are available:

```
./HDownloader.py --help
usage: HDownloader.py [-h] [-f] [-p PROXY] [-o DIRECTORY] [-i LINKFILE]
                      [-u OLDFILE] [-d DELETED]
                      [Downloadlink [Downloadlink ...]]

positional arguments:
  Downloadlink          Add Links to download, links are accepted from 8muses,
                        Pururin, Hentai2read, Hitomi, Hentaifox, nhentai,
                        hentaihere, hbrowse, doujin, e-Hentai and porncomix

optional arguments:
  -h, --help            show this help message and exit
  -f, --force           overwrite existing folders if necessary, this deletes
                        all content of those folders! Folder name is the name
                        of the Hentai from the site
  -p PROXY, --proxy PROXY
                        you may provide a http proxy here. Example: -p
                        http://127.0.0.1:8118
  -o DIRECTORY, --output DIRECTORY
                        write the output directory here. If not set, the
                        directory you're currently in is used
  -i LINKFILE, --input LINKFILE
                        you may provide a textfile containing download Links.
                        You may seperate them with any combination of
                        whitespaces, tabs and new Lines. Combining this with
                        default Link input is possible.
  -u OLDFILE, --update OLDFILE
                        you may take an already downloaded Comic and get newer
                        material from the same source. This cannot be used
                        with multiple input, only one update can be done at a
                        time.
  -d DELETED, --deleted DELETED
                        only used in combination with update. Provide a number
                        that resembles the amount of files you deleted from
                        the original download (they will be skipped). This number will be recognized
                        in all future updates and can be changed with this
                        command.
```

I'm open for feature ideas, just submit an issue
