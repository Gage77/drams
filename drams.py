from bs4 import BeautifulSoup
import urllib.request as ur
import csv
from datetime import datetime

# Big ol' list of whiskeys
whiskeyList = []

f = open('whiskeys.csv', 'w+')
f.close()

# Have to use this to get around 403 forbidden error when fetching page
class AppURLOpener(ur.FancyURLopener):
    version = "Mozilla/5.0"

# Update CSV
def updateCSV(type):
    with open('whiskeys.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if type == 'Single Malt':
            writer.writerow(['Type', 'Name', 'Updated'])
        for w in whiskeyList:
            writer.writerow([type, w, datetime.now()])

# All letter lists will be of the same structure, so pass the html section
# for each letter here to parse 
def parseList(soup):
    azContainer = soup.body.div.find("div", "wrapper").find_all("div", "container")
    azList = azContainer[3].div.find_all("div", "az-letter")

    # List of whiskeys isolated
    for letter in azList:
        whiskeys = letter.find_all("li", "az-item")
        for a in whiskeys:
            whiskeyList.append(a.span.text)

# URL opener
opener = AppURLOpener()

# Scotch

## Single Malt
smUrl = 'https://www.thewhiskyexchange.com/brands/scotchwhisky/40/single-malt-scotch-whisky'
smOuter = opener.open(smUrl)
singleMaltPage = smOuter.read()
smSoup = BeautifulSoup(singleMaltPage, 'html.parser')
parseList(smSoup)
updateCSV('Single Malt')


## Blended Malt
bmUrl = 'https://www.thewhiskyexchange.com/brands/scotchwhisky/309/blended-malt-scotch-whisky'
bmOuter = opener.open(bmUrl)
blendedMaltPage = bmOuter.read()
bmSoup = BeautifulSoup(blendedMaltPage, 'html.parser')
parseList(bmSoup)
updateCSV('Blended Malt')

## Grain
gUrl = 'https://www.thewhiskyexchange.com/brands/scotchwhisky/310/grain-scotch-whisky'
gOuter = opener.open(gUrl)
grainPage = gOuter.read()
gSoup = BeautifulSoup(grainPage, 'html.parser')
parseList(gSoup)
updateCSV('Grain')

## Blended
bUrl = 'https://www.thewhiskyexchange.com/brands/scotchwhisky/304/blended-scotch-whisky'
bOuter = opener.open(bUrl)
blendedPage = bOuter.read()
bSoup = BeautifulSoup(blendedPage, 'html.parser')
parseList(bSoup)
updateCSV('Blended')

# Irish
iUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/32/irish-whiskey'
iOuter = opener.open(iUrl)
irishPage = iOuter.read()
iSoup = BeautifulSoup(irishPage, 'html.parser')
parseList(iSoup)
updateCSV('Irish')

# Japanese
jUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/35/japanese-whisky'
jOuter = opener.open(gUrl)
japanesePage = jOuter.read()
jSoup = BeautifulSoup(japanesePage, 'html.parser')
parseList(jSoup)
updateCSV('Japanese')

# Canadian
cUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/34/canadian-whisky'
cOuter = opener.open(cUrl)
canadaPage = cOuter.read()
cSoup = BeautifulSoup(canadaPage, 'html.parser')
parseList(cSoup)
updateCSV('Canadian')

# American
aUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/33/american-whiskey'
aOuter = opener.open(aUrl)
americanPage = aOuter.read()
aSoup = BeautifulSoup(americanPage, 'html.parser')
parseList(aSoup)
updateCSV('American')

# World
wUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/305/world-whisky'
wOuter = opener.open(wUrl)
worldPage = wOuter.read()
wSoup = BeautifulSoup(worldPage, 'html.parser')
parseList(wSoup)
updateCSV('World')
