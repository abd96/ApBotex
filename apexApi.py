import os,sys
import requests

class apexApi():

    def __init__(self,platform,username):
        self.url = "https://public-api.tracker.gg/apex/v1/standard/profile/{}/{}".format(platform,username)
        self.key = "32fda296-d88c-4341-b76f-aebcc5ec553d"


    """ returns data as json """
    def get(self):
        r = requests.get(url = self.url, headers = {"TRN-Api-Key":self.key})
        return r.json()

    def anotherGet(self):
        r = requests.get(url= "http://www.apexlegendsapi.com/api/v1/player?platform=pc&name=SaikoCoRe",headers = "ZeqebDXUJ2M-ph0z4wyUaMgvSF8ibNZNe5asqH5QbKk" )
        return r.json()
