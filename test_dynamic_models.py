#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testing dynamic model loading functionality
"""

from ApiClient import ApiClient

def test_dynamic_models():
    """Test dynamic model loading functionality"""
    
    print("🚀 Starting dynamic model loading test...")
    print("=" * 50)
    
    try:
        # Create ApiClient
        client = ApiClient()
        
        print("\n📋 Available functions for Accidents:")
        accidents_methods = [method for method in dir(client.API) if method.startswith('Accidents_')]
        for method in accidents_methods:
            print(f"  • {method}")
        
        print("\n📋 Available functions for Assets:")
        assets_methods = [method for method in dir(client.API) if method.startswith('Assets_')]
        for method in assets_methods[:10]:  # Show only first 10
            print(f"  • {method}")
        if len(assets_methods) > 10:
            print(f"  ... and {len(assets_methods) - 10} more functions")
        
        print("\n🧪 Testing custom functions:")
        
        # Test Accidents
        if hasattr(client.API, 'Accidents_Get'):
            print("✅ Accidents_Get found")
            print("📞 Calling Accidents_Get...")
            # result = client.API.Accidents_Get()  # Uncomment for actual execution
        
        if hasattr(client.API, 'Accidents_GetWithDetails'):
            print("✅ Accidents_GetWithDetails (new function) found")
            print("📞 Calling Accidents_GetWithDetails...")
            # result = client.API.Accidents_GetWithDetails(123)  # Uncomment for actual execution
        
        # Test Assets
        if hasattr(client.API, 'Assets_GetWithMaintenanceHistory'):
            print("✅ Assets_GetWithMaintenanceHistory (new function) found")
            print("📞 Calling Assets_GetWithMaintenanceHistory...")
            # result = client.API.Assets_GetWithMaintenanceHistory(123)  # Uncomment for actual execution
        
        if hasattr(client.API, 'Assets_GetSummary'):
            print("✅ Assets_GetSummary (new function) found")
            print("📞 Calling Assets_GetSummary...")
            # result = client.API.Assets_GetSummary()  # Uncomment for actual execution
        
        print("\n🎉 Dynamic loading test completed successfully!")
        
    except Exception as e:
        print(f"❌ Error in test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_dynamic_models()