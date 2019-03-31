#! /usr/bin/python3
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import requests

####################################################################################################

# setup the authentication
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('RCWmmrProgress.json',scope)

gc = gspread.authorize(credentials)
# opening the required spreadsheet and its sheet number
wksRankBadge = gc.open('RCWmmr').get_worksheet(0)
wksMMR = gc.open('RCWmmr').get_worksheet(1)


#####################################################################################################

#store all player ids associated with each member in the form of a URL
#777 Airavata Android hallucinogen Insane RedX Rex ShadowKnight TuskKnight

url777 = 'https://api.opendota.com/api/players/89349587'

urlAiravata =  'https://api.opendota.com/api/players/120791972'

urlAndroid = 'https://api.opendota.com/api/players/185336082'

urlHallucinogen = 'https://api.opendota.com/api/players/389265591'

urlInsane = 'https://api.opendota.com/api/players/418248671'

urlRedX = 'https://api.opendota.com/api/players/314500481'

urlRex = 'https://api.opendota.com/api/players/125035962'

urlShadowKnight = 'https://api.opendota.com/api/players/400885093'

urlTuskKnight = 'https://api.opendota.com/api/players/385284079'

#######################################################################################################

#functions for getting MMR of the player and the rank badge
def getMMR(str):
    r = requests.get(str).json()["mmr_estimate"]["estimate"]
    return r


def getRankBadge(str):
	a = 0
	b = requests.get(str).json()["rank_tier"]
	if(b == None):
		return a
	return b

# need todays date in the MM-DD-YY format in column 1
todaysDate = datetime.datetime.today()
dateFormat = todaysDate.strftime('%m-%d-%y')

######################################################################################################


# MMR variables

mmr777 = getMMR(url777)
mmrAiravata = getMMR(urlAiravata)
mmrAndroid = getMMR(urlAndroid)
mmrHallucinogen = getMMR(urlHallucinogen)
mmrInsane = getMMR(urlInsane)
mmrRedX = getMMR(urlRedX)
mmrRex = getMMR(urlRex)
mmrShadowKnight = getMMR(urlShadowKnight)
mmrTuskKnight = getMMR(urlTuskKnight)

######################################################################################################

# Rank Badge Variables

badge777 = getRankBadge(url777)
badgeAiravata = getRankBadge(urlAiravata)
badgeAndroid = getRankBadge(urlAndroid)
badgeHallucinogen = getRankBadge(urlHallucinogen)
badgeInsane = getRankBadge(urlInsane)
badgeRedX = getRankBadge(urlRedX)
badgeRex = getRankBadge(urlRex)
badgeShadowKnight = getRankBadge(urlShadowKnight)
badgeTuskKnight = getRankBadge(urlTuskKnight)


print(badgeTuskKnight)

#write it to the concerned spreadsheet
print("Writing rank badges")
wksRankBadge.append_row([dateFormat,badge777,badgeAiravata,badgeAndroid,badgeHallucinogen,badgeInsane,badgeRedX,badgeRex,badgeShadowKnight,badgeTuskKnight])
print("Completed writing Rank Badges")
print("Writing MMR ")
wksMMR.append_row([dateFormat,mmr777,mmrAiravata,mmrAndroid,mmrHallucinogen,mmrInsane,mmrRedX,mmrRex,mmrShadowKnight,mmrTuskKnight)

print("Script Succesfully Run")
