'''
    Custom Assets Model - Custom model for Assets
    Example of advanced model with enhanced functions
'''

import json
from datetime import datetime

class AssetsModel:
    def __init__(self, ApiClient):
        self.ApiClient = ApiClient

    def Assets_Get(self):
        """Custom function to get assets with logging"""
        print(f"🏭 [{datetime.now()}] Fetching all assets")
        try:
            result = self.ApiClient.getAPI('/assets')
            print(f"✅ Retrieved {len(result) if isinstance(result, list) else 'N/A'} assets")
            return result
        except Exception as e:
            print(f"❌ Error fetching assets: {e}")
            raise

    def Assets_GetById(self, asset_id):
        """Custom function to get asset by ID with validation"""
        print(f"🏭 Fetching asset ID: {asset_id}")
        
        # Basic validation
        if not asset_id or str(asset_id).strip() == "":
            raise ValueError("Asset ID cannot be empty")
        
        try:
            result = self.ApiClient.getAPI(f'/assets/{asset_id}')
            print(f"✅ Asset {asset_id} found successfully")
            return result
        except Exception as e:
            print(f"❌ Error fetching asset {asset_id}: {e}")
            raise

    def Assets_GetWithMaintenanceHistory(self, asset_id):
        """New function: Get asset with maintenance history"""
        print(f"🔧 Fetching asset {asset_id} with maintenance history")
        
        try:
            # Get asset data
            asset_data = self.ApiClient.getAPI(f'/assets/{asset_id}')
            
            # Get maintenance history (example)
            try:
                maintenance_data = self.ApiClient.getAPI(f'/workorders?assetId={asset_id}')
            except:
                maintenance_data = []
                print("⚠️ Could not retrieve maintenance history")
            
            result = {
                'asset': asset_data,
                'maintenance_history': maintenance_data,
                'retrieved_at': datetime.now().isoformat()
            }
            
            print(f"✅ Asset {asset_id} with maintenance history retrieved successfully")
            return result
            
        except Exception as e:
            print(f"❌ Error fetching asset with maintenance history: {e}")
            raise

    def Assets_Search(self, search):
        """Custom function to search assets with filters"""
        print(f"🔍 Searching assets: '{search}'")
        
        if not search or len(search.strip()) < 2:
            print("⚠️ Search string too short, returning empty list")
            return []
        
        try:
            result = self.ApiClient.getAPI(f'/assets/search/{search}')
            count = len(result) if isinstance(result, list) else 0
            print(f"✅ Found {count} assets for search '{search}'")
            return result
        except Exception as e:
            print(f"❌ Error searching assets: {e}")
            raise

    def Assets_GetSummary(self):
        """New function: Get assets summary"""
        print("📊 Generating assets summary")
        
        try:
            all_assets = self.ApiClient.getAPI('/assets')
            
            if not isinstance(all_assets, list):
                return {"error": "Could not retrieve assets list"}
            
            summary = {
                'total_assets': len(all_assets),
                'summary_generated_at': datetime.now().isoformat(),
                'asset_types': {},
                'status_distribution': {}
            }
            
            # Analyze data
            for asset in all_assets:
                # Count asset types
                asset_type = asset.get('assetType', 'Unknown')
                summary['asset_types'][asset_type] = summary['asset_types'].get(asset_type, 0) + 1
                
                # Count statuses
                status = asset.get('status', 'Unknown')
                summary['status_distribution'][status] = summary['status_distribution'].get(status, 0) + 1
            
            print(f"✅ Assets summary created successfully - Total {summary['total_assets']} assets")
            return summary
            
        except Exception as e:
            print(f"❌ Error creating assets summary: {e}")
            raise