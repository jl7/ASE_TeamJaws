#import model
#import API
#import championDB
class Controller:
    """The controller provides the logic and calls the methods in the models"""
    def __init__(self, arg):
        """constructor"""
        super(Controller, self).__init__()
        self.arg = arg

    def generateSummonerStats(self, summName):
        """First get the summoner ID from summName with the method provided
        by API. Then get the data of the summoner using the method provided
        by API. The data is a dictionary. Set the data in the model. """
        #get summoner ID 
        #if the summoner doesn't exist, raise an exception for the view to catch
        #call the setters in the models
        pass

    def generateChampionStats(self, championID):
        """Get the data of the champion from the champion database. The data 
        is a list of strings. Set the data in the model. """
        try:
            #get the data from the champion database
            pass
        except Exception, e:
            #If can't connect to the database server, raise an exception
            raise
        else:
            #call the setters in the models
            pass
        
    def getSummonerID(self, summonerName):
        """Get the summoner ID with the name"""
        #get the summoner ID using the method provided by the API
        #return summonerID, a long number
        pass

    def validateName(self, summonerName):
        """Validate the summoner name, including checking whether the name exists.
        Return true if the name is valid"""
        pass

