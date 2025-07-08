'''
    Created by Aviran Amar, API Support Engineer at AssetWorks. Built on 16th June 2025

'''
import requests
import urllib3
import config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Functions:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}

    def fetch_token(self):
        payload = {
            "Username": config.username,
            "Password": config.password,
            "Site": config.site
        }
        try:
            response = requests.post(config.token_url, headers=self.headers, json=payload, verify=False)
            response.raise_for_status()
            return response.json()["items"][0]
        except requests.exceptions.RequestException as e:
            print(f"[TokenFetcher] Token request failed: {e}")
            return None
    
    def Url_exec(self, apiClient):
        headers = {
            "Authorization": f"Bearer {apiClient.token}",
            "Content-Type": "application/json"
        }
        method = apiClient.method.upper()
        try:
            if method == "GET":
                response = requests.get(apiClient.url, headers=headers)
            elif method == "POST":
                response = requests.post(apiClient.url, headers=headers, json=apiClient.payload)
            elif method == "PUT":
                response = requests.put(apiClient.url, headers=headers, json=apiClient.payload)
            elif method == "DELETE":
                response = requests.delete(apiClient.url, headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()
            results = response.text
            return results

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            #return None
