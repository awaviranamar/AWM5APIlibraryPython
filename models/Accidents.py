'''
    Custom Accidents Model - Example of custom model implementation
    This file will override standard Accidents functions in endpoints.py
'''

class AccidentsModel:
    def __init__(self, ApiClient):
        self.ApiClient = ApiClient

    def Accidents_Get(self):
        """Custom function to get accidents"""
        print("🚗 Using custom model for Accidents_Get")
        return self.ApiClient.getAPI('/accidents')

    def Accidents_Post(self):
        """Custom function to create accident"""
        print("🚗 Using custom model for Accidents_Post")
        return self.ApiClient.postAPI(self.ApiClient.payload, '/accidents')

    def Accidents_Search(self, search):
        """Custom function to search accidents"""
        print(f"🚗 Using custom model for Accidents_Search: {search}")
        return self.ApiClient.getAPI(f'/accidents/search/{search}')

    def Accidents_SearchExact(self, search):
        """Custom function for exact accident search"""
        print(f"🚗 Using custom model for Accidents_SearchExact: {search}")
        return self.ApiClient.getAPI(f'/accidents/searchexact/{search}')

    def Accidents_GetById(self, Theid):
        """Custom function to get accident by ID"""
        print(f"🚗 Using custom model for Accidents_GetById: {Theid}")
        return self.ApiClient.getAPI(f'/accidents/{Theid}')

    # Additional custom functions can be added
    def Accidents_GetWithDetails(self, accident_id):
        """New custom function"""
        print(f"🚗 New function: Get accident with full details: {accident_id}")
        return self.ApiClient.getAPI(f'/accidents/{accident_id}')