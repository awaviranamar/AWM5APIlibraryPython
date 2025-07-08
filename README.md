[Read Me.docx](https://github.com/user-attachments/files/21129708/Read.Me.docx)
# AWM5APIlibraryPython
________________________________________
📘 Guide to Using the M5 API Python Library
📁 Project Structure
project/
│
├── config.py
├── ApiClient.py
├── Functions.py
├── endpoints.py
└── main.py (optional for testing)
________________________________________
1. 🔧 Configuration (config/config.py)
This file stores your credentials and API URLs.
username = "The_User_Name"
password = "The_Password"
site = "The_DB_site"
token_url = "The_Token_URL"  # No trailing slash
api_url = "The_API_URL"      # No trailing slash
⚠️ Never commit this file to version control if it contains real credentials.
________________________________________
2. 🧠 Core Logic
Functions.py
Handles:
•	Token fetching
•	Executing HTTP requests
class Functions:
    def fetch_token(self):
        # Authenticates and returns a bearer token
    def Url_exec(self, apiClient):
        # Executes GET, POST, PUT, DELETE requests using the token
________________________________________
ApiClient.py
This is the main interface to interact with the API.
class ApiClient:
    def __init__(self, url="", payload=None, method="GET"):
        self.token = self.func.fetch_token()
Key Methods:
•	getToken() – Refreshes and returns the token
•	customAPI(method, payload, endpoint) – Custom API call
•	getAPI(endpoint) – GET request
•	postAPI(payload, endpoint) – POST request
•	putAPI(payload, endpoint) – PUT request
•	deleteAPI(payload, endpoint) – DELETE request
________________________________________
endpoints.py
This file defines endpoint-specific methods. For example:
class endpoints:
    def Accidents_Get(self):
        return self.ApiClient.getAPI('/accidents')

    def Accidents_GetById(self, id):
        return self.ApiClient.getAPI(f'/accidents/{id}')
You can expand this class with more endpoints as needed.
________________________________________
3. 🚀 How to Use
Example: Fetching an Accident by ID
from ApiClient import ApiClient

client = ApiClient()
accident = client.API.Accidents_GetById(5)
print("Accident Data:", accident)
________________________________________
4. 🧪 Testing Tips
•	Use print(client.getToken()) to verify token retrieval.
•	Use client.customAPI("GET", endpoint="/your-endpoint") for quick testing.
________________________________________
5. 🛠️ Extending the Library
To add a new endpoint:
1.	Add a method in endpoints.py:
   def Vehicles_Get(self):
       return self.ApiClient.getAPI('/vehicles')
2.	Call it like:
   vehicles = client.API.Vehicles_Get()
________________________________________

