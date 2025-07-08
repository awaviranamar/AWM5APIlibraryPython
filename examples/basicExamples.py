import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)


from ApiClient import ApiClient  

if __name__ == "__main__":
    client = ApiClient()
    
    #Here are some examples of retrieving data, such as searching for specific terms or retrieving by specific ID.
    accidents = client.API.Accidents_Get() #Retrieve all accident reports.
    print("Accidents data:", accidents)
    
    accidents = client.API.Accidents_Search("Car") #Search for specific terms.
    print("Accidents data for 'Car':", accidents)
    
    accidents = client.API.Assets_GetById("1234") #Retrieve the asset by its ID.
    print("Accidents data for '1234':", accidents)
    
    #Configure the payload as a JSON structure.
    payload = { "body":{
            "assetId": "#1UNIT1",
            "acquisitionDate": "2019-02-01T08:00:00Z",
            "Active": "true",
            "billingId": "CL",
            "maintenanceLocationId": "FM",
            "owningDeptId": "0010"}}
    #Configure the payload within the client object.
    client.setPayload(payload)
    
    
    '''
        Here are some examples, including create, update, and delete.
    '''
    
    #Updating the existing asset.
    #print(client.API.Assets_Put())
    #Creating a new assets
    #print(client.API.Assets_Post())
    #Delete a userclass
    #print(client.API.UserClasses_Delete())

