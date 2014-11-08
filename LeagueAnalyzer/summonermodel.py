import abc
from abc_base import EntityModel
#import views

class SummonerModel(EntityModel):
    """docstring for SummonerModel"""
    def __init__(self, arg):
        super(SummonerModel, self).__init__()
        self.arg = arg

    def _setAllWithoutUpdate(self, data):
        """Sets all attributes without calling the view's updateDisplay method"""
        super(SummonerModel, self)._setAllWithoutUpdate(data)

    def _setAll(self, data):
        """Sets all attributes and call the view's updateDisplay method"""
        super(SummonerModel, self)._setAll(data)

    
