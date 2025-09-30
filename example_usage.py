#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example usage of the library with dynamic models
"""

from ApiClient import ApiClient

def main():
    """Example usage of the library with custom models"""
    
    print("🚀 Example usage of library with dynamic models")
    print("=" * 60)
    
    try:
        # Create API client
        client = ApiClient()
        
        print("\n📋 Usage examples:")
        
        # Example 1: Using custom function
        print("\n1️⃣ Using custom function:")
        print("   client.API.Accidents_Get()")
        # result = client.API.Accidents_Get()
        
        # Example 2: Using new function
        print("\n2️⃣ Using new function:")
        print("   client.API.Accidents_GetWithDetails(123)")
        # result = client.API.Accidents_GetWithDetails(123)
        
        # Example 3: Using advanced Assets functions
        print("\n3️⃣ Using advanced Assets functions:")
        print("   client.API.Assets_GetWithMaintenanceHistory(456)")
        # result = client.API.Assets_GetWithMaintenanceHistory(456)
        
        print("   client.API.Assets_GetSummary()")
        # summary = client.API.Assets_GetSummary()
        
        # Example 4: Using regular function (not customized)
        print("\n4️⃣ Using regular function (not customized):")
        print("   client.API.Employees_Get()")
        # result = client.API.Employees_Get()
        
        print("\n✨ All examples ready to use!")
        print("💡 Remove code comments (#) to execute actual calls")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

def demonstrate_custom_functionality():
    """Demonstrate custom functionality"""
    
    print("\n🎯 Demonstrating custom functionality:")
    print("-" * 50)
    
    try:
        client = ApiClient()
        
        # Check available functions
        print("\n🔍 Available custom functions:")
        
        custom_functions = []
        
        # Search for custom functions
        for attr_name in dir(client.API):
            if not attr_name.startswith('_'):
                attr = getattr(client.API, attr_name)
                if callable(attr):
                    # Check if it's a custom function (by print messages)
                    if any(keyword in attr_name for keyword in ['GetWithDetails', 'GetSummary', 'GetWithMaintenanceHistory']):
                        custom_functions.append(attr_name)
        
        if custom_functions:
            print("✅ Custom functions found:")
            for func in custom_functions:
                print(f"   • {func}")
        else:
            print("ℹ️ No special custom functions found")
        
        print("\n📊 Statistics:")
        all_methods = [m for m in dir(client.API) if not m.startswith('_') and callable(getattr(client.API, m))]
        print(f"   • Total available functions: {len(all_methods)}")
        print(f"   • Custom functions: {len(custom_functions)}")
        
    except Exception as e:
        print(f"❌ Error in demonstration: {e}")

if __name__ == "__main__":
    main()
    demonstrate_custom_functionality()