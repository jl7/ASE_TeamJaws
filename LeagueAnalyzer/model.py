import abc
#import views
class EntityModel(object):
    """This is the abstract class for the champion model and summoner model"""
    __metaclass__ = abc.ABCMeta

    def __init__(self, data):
        #Initialize the  data
        super(EntityModel, self).__init__()
        self._setAllWithoutUpdate(data)
            
    @abc.abstractmethod
    def _setAllWithoutUpdate(self, data):
        self.ID = data[ID]
        self.name = data[name]
        self.winRate = data[winRate]
        self.avgKills = data[avgKills]
        self.avgAssists = data[avgAssists]
        self.avgDeaths = data[avgDeaths]
        self.avgGameLength = data[avgGameLength]
        self.avgGoldEarned = data[avgGoldEarned]
 
    @abc.abstractmethod
    def _setAll(self, data):
        self._setAllWithoutUpdate(data)
        self._updateview()

    def _updateview(self):
        #call the view's update display method
        pass

    def setID(self, ID):
        self.ID = ID
        self._updateview()

    def setname(self, name):
        self.name = name
        self._updateview()

    def setwinRate(self, winRate):
        self.winRate = winRate
        self._updateview()

    def setavgKills(self, avgKills):
        self.avgKills = avgKills
        self._updateview()

    def setavgAssists(self, avgAssists):
        self.avgAssists = avgAssists
        self._updateview()

    def setavgDeaths(self, avgDeaths):
        self.avgDeaths = avgDeaths
        self._updateview()

    def setavgGameLength(self, avgGameLength):
        self.avgGameLength = avgGameLength
        self._updateview()

    def setavgGoldEarned(self, avgGoldEarned):
        self.avgGoldEarned = avgGoldEarned
        self._updateview()

    def getID(self):
        return self.ID

    def getname(self):
        return self.name

    def getwinRate(self):
        return self.winRate

    def getavgKills(self):
        return self.avgKills

    def getavgAssists(self):
        return self.avgAssists

    def getavgDeaths(self):
        return self.avgDeaths

    def getavgGameLength(self):
        return self.avgGameLength

    def getavgGoldEarned(self):
        return self.avgGoldEarned
