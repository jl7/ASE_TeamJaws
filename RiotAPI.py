KEY = "KEY"
import requests # not native, need to install
import json

class RiotAPI:
    
    def __init__(self):
        pass

    #def checkStatusCode(self, code):
        #if code == 

    #Returns summonerID if request sucessful, or the status code if fails
    def requestSummonerID(self, summonerName):
        request = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + summonerName + "?api_key=" + KEY)
        if request.ok == True:
            jsonObj = request.json()
            jsonDic = jsonObj.values()[0]
            summonerID = jsonDic["id"]
            return summonerID
        else:
            return request.status_code

    #Returns recent match history if request sucessful, or the status code if fails
    def requestSummoner(self, summonerID):

        request = requests.get("https://na.api.pvp.net/api/lol/na/v2.2/matchhistory/"+summonerID+"?api_key="+ KEY)
        if request.ok == True:
            playerHistory = request.json()
            return playerHistory
        else:
            return request.status_code

    #Returns all champion data if request sucessful, or the status code if fails
    #Static information, need only call once in a while to check for updates (ie new champion)
        #only useful information to pull from this is the Champion name (under name, not key) and its ID (under id)
    #API call does not count towards key limit 
    def requestChampion(self):        
        request = requests.get("https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion?api_key=" +KEY)
        if request.ok == True:
            champJSON = request.json()
            return champJSON
        else:
            return request.status_code

    #Returns details on a match if request sucessful, or the status code if fails
    def requestMatch(self, matchID):
        request = requests.get("https://na.api.pvp.net/api/lol/na/v2.2/match/"+matchID+"?api_key="+KEY)
        if request.ok == True:
            matchJSON = request.json()
            return matchJSON
        else:
            return request.status_code


# get 10 people ourselves
# look at their recent games
# get the people from their recent games
# check those people's recent games
# repeat
# have a list of people in a queue with which to lookup the history of



#Instead of requestSummon (as all it does of use is provide the champ name by the id, which could be stored in a table),
#implement requestmatch, which can be used to find the details of other players who partipated in someone's "recent match"
    #contains summonerID's
