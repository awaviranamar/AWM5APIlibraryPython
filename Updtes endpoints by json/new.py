import json

def generate_class_from_openapi(openapi_doc):
    class_code = "class endpoints:\n"
    class_code += "    def __init__(self, ApiClient):\n"
    class_code += "        self.ApiClient = ApiClient\n\n"
    
    for path, methods in openapi_doc["paths"].items():
        for method, details in methods.items():
            method_name = details.get("operationId", f"{method}_{path.strip('/').replace('/', '_')}")
            method_name = method_name.replace("api_v1_", "")  # Optional cleanup
            endpoint = path.replace('/api/v1/', '/')
            params = [part[1:-1] for part in path.split('/') if part.startswith('{') and part.endswith('}')]
            param_str = ', '.join(params)
            param_str = f", {param_str}" if param_str else ""

            if method.lower() == "get":
                class_code += f"    def {method_name}(self{param_str}):\n"
                class_code += f"        return self.ApiClient.getAPI(f'{endpoint}')\n\n"
            elif method.lower() == "post":
                class_code += f"    def {method_name}(self{param_str}):\n"
                class_code += f"        return self.ApiClient.postAPI(self.ApiClient.payload, f'{endpoint}')\n\n"
            elif method.lower() == "put":
                class_code += f"    def {method_name}(self{param_str}):\n"
                class_code += f"        return self.ApiClient.putAPI(self.ApiClient.payload, f'{endpoint}')\n\n"
            elif method.lower() == "delete":
                class_code += f"    def {method_name}(self{param_str}):\n"
                class_code += f"        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'{endpoint}')\n\n"
    
    return class_code

def main():
    with open('openapi.json', 'r') as file:
        openapi_doc = json.load(file)
    
    class_code = generate_class_from_openapi(openapi_doc)
    
    with open('generated_api_client.py', 'w') as file:
        file.write(class_code)

if __name__ == "__main__":
    main()
