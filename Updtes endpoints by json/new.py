import json

def generate_class_from_openapi(openapi_doc):
    class_code = "'''\n"
    class_code += "    Generated endpoints with Dynamic Model Loading support\n"
    class_code += "    Created by Aviran Amar, API Support Engineer at AssetWorks\n"
    class_code += "'''\n"
    class_code += "import os\n"
    class_code += "import importlib.util\n"
    class_code += "import inspect\n\n"
    class_code += "class endpoints:\n"
    class_code += "    def __init__(self, ApiClient):\n"
    class_code += "        self.ApiClient = ApiClient\n"
    class_code += "        self._load_custom_models()\n\n"
    class_code += "    def _load_custom_models(self):\n"
    class_code += "        \"\"\"Load custom models from models directory\"\"\"\n"
    class_code += "        models_dir = os.path.join(os.path.dirname(__file__), 'models')\n"
    class_code += "        \n"
    class_code += "        if not os.path.exists(models_dir):\n"
    class_code += "            return\n"
    class_code += "        \n"
    class_code += "        for filename in os.listdir(models_dir):\n"
    class_code += "            if filename.endswith('.py') and filename != '__init__.py':\n"
    class_code += "                model_name = filename[:-3]\n"
    class_code += "                model_path = os.path.join(models_dir, filename)\n"
    class_code += "                \n"
    class_code += "                try:\n"
    class_code += "                    spec = importlib.util.spec_from_file_location(model_name, model_path)\n"
    class_code += "                    module = importlib.util.module_from_spec(spec)\n"
    class_code += "                    spec.loader.exec_module(module)\n"
    class_code += "                    \n"
    class_code += "                    for name, obj in inspect.getmembers(module, inspect.isclass):\n"
    class_code += "                        if name.endswith('Model'):\n"
    class_code += "                            model_instance = obj(self.ApiClient)\n"
    class_code += "                            \n"
    class_code += "                            prefix = model_name + '_'\n"
    class_code += "                            for method_name in dir(model_instance):\n"
    class_code += "                                if method_name.startswith(prefix) and not method_name.startswith('_'):\n"
    class_code += "                                    setattr(self, method_name, getattr(model_instance, method_name))\n"
    class_code += "                                    print(f\"Replaced: {method_name} from {model_name} model\")\n"
    class_code += "                            \n"
    class_code += "                            break\n"
    class_code += "                            \n"
    class_code += "                except Exception as e:\n"
    class_code += "                    print(f\"Error loading model {model_name}: {e}\")\n\n"
    
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
    
    with open('generated_api_client.py', 'w', encoding='utf-8') as file:
        file.write(class_code)

if __name__ == "__main__":
    main()