from bs4 import BeatifulSoup as bs
import urllib2

# Scotch

## Single Malt
smUrl = 'https://www.thewhiskyexchange.com/brands/scotchwhisky/40/single-malt-scotch-whisky'

## Blended Malt
bmUrl = 'https://www.thewhiskyexchange.com/brands/scotchwhisky/309/blended-malt-scotch-whisky'

## Grain
gUrl = 'https://www.thewhiskyexchange.com/brands/scotchwhisky/310/grain-scotch-whisky'

## Blended
bUrl = 'https://www.thewhiskyexchange.com/brands/scotchwhisky/304/blended-scotch-whisky'

# Irish
iUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/32/irish-whiskey'

# Japanese
jUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/35/japanese-whisky'

# Canadian
cUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/34/canadian-whisky'

# American
aUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/33/american-whiskey'

# World
wUrl = 'https://www.thewhiskyexchange.com/brands/worldwhisky/305/world-whisky'