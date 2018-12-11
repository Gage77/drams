from bs4 import BeautifulSoup
import urllib.request as ur
import csv
import time

start_time = time.time()
totalNumWhiskeys = 0
totalNumDistilleries = 0

BASE_URL = 'https://www.thewhiskyexchange.com'
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
            writer.writerow(['Type', 'Distillery', 'Whiskeys'])
        for w in whiskeyList:
            if w[0] == type:
                writer.writerow([w[0], w[1], w[2]])

# Get list of individual whiskeys under a specific distillery
def parseIndividualWhiskeys(brandURL):
    listowhiskeys = []
    global totalNumWhiskeys

    indURL = BASE_URL + brandURL
    print(indURL)
    indOuter = opener.open(indURL)
    indPage = indOuter.read()
    indSoup = BeautifulSoup(indPage, 'html.parser')
    pGrid = indSoup.body.div.find("div", "wrapper").find("div", "products-wrapper").find("div", "products-grid")
    # Check if said distillery has any whiskeys posted on Whiskey Exchange
    if pGrid != None:
        indList = indSoup.body.div.find("div", "wrapper").find("div", "products-wrapper").div.div.find_all("div", "item")
        for i in indList:
            subText = i.a.find("div", "information").div.span
            if subText != None:
                subText = i.a.find("div", "information").div.span.text
                i.a.find("div", "information").div.span.replace_with('')
                listowhiskeys.append(i.a.find("div", "information").div.text.strip() + ' ' + subText)
            else:
                listowhiskeys.append(i.a.find("div", "information").div.text.strip())
            totalNumWhiskeys += 1
    # Otherwise, append None
    else:
        listowhiskeys.append('None')

    return listowhiskeys


# All letter lists will be of the same structure, so pass the html section
# for each letter here to parse 
def parseList(soup, type):
    global totalNumDistilleries
    azContainer = soup.body.div.find("div", "wrapper").find_all("div", "container")
    azList = azContainer[3].div.find_all("div", "az-letter")

    # List of whiskeys isolated
    for letter in azList:
        whiskeys = letter.find_all("li", "az-item")
        for a in whiskeys:
            dLink = a.a['href']
            dWhiskeys = parseIndividualWhiskeys(dLink) # List of whiskeys
            # Type, Distillery, List of whiskeys
            whiskeyList.append([type, a.span.text, dWhiskeys])
            totalNumDistilleries += 1


# URL opener
opener = AppURLOpener()

## Single Malt
smUrl = 'https://www.thewhiskyexchange.com/brands/scotchwhisky/40/single-malt-scotch-whisky'
smOuter = opener.open(smUrl)
singleMaltPage = smOuter.read()
smSoup = BeautifulSoup(singleMaltPage, 'html.parser')
parseList(smSoup, 'Single Malt')
updateCSV('Single Malt')

## Blended Malt
bmUrl = 'https://www.thewhiskyexchange.com/brands/scotchwhisky/309/blended-malt-scotch-whisky'
bmOuter = opener.open(bmUrl)
blendedMaltPage = bmOuter.read()
bmSoup = BeautifulSoup(blendedMaltPage, 'html.parser')
parseList(bmSoup, 'Blended Malt')
updateCSV('Blended Malt')

## Grain
gUrl = 'https://www.thewhiskyexchange.com/brands/scotchwhisky/310/grain-scotch-whisky'
gOuter = opener.open(gUrl)
grainPage = gOuter.read()
gSoup = BeautifulSoup(grainPage, 'html.parser')
parseList(gSoup, 'Grain')
updateCSV('Grain')

## Blended
bUrl = 'https://www.thewhiskyexchange.com/brands/scotchwhisky/304/blended-scotch-whisky'
bOuter = opener.open(bUrl)
blendedPage = bOuter.read()
bSoup = BeautifulSoup(blendedPage, 'html.parser')
parseList(bSoup, 'Blended')
updateCSV('Blended')

# Irish
iUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/32/irish-whiskey'
iOuter = opener.open(iUrl)
irishPage = iOuter.read()
iSoup = BeautifulSoup(irishPage, 'html.parser')
parseList(iSoup, 'Irish')
updateCSV('Irish')

# Japanese
jUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/35/japanese-whisky'
jOuter = opener.open(gUrl)
japanesePage = jOuter.read()
jSoup = BeautifulSoup(japanesePage, 'html.parser')
parseList(jSoup, 'Japanese')
updateCSV('Japanese')

# Canadian
cUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/34/canadian-whisky'
cOuter = opener.open(cUrl)
canadaPage = cOuter.read()
cSoup = BeautifulSoup(canadaPage, 'html.parser')
parseList(cSoup, 'Canadian')
updateCSV('Canadian')

# American
aUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/33/american-whiskey'
aOuter = opener.open(aUrl)
americanPage = aOuter.read()
aSoup = BeautifulSoup(americanPage, 'html.parser')
parseList(aSoup, 'American')
updateCSV('American')

# World
wUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/305/world-whisky'
wOuter = opener.open(wUrl)
worldPage = wOuter.read()
wSoup = BeautifulSoup(worldPage, 'html.parser')
parseList(wSoup, 'World')
updateCSV('World')

# Show runtime
print('Total number of distilleries in DB: ' + str(totalNumDistilleries))
print('Total number of whiskeys in DB: ' + str(totalNumWhiskeys))
print("Drams finished in (seconds): ", time.time() - start_time)