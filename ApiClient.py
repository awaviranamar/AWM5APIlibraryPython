'''
    Created by Aviran Amar, API Support Engineer at AssetWorks. Built on 16th June 2025

'''
import requests
from Functions import Functions
import config
from endpoints import endpoints 

class ApiClient:
    def __init__(self, url="", payload=None, method="GET"):
        self.url = url
        self.func = Functions()
        self.token = self.func.fetch_token()
        self.payload = payload
        self.method = method
        self.results = None
        self.API = endpoints(self)
            
    def initAPI(self):
        self.API = endpoints(self)

    def getToken(self):
        self.token = self.func.fetch_token()
        return self.token

    def setToken(self, token=None):
        self.token = token
        
    def setPayload(self, payload=None):
        self.payload = payload

    def customAPI(self, method, payload=None, endpoint=""):
        self.url = config.api_url + endpoint
        self.method = method
        self.payload = payload
        self.initAPI()
        self.results = self.func.Url_exec(self)
        return self.results

    def getAPI(self, endpoint=""):
        self.url = config.api_url + endpoint
        self.initAPI()
        self.results = self.func.Url_exec(self)
        return self.results

    def putAPI(self, payload=None, endpoint=""):
        self.url = config.api_url + endpoint
        self.method = "PUT"
        self.payload = payload
        self.initAPI()
        self.results = self.func.Url_exec(self)
        return self.results

    def postAPI(self, payload=None, endpoint=""):
        self.url = config.api_url + endpoint
        self.method = "POST"
        self.payload = payload
        self.initAPI()
        self.results = self.func.Url_exec(self)
        return self.results

    def deleteAPI(self, payload=None, endpoint=""):
        self.url = config.api_url + endpoint
        self.method = "DELETE"
        self.initAPI()
        self.results = self.func.Url_exec(self)
        return self.results 

if __name__ == "__main__":
    client = ApiClient()
    payload = {}
    accidents = client.API.Accidents_Post(payload)
    print("Accidents data:", accidents)
