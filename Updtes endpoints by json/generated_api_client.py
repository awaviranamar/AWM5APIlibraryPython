class endpoints:
    def __init__(self, ApiClient):
        self.ApiClient = ApiClient

    def Accidents_Get(self):
        return self.ApiClient.getAPI(f'/accidents')

    def Accidents_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/accidents')

    def Accidents_Search(self, search):
        return self.ApiClient.getAPI(f'/accidents/search/{search}')

    def Accidents_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/accidents/searchexact/{search}')

    def Accidents_GetById(self, id):
        return self.ApiClient.getAPI(f'/accidents/{id}')

    def AccountPartIssues_Get(self):
        return self.ApiClient.getAPI(f'/accountPartIssues')

    def AccountPartIssues_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/accountPartIssues')

    def AccountPartIssues_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/accountPartIssues')

    def AccountPartIssues_Search(self, search):
        return self.ApiClient.getAPI(f'/accountPartIssues/search/{search}')

    def AccountPartIssues_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/accountPartIssues/searchexact/{search}')

    def AccountPartIssues_GetById(self, id):
        return self.ApiClient.getAPI(f'/accountPartIssues/{id}')

    def Accounts_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/accounts/bulk')

    def Accounts_Update(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/accounts/bulk')

    def Accounts_Get(self):
        return self.ApiClient.getAPI(f'/accounts')

    def Accounts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/accounts')

    def Accounts_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/accounts')

    def Accounts_Search(self, search):
        return self.ApiClient.getAPI(f'/accounts/search/{search}')

    def Accounts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/accounts/searchexact/{search}')

    def Accounts_GetById(self, id):
        return self.ApiClient.getAPI(f'/accounts/{id}')

    def AppointmentRequests_Get(self):
        return self.ApiClient.getAPI(f'/appointmentRequests')

    def AppointmentRequests_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/appointmentRequests')

    def AppointmentRequests_Search(self, search):
        return self.ApiClient.getAPI(f'/appointmentRequests/search/{search}')

    def AppointmentRequests_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/appointmentRequests/searchexact/{search}')

    def AppointmentRequests_GetById(self, id):
        return self.ApiClient.getAPI(f'/appointmentRequests/{id}')

    def AssetAttributes_CreatePost(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetAttributes/bulk')

    def AssetAttributes_CreatePut(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/assetAttributes/bulk')

    def AssetAttributes_Get(self):
        return self.ApiClient.getAPI(f'/assetAttributes')

    def AssetAttributes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetAttributes')

    def AssetAttributes_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/assetAttributes')

    def AssetAttributes_Search(self, search):
        return self.ApiClient.getAPI(f'/assetAttributes/search/{search}')

    def AssetAttributes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetAttributes/searchexact/{search}')

    def AssetAttributes_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetAttributes/{id}')

    def AssetCategories_Get(self):
        return self.ApiClient.getAPI(f'/assetCategories')

    def AssetCategories_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetCategories')

    def AssetCategories_Search(self, search):
        return self.ApiClient.getAPI(f'/assetCategories/search/{search}')

    def AssetCategories_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetCategories/searchexact/{search}')

    def AssetCategories_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetCategories/{id}')

    def AssetChangeLogs_Get(self):
        return self.ApiClient.getAPI(f'/assetChangeLogs')

    def AssetChangeLogs_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetChangeLogs')

    def AssetChangeLogs_Search(self, search):
        return self.ApiClient.getAPI(f'/assetChangeLogs/search/{search}')

    def AssetChangeLogs_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetChangeLogs/searchexact/{search}')

    def AssetChangeLogs_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetChangeLogs/{id}')

    def AssetClasses_Get(self):
        return self.ApiClient.getAPI(f'/assetClasses')

    def AssetClasses_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetClasses')

    def AssetClasses_Search(self, search):
        return self.ApiClient.getAPI(f'/assetClasses/search/{search}')

    def AssetClasses_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetClasses/searchexact/{search}')

    def AssetClasses_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetClasses/{id}')

    def AssetComponentWarranties_Get(self):
        return self.ApiClient.getAPI(f'/assetComponentWarranties')

    def AssetComponentWarranties_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetComponentWarranties')

    def AssetComponentWarranties_Search(self, search):
        return self.ApiClient.getAPI(f'/assetComponentWarranties/search/{search}')

    def AssetComponentWarranties_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetComponentWarranties/searchexact/{search}')

    def AssetComponentWarranties_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetComponentWarranties/{id}')

    def AssetCreditCard_BulkPost(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/AssetCreditCards/bulk')

    def AssetCreditCard_BulkPut(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/AssetCreditCards/bulk')

    def AssetCreditCard_Get(self):
        return self.ApiClient.getAPI(f'/AssetCreditCards')

    def AssetCreditCard_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/AssetCreditCards')

    def AssetCreditCard_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/AssetCreditCards')

    def AssetCreditCard_Search(self, search):
        return self.ApiClient.getAPI(f'/AssetCreditCards/search/{search}')

    def AssetCreditCard_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/AssetCreditCards/searchexact/{search}')

    def AssetCreditCard_GetById(self, id):
        return self.ApiClient.getAPI(f'/AssetCreditCards/{id}')

    def AssetHistoryByMonths_Get(self):
        return self.ApiClient.getAPI(f'/assetHistoryByMonths')

    def AssetHistoryByMonths_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetHistoryByMonths')

    def AssetHistoryByMonths_Search(self, search):
        return self.ApiClient.getAPI(f'/assetHistoryByMonths/search/{search}')

    def AssetHistoryByMonths_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetHistoryByMonths/searchexact/{search}')

    def AssetHistoryByMonths_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetHistoryByMonths/{id}')

    def AssetMakes_Get(self):
        return self.ApiClient.getAPI(f'/assetMakes')

    def AssetMakes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetMakes')

    def AssetMakes_Search(self, search):
        return self.ApiClient.getAPI(f'/assetMakes/search/{search}')

    def AssetMakes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetMakes/searchexact/{search}')

    def AssetMakes_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetMakes/{id}')

    def AssetManufacturers_Get(self):
        return self.ApiClient.getAPI(f'/assetManufacturers')

    def AssetManufacturers_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetManufacturers')

    def AssetManufacturers_Search(self, search):
        return self.ApiClient.getAPI(f'/assetManufacturers/search/{search}')

    def AssetManufacturers_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetManufacturers/searchexact/{search}')

    def AssetManufacturers_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetManufacturers/{id}')

    def AssetModels_Get(self):
        return self.ApiClient.getAPI(f'/assetModels')

    def AssetModels_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetModels')

    def AssetModels_Search(self, search):
        return self.ApiClient.getAPI(f'/assetModels/search/{search}')

    def AssetModels_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetModels/searchexact/{search}')

    def AssetModels_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetModels/{id}')

    def AssetPartIssues_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetpartissues/bulk')

    def AssetPartIssues_CollectionWithResults(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetpartissues/bulk/returnresults')

    def AssetPartIssues_Get(self):
        return self.ApiClient.getAPI(f'/assetpartissues')

    def AssetPartIssues_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetpartissues')

    def AssetPartIssues_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/assetpartissues')

    def AssetPartIssues_Search(self, search):
        return self.ApiClient.getAPI(f'/assetpartissues/search/{search}')

    def AssetPartIssues_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetpartissues/searchexact/{search}')

    def AssetPartIssues_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetpartissues/{id}')

    def AssetPartsUsed_ForTechSpec(self, techSpecId):
        return self.ApiClient.getAPI(f'/assetpartsused/fortechspec/{techSpecId}')

    def AssetPartsUsed_Get(self):
        return self.ApiClient.getAPI(f'/assetpartsused')

    def AssetPartsUsed_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetpartsused')

    def AssetPartsUsed_Search(self, search):
        return self.ApiClient.getAPI(f'/assetpartsused/search/{search}')

    def AssetPartsUsed_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetpartsused/searchexact/{search}')

    def AssetPartsUsed_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetpartsused/{id}')

    def AssetPmInspections_Get(self):
        return self.ApiClient.getAPI(f'/assetPmInspections')

    def AssetPmInspections_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetPmInspections')

    def AssetPmInspections_Search(self, search):
        return self.ApiClient.getAPI(f'/assetPmInspections/search/{search}')

    def AssetPmInspections_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetPmInspections/searchexact/{search}')

    def AssetPmInspections_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetPmInspections/{id}')

    def AssetPmServices_Get(self):
        return self.ApiClient.getAPI(f'/assetPmServices')

    def AssetPmServices_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetPmServices')

    def AssetPmServices_Search(self, search):
        return self.ApiClient.getAPI(f'/assetPmServices/search/{search}')

    def AssetPmServices_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetPmServices/searchexact/{search}')

    def AssetPmServices_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetPmServices/{id}')

    def AssetPosition_Get(self):
        return self.ApiClient.getAPI(f'/assetpositions')

    def AssetPosition_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetpositions')

    def AssetPosition_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/assetpositions')

    def AssetPosition_GetByAsset(self, assetId):
        return self.ApiClient.getAPI(f'/assetpositions/assetid/{assetId}')

    def AssetPosition_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetpositions/bulk')

    def AssetPosition_Search(self, search):
        return self.ApiClient.getAPI(f'/assetpositions/search/{search}')

    def AssetPosition_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetpositions/searchexact/{search}')

    def AssetPosition_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetpositions/{id}')

    def AssetProductIssues_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetproductissues/bulk')

    def AssetProductIssues_Delete(self):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/assetproductissues')

    def AssetProductIssues_Get(self):
        return self.ApiClient.getAPI(f'/assetproductissues')

    def AssetProductIssues_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetproductissues')

    def AssetProductIssues_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/assetproductissues')

    def AssetProductIssues_DeleteById(self, id):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/assetproductissues/{id}')

    def AssetProductIssues_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetproductissues/{id}')

    def AssetProductIssues_Search(self, search):
        return self.ApiClient.getAPI(f'/assetproductissues/search/{search}')

    def AssetProductIssues_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetproductissues/searchexact/{search}')

    def AssetProductIssues_LovSearch(self, search):
        return self.ApiClient.getAPI(f'/assetproductissues/lov/{search}')

    def AssetProducts_PostCollection(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetProducts/bulk')

    def AssetProducts_PutCollection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/assetProducts/bulk')

    def AssetProducts_Get(self):
        return self.ApiClient.getAPI(f'/assetProducts')

    def AssetProducts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetProducts')

    def AssetProducts_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/assetProducts')

    def AssetProducts_Search(self, search):
        return self.ApiClient.getAPI(f'/assetProducts/search/{search}')

    def AssetProducts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetProducts/searchexact/{search}')

    def AssetProducts_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetProducts/{id}')

    def AssetRelationships_Get(self):
        return self.ApiClient.getAPI(f'/assetRelationships')

    def AssetRelationships_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetRelationships')

    def AssetRelationships_Search(self, search):
        return self.ApiClient.getAPI(f'/assetRelationships/search/{search}')

    def AssetRelationships_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetRelationships/searchexact/{search}')

    def AssetRelationships_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetRelationships/{id}')

    def AssetScheduledServices_Get(self):
        return self.ApiClient.getAPI(f'/assetScheduledServices')

    def AssetScheduledServices_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetScheduledServices')

    def AssetScheduledServices_Search(self, search):
        return self.ApiClient.getAPI(f'/assetScheduledServices/search/{search}')

    def AssetScheduledServices_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetScheduledServices/searchexact/{search}')

    def AssetScheduledServices_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetScheduledServices/{id}')

    def Assets_Get(self):
        return self.ApiClient.getAPI(f'/assets')

    def Assets_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assets')

    def Assets_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/assets')

    def Assets_UpdateMeters(self, assetId):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/assets/{assetId}/updatemeters')

    def Assets_PMServicesDue(self, assetId):
        return self.ApiClient.getAPI(f'/assets/{assetId}/pmservicesdue')

    def Assets_TestTypes(self, assetId):
        return self.ApiClient.getAPI(f'/assets/{assetId}/testtypes')

    def Assets_GetPartReserves(self, assetId):
        return self.ApiClient.getAPI(f'/assets/{assetId}/partreserves')

    def Assets_DashboardSearch(self, search):
        return self.ApiClient.getAPI(f'/assets/dashboardsearch/{search}')

    def Assets_DashboardSearchForLocation(self, search, locationId):
        return self.ApiClient.getAPI(f'/assets/dashboardsearch/{search}/forlocation/{locationId}')

    def Assets_DashboardSearchExact(self, search):
        return self.ApiClient.getAPI(f'/assets/dashboardsearchexact/{search}')

    def Assets_OrderSearch(self, search):
        return self.ApiClient.getAPI(f'/assets/withorders/search/{search}')

    def Assets_OrderSearchExact(self, search):
        return self.ApiClient.getAPI(f'/assets/withorders/searchexact/{search}')

    def Assets_Collection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/assets/bulk')

    def Assets_Search(self, search):
        return self.ApiClient.getAPI(f'/assets/search/{search}')

    def Assets_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assets/searchexact/{search}')

    def Assets_GetById(self, id):
        return self.ApiClient.getAPI(f'/assets/{id}')

    def AssetServicesDue_Get(self):
        return self.ApiClient.getAPI(f'/assetServicesDue')

    def AssetServicesDue_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetServicesDue')

    def AssetServicesDue_Search(self, search):
        return self.ApiClient.getAPI(f'/assetServicesDue/search/{search}')

    def AssetServicesDue_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetServicesDue/searchexact/{search}')

    def AssetServicesDue_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetServicesDue/{id}')

    def AssetTypes_Get(self):
        return self.ApiClient.getAPI(f'/assetTypes')

    def AssetTypes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetTypes')

    def AssetTypes_Search(self, search):
        return self.ApiClient.getAPI(f'/assetTypes/search/{search}')

    def AssetTypes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetTypes/searchexact/{search}')

    def AssetTypes_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetTypes/{id}')

    def AssetWarranties_Get(self):
        return self.ApiClient.getAPI(f'/assetWarranties')

    def AssetWarranties_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetWarranties')

    def AssetWarranties_Search(self, search):
        return self.ApiClient.getAPI(f'/assetWarranties/search/{search}')

    def AssetWarranties_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetWarranties/searchexact/{search}')

    def AssetWarranties_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetWarranties/{id}')

    def AssetWarrantyParts_Get(self):
        return self.ApiClient.getAPI(f'/assetWarrantyParts')

    def AssetWarrantyParts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/assetWarrantyParts')

    def AssetWarrantyParts_Search(self, search):
        return self.ApiClient.getAPI(f'/assetWarrantyParts/search/{search}')

    def AssetWarrantyParts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/assetWarrantyParts/searchexact/{search}')

    def AssetWarrantyParts_GetById(self, id):
        return self.ApiClient.getAPI(f'/assetWarrantyParts/{id}')

    def Attachments_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/attachments/bulk')

    def Attachments_PostBulk(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/attachments/bulk')

    def Attachments_GetContent(self, filepath):
        return self.ApiClient.getAPI(f'/attachments/content/{filepath}')

    def Attachments_Delete(self):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/attachments')

    def Attachments_Get(self):
        return self.ApiClient.getAPI(f'/attachments')

    def Attachments_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/attachments')

    def Attachments_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/attachments')

    def Attachments_DeleteById(self, id):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/attachments/{id}')

    def Attachments_GetById(self, id):
        return self.ApiClient.getAPI(f'/attachments/{id}')

    def Attachments_Search(self, search):
        return self.ApiClient.getAPI(f'/attachments/search/{search}')

    def Attachments_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/attachments/searchexact/{search}')

    def Attachments_LovSearch(self, search):
        return self.ApiClient.getAPI(f'/attachments/lov/{search}')

    def Availabilities_Get(self):
        return self.ApiClient.getAPI(f'/availabilities')

    def Availabilities_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/availabilities')

    def Availabilities_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/availabilities')

    def Availabilities_Search(self, search):
        return self.ApiClient.getAPI(f'/availabilities/search/{search}')

    def Availabilities_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/availabilities/searchexact/{search}')

    def Availabilities_GetById(self, id):
        return self.ApiClient.getAPI(f'/availabilities/{id}')

    def Billings_Get(self):
        return self.ApiClient.getAPI(f'/billings')

    def Billings_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/billings')

    def Billings_GetById(self, id):
        return self.ApiClient.getAPI(f'/billings/{id}')

    def ChangeLogs_GetForSWC(self, screen, window, control, keyvalue):
        return self.ApiClient.getAPI(f'/changelogs/FAcontrol/{screen}/{window}/{control}/{keyvalue}')

    def ChangeLogs_GetForTCK(self, tablename, columnname, keyvalue):
        return self.ApiClient.getAPI(f'/changelogs/DBcolumn/{tablename}/{columnname}/{keyvalue}')

    def ChangeLogs_Get(self):
        return self.ApiClient.getAPI(f'/changelogs')

    def ChangeLogs_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/changelogs')

    def ChangeLogs_GetById(self, id):
        return self.ApiClient.getAPI(f'/changelogs/{id}')

    def ConditionRatings_Get(self):
        return self.ApiClient.getAPI(f'/conditionRatings')

    def ConditionRatings_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/conditionRatings')

    def ConditionRatings_Search(self, search):
        return self.ApiClient.getAPI(f'/conditionRatings/search/{search}')

    def ConditionRatings_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/conditionRatings/searchexact/{search}')

    def ConditionRatings_GetById(self, id):
        return self.ApiClient.getAPI(f'/conditionRatings/{id}')

    def CoreClaims_Get(self):
        return self.ApiClient.getAPI(f'/coreclaims')

    def CoreClaims_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/coreclaims')

    def CoreClaims_Search(self, search):
        return self.ApiClient.getAPI(f'/coreclaims/search/{search}')

    def CoreClaims_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/coreclaims/searchexact/{search}')

    def CoreClaims_GetById(self, id):
        return self.ApiClient.getAPI(f'/coreclaims/{id}')

    def CoreTrackings_Get(self):
        return self.ApiClient.getAPI(f'/coretrackings')

    def CoreTrackings_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/coretrackings')

    def CoreTrackings_Search(self, search):
        return self.ApiClient.getAPI(f'/coretrackings/search/{search}')

    def CoreTrackings_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/coretrackings/searchexact/{search}')

    def CoreTrackings_GetById(self, id):
        return self.ApiClient.getAPI(f'/coretrackings/{id}')

    def CurrentJobStatuses_Get(self):
        return self.ApiClient.getAPI(f'/currentJobStatuses')

    def CurrentJobStatuses_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/currentJobStatuses')

    def CurrentJobStatuses_Search(self, search):
        return self.ApiClient.getAPI(f'/currentJobStatuses/search/{search}')

    def CurrentJobStatuses_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/currentJobStatuses/searchexact/{search}')

    def CurrentJobStatuses_GetById(self, id):
        return self.ApiClient.getAPI(f'/currentJobStatuses/{id}')

    def DepartmentAttributes_Get(self):
        return self.ApiClient.getAPI(f'/departmentAttributes')

    def DepartmentAttributes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/departmentAttributes')

    def DepartmentAttributes_Search(self, search):
        return self.ApiClient.getAPI(f'/departmentAttributes/search/{search}')

    def DepartmentAttributes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/departmentAttributes/searchexact/{search}')

    def DepartmentAttributes_GetById(self, id):
        return self.ApiClient.getAPI(f'/departmentAttributes/{id}')

    def DepartmentOrgLevels_Get(self):
        return self.ApiClient.getAPI(f'/departmentOrgLevels')

    def DepartmentOrgLevels_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/departmentOrgLevels')

    def DepartmentOrgLevels_Search(self, search):
        return self.ApiClient.getAPI(f'/departmentOrgLevels/search/{search}')

    def DepartmentOrgLevels_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/departmentOrgLevels/searchexact/{search}')

    def DepartmentOrgLevels_GetById(self, id):
        return self.ApiClient.getAPI(f'/departmentOrgLevels/{id}')

    def DepartmentPartIssues_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/departmentPartIssues/bulk')

    def DepartmentPartIssues_Get(self):
        return self.ApiClient.getAPI(f'/departmentPartIssues')

    def DepartmentPartIssues_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/departmentPartIssues')

    def DepartmentPartIssues_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/departmentPartIssues')

    def DepartmentPartIssues_Search(self, search):
        return self.ApiClient.getAPI(f'/departmentPartIssues/search/{search}')

    def DepartmentPartIssues_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/departmentPartIssues/searchexact/{search}')

    def DepartmentPartIssues_GetById(self, id):
        return self.ApiClient.getAPI(f'/departmentPartIssues/{id}')

    def DepartmentRequisitions_Get(self):
        return self.ApiClient.getAPI(f'/departmentRequisitions')

    def DepartmentRequisitions_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/departmentRequisitions')

    def DepartmentRequisitions_Search(self, search):
        return self.ApiClient.getAPI(f'/departmentRequisitions/search/{search}')

    def DepartmentRequisitions_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/departmentRequisitions/searchexact/{search}')

    def DepartmentRequisitions_GetById(self, id):
        return self.ApiClient.getAPI(f'/departmentRequisitions/{id}')

    def Departments_Get(self):
        return self.ApiClient.getAPI(f'/departments')

    def Departments_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/departments')

    def Departments_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/departments')

    def Departments_GetHierarchy(self, departmentId):
        return self.ApiClient.getAPI(f'/departments/{departmentId}/hierarchy')

    def Departments_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/departments/bulk')

    def Departments_Update(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/departments/bulk')

    def Departments_Search(self, search):
        return self.ApiClient.getAPI(f'/departments/search/{search}')

    def Departments_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/departments/searchexact/{search}')

    def Departments_GetById(self, id):
        return self.ApiClient.getAPI(f'/departments/{id}')

    def EmployeeAttributes_CreatePost(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/employeeAttributes/bulk')

    def EmployeeAttributes_CreatePut(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/employeeAttributes/bulk')

    def EmployeeAttributes_Get(self):
        return self.ApiClient.getAPI(f'/employeeAttributes')

    def EmployeeAttributes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/employeeAttributes')

    def EmployeeAttributes_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/employeeAttributes')

    def EmployeeAttributes_Search(self, search):
        return self.ApiClient.getAPI(f'/employeeAttributes/search/{search}')

    def EmployeeAttributes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/employeeAttributes/searchexact/{search}')

    def EmployeeAttributes_GetById(self, id):
        return self.ApiClient.getAPI(f'/employeeAttributes/{id}')

    def EmployeeClockIn_Get(self):
        return self.ApiClient.getAPI(f'/employeeClockIn')

    def EmployeeClockIn_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/employeeClockIn')

    def EmployeeClockIn_GetById(self, id):
        return self.ApiClient.getAPI(f'/employeeClockIn/{id}')

    def EmployeeProducts_PostCollection(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/employeeProducts/bulk')

    def EmployeeProducts_PutCollection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/employeeProducts/bulk')

    def EmployeeProducts_Get(self):
        return self.ApiClient.getAPI(f'/employeeProducts')

    def EmployeeProducts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/employeeProducts')

    def EmployeeProducts_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/employeeProducts')

    def EmployeeProducts_Search(self, search):
        return self.ApiClient.getAPI(f'/employeeProducts/search/{search}')

    def EmployeeProducts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/employeeProducts/searchexact/{search}')

    def EmployeeProducts_GetById(self, id):
        return self.ApiClient.getAPI(f'/employeeProducts/{id}')

    def Employees_GetCurrentTask(self, employeeId):
        return self.ApiClient.getAPI(f'/employees/{employeeId}/currenttask')

    def Employees_GetActiveWorkAssignments(self, employeeId):
        return self.ApiClient.getAPI(f'/employees/{employeeId}/taskassignments')

    def Employees_StopTask(self, employeeId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/employees/{employeeId}/stoptask')

    def Employees_StartTask(self, employeeId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/employees/{employeeId}/starttask')

    def Employees_Renumber(self, employeeId, newId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/employees/{employeeId}/renumberto/{newId}')

    def Employees_GetCurrentJobStatus(self, employeeId):
        return self.ApiClient.getAPI(f'/employees/{employeeId}/currentjobstatus')

    def Employees_GetSubordinateStatus(self, supervisorId):
        return self.ApiClient.getAPI(f'/employees/{supervisorId}/subordinatestatus')

    def Employees_GetUnassignedTasks(self, supervisorId):
        return self.ApiClient.getAPI(f'/employees/{supervisorId}/unassignedtasks')

    def Employees_GetAllWorkOrders(self, employeeId):
        return self.ApiClient.getAPI(f'/employees/{employeeId}/allworkorders')

    def Employees_GetMaintenanceLocations(self, employeeId):
        return self.ApiClient.getAPI(f'/employees/{employeeId}/maintenancelocations')

    def Employees_GetStockLocations(self, employeeId):
        return self.ApiClient.getAPI(f'/employees/{employeeId}/stocklocations')

    def Employees_GetEmployeeMediaFile(self, employeeId):
        return self.ApiClient.getAPI(f'/employees/{employeeId}/mediafile')

    def Employees_GetClockIns(self, employeeId):
        return self.ApiClient.getAPI(f'/employees/{employeeId}/clockins')

    def Employees_ClockIn(self, employeeId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/employees/{employeeId}/clockin')

    def Employees_ClockOut(self, employeeId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/employees/{employeeId}/clockout')

    def Employees_GetCompletedWorkOrders(self, supervisorId):
        return self.ApiClient.getAPI(f'/employees/{supervisorId}/completedworkorders')

    def Employees_GetOpenWorkOrders(self, supervisorId):
        return self.ApiClient.getAPI(f'/employees/{supervisorId}/openworkorders')

    def Employees_GetActiveServiceRequests(self, supervisorId):
        return self.ApiClient.getAPI(f'/employees/{supervisorId}/activeservicerequests')

    def Employees_Delete(self):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/employees')

    def Employees_Get(self):
        return self.ApiClient.getAPI(f'/employees')

    def Employees_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/employees')

    def Employees_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/employees')

    def Employees_DeleteById(self, id):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/employees/{id}')

    def Employees_GetById(self, id):
        return self.ApiClient.getAPI(f'/employees/{id}')

    def Employees_Search(self, search):
        return self.ApiClient.getAPI(f'/employees/search/{search}')

    def Employees_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/employees/searchexact/{search}')

    def Employees_LovSearch(self, search):
        return self.ApiClient.getAPI(f'/employees/lov/{search}')

    def FailureCodes_Get(self):
        return self.ApiClient.getAPI(f'/failureCodes')

    def FailureCodes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/failureCodes')

    def FailureCodes_Search(self, search):
        return self.ApiClient.getAPI(f'/failureCodes/search/{search}')

    def FailureCodes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/failureCodes/searchexact/{search}')

    def FailureCodes_GetById(self, id):
        return self.ApiClient.getAPI(f'/failureCodes/{id}')

    def Faults_Get(self):
        return self.ApiClient.getAPI(f'/faults')

    def Faults_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/faults')

    def Faults_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/faults')

    def Faults_Delete(self):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/faults')

    def Faults_Collection(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/faults/bulk')

    def Faults_PutCollection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/faults/bulk')

    def Faults_AddServiceRequest(self, faultId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/faults/{faultId}/addsr')

    def Faults_DeleteById(self, id):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/faults/{id}')

    def Faults_GetById(self, id):
        return self.ApiClient.getAPI(f'/faults/{id}')

    def Faults_Search(self, search):
        return self.ApiClient.getAPI(f'/faults/search/{search}')

    def Faults_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/faults/searchexact/{search}')

    def Faults_LovSearch(self, search):
        return self.ApiClient.getAPI(f'/faults/lov/{search}')

    def FluidHoses_Get(self):
        return self.ApiClient.getAPI(f'/fluidHoses')

    def FluidHoses_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/fluidHoses')

    def FluidHoses_Search(self, search):
        return self.ApiClient.getAPI(f'/fluidHoses/search/{search}')

    def FluidHoses_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/fluidHoses/searchexact/{search}')

    def FluidHoses_GetById(self, id):
        return self.ApiClient.getAPI(f'/fluidHoses/{id}')

    def FuelCards_CreatePost(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/fuelCards/bulk')

    def FuelCards_CreatePut(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/fuelCards/bulk')

    def FuelCards_Get(self):
        return self.ApiClient.getAPI(f'/fuelCards')

    def FuelCards_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/fuelCards')

    def FuelCards_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/fuelCards')

    def FuelCards_Search(self, search):
        return self.ApiClient.getAPI(f'/fuelCards/search/{search}')

    def FuelCards_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/fuelCards/searchexact/{search}')

    def FuelCards_GetById(self, id):
        return self.ApiClient.getAPI(f'/fuelCards/{id}')

    def IndirectCodes_GetIndirectCodesForLocation(self, locationId):
        return self.ApiClient.getAPI(f'/indirectcodes/forlocation/{locationId}')

    def IndirectCodes_Get(self):
        return self.ApiClient.getAPI(f'/indirectcodes')

    def IndirectCodes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/indirectcodes')

    def IndirectCodes_Search(self, search):
        return self.ApiClient.getAPI(f'/indirectcodes/search/{search}')

    def IndirectCodes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/indirectcodes/searchexact/{search}')

    def IndirectCodes_GetById(self, id):
        return self.ApiClient.getAPI(f'/indirectcodes/{id}')

    def IndirectPartIssues_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/indirectPartIssues/bulk')

    def IndirectPartIssues_CollectionWithResults(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/indirectPartIssues/bulk/returnresults')

    def IndirectPartIssues_Get(self):
        return self.ApiClient.getAPI(f'/indirectPartIssues')

    def IndirectPartIssues_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/indirectPartIssues')

    def IndirectPartIssues_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/indirectPartIssues')

    def IndirectPartIssues_Search(self, search):
        return self.ApiClient.getAPI(f'/indirectPartIssues/search/{search}')

    def IndirectPartIssues_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/indirectPartIssues/searchexact/{search}')

    def IndirectPartIssues_GetById(self, id):
        return self.ApiClient.getAPI(f'/indirectPartIssues/{id}')

    def InventoryCountItems_SearchForBins(self, inventoryCountId, search):
        return self.ApiClient.getAPI(f'/inventorycountitems/{inventoryCountId}/searchforbins/{search}')

    def InventoryCountItems_SearchExactForBins(self, inventoryCountId, search):
        return self.ApiClient.getAPI(f'/inventorycountitems/{inventoryCountId}/searchexactforbins/{search}')

    def InventoryCountItems_Get(self):
        return self.ApiClient.getAPI(f'/inventorycountitems')

    def InventoryCountItems_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/inventorycountitems')

    def InventoryCountItems_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/inventorycountitems')

    def InventoryCountItems_Search(self, search):
        return self.ApiClient.getAPI(f'/inventorycountitems/search/{search}')

    def InventoryCountItems_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/inventorycountitems/searchexact/{search}')

    def InventoryCountItems_GetById(self, id):
        return self.ApiClient.getAPI(f'/inventorycountitems/{id}')

    def InventoryCounts_Complete(self, inventoryCountId):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/inventorycounts/{inventoryCountId}/complete')

    def InventoryCounts_GetVariances(self, inventoryCountId):
        return self.ApiClient.getAPI(f'/inventorycounts/{inventoryCountId}/variances')

    def InventoryCounts_Get(self):
        return self.ApiClient.getAPI(f'/inventorycounts')

    def InventoryCounts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/inventorycounts')

    def InventoryCounts_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/inventorycounts')

    def InventoryCounts_Search(self, search):
        return self.ApiClient.getAPI(f'/inventorycounts/search/{search}')

    def InventoryCounts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/inventorycounts/searchexact/{search}')

    def InventoryCounts_GetById(self, id):
        return self.ApiClient.getAPI(f'/inventorycounts/{id}')

    def InvoiceReconciliationLine_PutCollection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/invoicereconciliationlines/bulk')

    def InvoiceReconciliationLine_Collection(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/invoicereconciliationlines/bulk')

    def InvoiceReconciliationLine_Get(self):
        return self.ApiClient.getAPI(f'/invoicereconciliationlines')

    def InvoiceReconciliationLine_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/invoicereconciliationlines')

    def InvoiceReconciliationLine_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/invoicereconciliationlines')

    def InvoiceReconciliationLine_Search(self, search):
        return self.ApiClient.getAPI(f'/invoicereconciliationlines/search/{search}')

    def InvoiceReconciliationLine_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/invoicereconciliationlines/searchexact/{search}')

    def InvoiceReconciliationLine_GetById(self, id):
        return self.ApiClient.getAPI(f'/invoicereconciliationlines/{id}')

    def InvoiceReconciliations_PostCollection(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/invoicereconciliations/bulk')

    def InvoiceReconciliations_PutCollection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/invoicereconciliations/bulk')

    def InvoiceReconciliations_Delete(self):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/invoicereconciliations')

    def InvoiceReconciliations_Get(self):
        return self.ApiClient.getAPI(f'/invoicereconciliations')

    def InvoiceReconciliations_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/invoicereconciliations')

    def InvoiceReconciliations_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/invoicereconciliations')

    def InvoiceReconciliations_Reconcile(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/invoicereconciliations/reconcile')

    def InvoiceReconciliations_UnReconcile(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/invoicereconciliations/unreconcile')

    def InvoiceReconciliations_Search(self, search):
        return self.ApiClient.getAPI(f'/invoicereconciliations/search/{search}')

    def InvoiceReconciliations_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/invoicereconciliations/searchexact/{search}')

    def InvoiceReconciliations_GetById(self, id):
        return self.ApiClient.getAPI(f'/invoicereconciliations/{id}')

    def LifeCycleStatuses_Get(self):
        return self.ApiClient.getAPI(f'/lifecyclestatuses')

    def LifeCycleStatuses_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/lifecyclestatuses')

    def LifeCycleStatuses_Search(self, search):
        return self.ApiClient.getAPI(f'/lifecyclestatuses/search/{search}')

    def LifeCycleStatuses_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/lifecyclestatuses/searchexact/{search}')

    def LifeCycleStatuses_GetById(self, id):
        return self.ApiClient.getAPI(f'/lifecyclestatuses/{id}')

    def LocationAttributes_CreatePost(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/locationAttributes/bulk')

    def LocationAttributes_CreatePut(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/locationAttributes/bulk')

    def LocationAttributes_Get(self):
        return self.ApiClient.getAPI(f'/locationAttributes')

    def LocationAttributes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/locationAttributes')

    def LocationAttributes_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/locationAttributes')

    def LocationAttributes_Search(self, search):
        return self.ApiClient.getAPI(f'/locationAttributes/search/{search}')

    def LocationAttributes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/locationAttributes/searchexact/{search}')

    def LocationAttributes_GetById(self, id):
        return self.ApiClient.getAPI(f'/locationAttributes/{id}')

    def LocationParts_GetTechSpecPartsUsed(self, techSpecId):
        return self.ApiClient.getAPI(f'/locationparts/fortechspec/{techSpecId}')

    def LocationParts_GetTechSpecStandardParts(self, standardsclass, task):
        return self.ApiClient.getAPI(f'/locationparts/forstandardsclass/{standardsclass}/fortask/{task}')

    def LocationParts_GetTechSpecTaskPartsUsed(self, locationId, techSpecId, taskId):
        return self.ApiClient.getAPI(f'/locationparts/{locationId}/fortechspec/{techSpecId}/fortask/{taskId}')

    def LocationParts_GetAssetTaskPartsUsed(self, locationId, assetId, taskId):
        return self.ApiClient.getAPI(f'/locationparts/{locationId}/forasset/{assetId}/fortask/{taskId}')

    def LocationParts_GetStandardsClassTaskParts(self, locationId, standardsClassId, taskId):
        return self.ApiClient.getAPI(f'/locationparts/{locationId}/forstandardsclass/{standardsClassId}/fortask/{taskId}')

    def LocationParts_Search(self, search):
        return self.ApiClient.getAPI(f'/locationparts/search/{search}')

    def LocationParts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/locationparts/searchexact/{search}')

    def LocationParts_OrderLineSearch(self, locationId, search):
        return self.ApiClient.getAPI(f'/locationparts/{locationId}/onorder/search/{search}')

    def LocationParts_OrderLineSearchExact(self, locationId, search):
        return self.ApiClient.getAPI(f'/locationparts/{locationId}/onorder/searchexact/{search}')

    def LocationParts_NotOnOrderSearch(self, locationId, search):
        return self.ApiClient.getAPI(f'/locationparts/{locationId}/notonorder/search/{search}')

    def LocationParts_NotOnOrderSearchExact(self, locationId, search):
        return self.ApiClient.getAPI(f'/locationparts/{locationId}/notonorder/searchexact/{search}')

    def LocationParts_TaskSearch(self, taskId, search):
        return self.ApiClient.getAPI(f'/locationparts/fortask/{taskId}/search/{search}')

    def LocationParts_TaskSearchExact(self, taskId, search):
        return self.ApiClient.getAPI(f'/locationparts/fortask/{taskId}/searchexact/{search}')

    def LocationParts_CreatePostCollection(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/locationparts/bulk')

    def LocationParts_CreatePutCollection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/locationparts/bulk')

    def LocationParts_Get(self):
        return self.ApiClient.getAPI(f'/locationparts')

    def LocationParts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/locationparts')

    def LocationParts_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/locationparts')

    def LocationParts_GetById(self, id):
        return self.ApiClient.getAPI(f'/locationparts/{id}')

    def Locations_Get(self):
        return self.ApiClient.getAPI(f'/locations')

    def Locations_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/locations')

    def Locations_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/locations')

    def Locations_Search(self, search):
        return self.ApiClient.getAPI(f'/locations/search/{search}')

    def Locations_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/locations/searchexact/{search}')

    def Locations_GetById(self, id):
        return self.ApiClient.getAPI(f'/locations/{id}')

    def Notes_Get(self):
        return self.ApiClient.getAPI(f'/notes')

    def Notes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/notes')

    def Notes_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/notes')

    def Notes_Search(self, search):
        return self.ApiClient.getAPI(f'/notes/search/{search}')

    def Notes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/notes/searchexact/{search}')

    def Notes_GetById(self, id):
        return self.ApiClient.getAPI(f'/notes/{id}')

    def OperationalClasses_Get(self):
        return self.ApiClient.getAPI(f'/operationalClasses')

    def OperationalClasses_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/operationalClasses')

    def OperationalClasses_Search(self, search):
        return self.ApiClient.getAPI(f'/operationalClasses/search/{search}')

    def OperationalClasses_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/operationalClasses/searchexact/{search}')

    def OperationalClasses_GetById(self, id):
        return self.ApiClient.getAPI(f'/operationalClasses/{id}')

    def OperationalEntities_Get(self):
        return self.ApiClient.getAPI(f'/operationalEntities')

    def OperationalEntities_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/operationalEntities')

    def OperationalEntities_Search(self, search):
        return self.ApiClient.getAPI(f'/operationalEntities/search/{search}')

    def OperationalEntities_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/operationalEntities/searchexact/{search}')

    def OperationalEntities_GetById(self, id):
        return self.ApiClient.getAPI(f'/operationalEntities/{id}')

    def OperationalStatuses_Get(self):
        return self.ApiClient.getAPI(f'/operationalStatuses')

    def OperationalStatuses_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/operationalStatuses')

    def OperationalStatuses_Search(self, search):
        return self.ApiClient.getAPI(f'/operationalStatuses/search/{search}')

    def OperationalStatuses_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/operationalStatuses/searchexact/{search}')

    def OperationalStatuses_GetById(self, id):
        return self.ApiClient.getAPI(f'/operationalStatuses/{id}')

    def Operator_Get(self):
        return self.ApiClient.getAPI(f'/operatordepartments')

    def Operator_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/operatordepartments')

    def Operator_Search(self, search):
        return self.ApiClient.getAPI(f'/operatordepartments/search/{search}')

    def Operator_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/operatordepartments/searchexact/{search}')

    def Operator_GetById(self, id):
        return self.ApiClient.getAPI(f'/operatordepartments/{id}')

    def OperatorCreditCard_BulkPost(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/OperatorCreditCards/bulk')

    def OperatorCreditCard_BulkPut(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/OperatorCreditCards/bulk')

    def OperatorCreditCard_Get(self):
        return self.ApiClient.getAPI(f'/OperatorCreditCards')

    def OperatorCreditCard_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/OperatorCreditCards')

    def OperatorCreditCard_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/OperatorCreditCards')

    def OperatorCreditCard_Search(self, search):
        return self.ApiClient.getAPI(f'/OperatorCreditCards/search/{search}')

    def OperatorCreditCard_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/OperatorCreditCards/searchexact/{search}')

    def OperatorCreditCard_GetById(self, id):
        return self.ApiClient.getAPI(f'/OperatorCreditCards/{id}')

    def Operators_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/operators/bulk')

    def Operators_Update(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/operators/bulk')

    def Operators_Get(self):
        return self.ApiClient.getAPI(f'/operators')

    def Operators_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/operators')

    def Operators_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/operators')

    def Operators_Search(self, search):
        return self.ApiClient.getAPI(f'/operators/search/{search}')

    def Operators_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/operators/searchexact/{search}')

    def Operators_GetById(self, id):
        return self.ApiClient.getAPI(f'/operators/{id}')

    def ParkingSpots_Get(self):
        return self.ApiClient.getAPI(f'/parkingspots')

    def ParkingSpots_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/parkingspots')

    def ParkingSpots_Search(self, search):
        return self.ApiClient.getAPI(f'/parkingspots/search/{search}')

    def ParkingSpots_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/parkingspots/searchexact/{search}')

    def ParkingSpots_GetById(self, id):
        return self.ApiClient.getAPI(f'/parkingspots/{id}')

    def PartAdjustments_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partadjustments')

    def PartAdjustments_Update(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/partadjustments')

    def PartAdjustments_Delete(self):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/partadjustments')

    def PartAdjustments_Get(self):
        return self.ApiClient.getAPI(f'/partadjustments')

    def PartAdjustments_Create2(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partadjustments/bulk')

    def PartAdjustments_DeleteById(self, id):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/partadjustments/{id}')

    def PartAdjustments_GetById(self, id):
        return self.ApiClient.getAPI(f'/partadjustments/{id}')

    def PartAdjustments_Search(self, search):
        return self.ApiClient.getAPI(f'/partadjustments/search/{search}')

    def PartAdjustments_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/partadjustments/searchexact/{search}')

    def PartAdjustments_LovSearch(self, search):
        return self.ApiClient.getAPI(f'/partadjustments/lov/{search}')

    def PartBins_Get(self):
        return self.ApiClient.getAPI(f'/partBins')

    def PartBins_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partBins')

    def PartBins_Search(self, search):
        return self.ApiClient.getAPI(f'/partBins/search/{search}')

    def PartBins_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/partBins/searchexact/{search}')

    def PartBins_GetById(self, id):
        return self.ApiClient.getAPI(f'/partBins/{id}')

    def PartCycles_Get(self):
        return self.ApiClient.getAPI(f'/partCycles')

    def PartCycles_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partCycles')

    def PartCycles_Search(self, search):
        return self.ApiClient.getAPI(f'/partCycles/search/{search}')

    def PartCycles_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/partCycles/searchexact/{search}')

    def PartCycles_GetById(self, id):
        return self.ApiClient.getAPI(f'/partCycles/{id}')

    def PartIssues_Get(self):
        return self.ApiClient.getAPI(f'/partIssues')

    def PartIssues_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partIssues')

    def PartIssues_Search(self, search):
        return self.ApiClient.getAPI(f'/partIssues/search/{search}')

    def PartIssues_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/partIssues/searchexact/{search}')

    def PartIssues_GetById(self, id):
        return self.ApiClient.getAPI(f'/partIssues/{id}')

    def PartManufacturers_Get(self):
        return self.ApiClient.getAPI(f'/partManufacturers')

    def PartManufacturers_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partManufacturers')

    def PartManufacturers_Search(self, search):
        return self.ApiClient.getAPI(f'/partManufacturers/search/{search}')

    def PartManufacturers_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/partManufacturers/searchexact/{search}')

    def PartManufacturers_GetById(self, id):
        return self.ApiClient.getAPI(f'/partManufacturers/{id}')

    def PartReceipts_LastReceiptForVendorAndPart(self, locationId, partSeq):
        return self.ApiClient.getAPI(f'/partreceipts/last/forlocation/{locationId}/forpartseq/{partSeq}')

    def PartReceipts_Collection(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partreceipts/bulk')

    def PartReceipts_CollectionWithBody(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partreceipts/bulk/returnresults')

    def PartReceipts_Get(self):
        return self.ApiClient.getAPI(f'/partreceipts')

    def PartReceipts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partreceipts')

    def PartReceipts_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/partreceipts')

    def PartReceipts_Search(self, search):
        return self.ApiClient.getAPI(f'/partreceipts/search/{search}')

    def PartReceipts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/partreceipts/searchexact/{search}')

    def PartReceipts_GetById(self, id):
        return self.ApiClient.getAPI(f'/partreceipts/{id}')

    def PartRequests_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partrequests/bulk')

    def PartRequests_Cancel(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/partrequests/cancel')

    def PartRequests_Approve(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/partrequests/approve')

    def PartRequests_Issue(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/partrequests/issue')

    def PartRequests_MakeReady(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/partrequests/makeready')

    def PartRequests_AddNote(self, workOrderId, partRequestId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partrequests/{workOrderId}/{partRequestId}/notes')

    def PartRequests_CollectionWithResultsPOST(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partrequests/bulk/returnresults')

    def PartRequests_CollectionWithResultsPUT(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/partrequests/bulk/returnresults')

    def PartRequests_Get(self):
        return self.ApiClient.getAPI(f'/partrequests')

    def PartRequests_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partrequests')

    def PartRequests_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/partrequests')

    def PartRequests_Search(self, search):
        return self.ApiClient.getAPI(f'/partrequests/search/{search}')

    def PartRequests_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/partrequests/searchexact/{search}')

    def PartRequests_GetById(self, id):
        return self.ApiClient.getAPI(f'/partrequests/{id}')

    def PartReturnRequests_PutPartReturnRequest(self, internalId):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/PartReturnRequests/{internalId}')

    def PartReturnRequests_Get(self):
        return self.ApiClient.getAPI(f'/PartReturnRequests')

    def PartReturnRequests_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/PartReturnRequests')

    def PartReturnRequests_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/PartReturnRequests')

    def PartReturnRequests_Search(self, search):
        return self.ApiClient.getAPI(f'/PartReturnRequests/search/{search}')

    def PartReturnRequests_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/PartReturnRequests/searchexact/{search}')

    def PartReturnRequests_GetById(self, id):
        return self.ApiClient.getAPI(f'/PartReturnRequests/{id}')

    def Parts_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/parts/bulk')

    def Parts_Update(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/parts/bulk')

    def Parts_DeleteById(self, partId):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/parts/{partId}')

    def Parts_DeleteByIdAndManufacturer(self, partId, manufacturerId):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/parts/{partId}/manufacturerId/{manufacturerId}')

    def Parts_Get(self):
        return self.ApiClient.getAPI(f'/parts')

    def Parts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/parts')

    def Parts_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/parts')

    def Parts_Search(self, search):
        return self.ApiClient.getAPI(f'/parts/search/{search}')

    def Parts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/parts/searchexact/{search}')

    def Parts_GetById(self, id):
        return self.ApiClient.getAPI(f'/parts/{id}')

    def PartSerialNumbers_Get(self):
        return self.ApiClient.getAPI(f'/partSerialNumbers')

    def PartSerialNumbers_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partSerialNumbers')

    def PartSerialNumbers_Search(self, search):
        return self.ApiClient.getAPI(f'/partSerialNumbers/search/{search}')

    def PartSerialNumbers_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/partSerialNumbers/searchexact/{search}')

    def PartSerialNumbers_GetById(self, id):
        return self.ApiClient.getAPI(f'/partSerialNumbers/{id}')

    def PartTransferLines_Get(self):
        return self.ApiClient.getAPI(f'/partTransferLines')

    def PartTransferLines_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partTransferLines')

    def PartTransferLines_Search(self, search):
        return self.ApiClient.getAPI(f'/partTransferLines/search/{search}')

    def PartTransferLines_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/partTransferLines/searchexact/{search}')

    def PartTransferLines_GetById(self, id):
        return self.ApiClient.getAPI(f'/partTransferLines/{id}')

    def PartWarranties_Get(self):
        return self.ApiClient.getAPI(f'/partWarranties')

    def PartWarranties_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partWarranties')

    def PartWarranties_Search(self, search):
        return self.ApiClient.getAPI(f'/partWarranties/search/{search}')

    def PartWarranties_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/partWarranties/searchexact/{search}')

    def PartWarranties_GetById(self, id):
        return self.ApiClient.getAPI(f'/partWarranties/{id}')

    def PartXrefs_Get(self):
        return self.ApiClient.getAPI(f'/partXrefs')

    def PartXrefs_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/partXrefs')

    def PartXrefs_Search(self, search):
        return self.ApiClient.getAPI(f'/partXrefs/search/{search}')

    def PartXrefs_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/partXrefs/searchexact/{search}')

    def PartXrefs_GetById(self, id):
        return self.ApiClient.getAPI(f'/partXrefs/{id}')

    def PmChecklistItems_Get(self):
        return self.ApiClient.getAPI(f'/pmChecklistItems')

    def PmChecklistItems_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/pmChecklistItems')

    def PmChecklistItems_Search(self, search):
        return self.ApiClient.getAPI(f'/pmChecklistItems/search/{search}')

    def PmChecklistItems_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/pmChecklistItems/searchexact/{search}')

    def PmChecklistItems_GetById(self, id):
        return self.ApiClient.getAPI(f'/pmChecklistItems/{id}')

    def PoolClasses_Get(self):
        return self.ApiClient.getAPI(f'/poolclasses')

    def PoolClasses_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/poolclasses')

    def PoolClasses_Search(self, search):
        return self.ApiClient.getAPI(f'/poolclasses/search/{search}')

    def PoolClasses_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/poolclasses/searchexact/{search}')

    def PoolClasses_GetById(self, id):
        return self.ApiClient.getAPI(f'/poolclasses/{id}')

    def ProductCategories_Get(self):
        return self.ApiClient.getAPI(f'/productCategories')

    def ProductCategories_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/productCategories')

    def ProductCategories_Search(self, search):
        return self.ApiClient.getAPI(f'/productCategories/search/{search}')

    def ProductCategories_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/productCategories/searchexact/{search}')

    def ProductCategories_GetById(self, id):
        return self.ApiClient.getAPI(f'/productCategories/{id}')

    def PurchaseOrderAttributes_CreatePost(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/purchaseOrderAttributes/bulk')

    def PurchaseOrderAttributes_CreatePut(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/purchaseOrderAttributes/bulk')

    def PurchaseOrderAttributes_Get(self):
        return self.ApiClient.getAPI(f'/purchaseOrderAttributes')

    def PurchaseOrderAttributes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/purchaseOrderAttributes')

    def PurchaseOrderAttributes_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/purchaseOrderAttributes')

    def PurchaseOrderAttributes_Search(self, search):
        return self.ApiClient.getAPI(f'/purchaseOrderAttributes/search/{search}')

    def PurchaseOrderAttributes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/purchaseOrderAttributes/searchexact/{search}')

    def PurchaseOrderAttributes_GetById(self, id):
        return self.ApiClient.getAPI(f'/purchaseOrderAttributes/{id}')

    def PurchaseOrderDestinations_Get(self):
        return self.ApiClient.getAPI(f'/purchaseOrderDestinations')

    def PurchaseOrderDestinations_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/purchaseOrderDestinations')

    def PurchaseOrderDestinations_Search(self, search):
        return self.ApiClient.getAPI(f'/purchaseOrderDestinations/search/{search}')

    def PurchaseOrderDestinations_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/purchaseOrderDestinations/searchexact/{search}')

    def PurchaseOrderDestinations_GetById(self, id):
        return self.ApiClient.getAPI(f'/purchaseOrderDestinations/{id}')

    def PurchaseOrderLine_PutCollection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/purchaseorderlines/bulk')

    def PurchaseOrderLine_Collection(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/purchaseorderlines/bulk')

    def PurchaseOrderLine_CancelLine(self, purchaseOrderId, purchaseOrderLine):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/purchaseorderlines/{purchaseOrderId}/{purchaseOrderLine}/cancel')

    def PurchaseOrderLine_Get(self):
        return self.ApiClient.getAPI(f'/purchaseorderlines')

    def PurchaseOrderLine_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/purchaseorderlines')

    def PurchaseOrderLine_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/purchaseorderlines')

    def PurchaseOrderLine_Search(self, search):
        return self.ApiClient.getAPI(f'/purchaseorderlines/search/{search}')

    def PurchaseOrderLine_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/purchaseorderlines/searchexact/{search}')

    def PurchaseOrderLine_GetById(self, id):
        return self.ApiClient.getAPI(f'/purchaseorderlines/{id}')

    def PurchaseOrders_PutCollection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/purchaseorders/bulk')

    def PurchaseOrders_PostCollection(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/purchaseorders/bulk')

    def PurchaseOrders_Cancel(self, purchaseOrderId):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/purchaseorders/{purchaseOrderId}/cancel')

    def PurchaseOrders_Get(self):
        return self.ApiClient.getAPI(f'/purchaseorders')

    def PurchaseOrders_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/purchaseorders')

    def PurchaseOrders_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/purchaseorders')

    def PurchaseOrders_Search(self, search):
        return self.ApiClient.getAPI(f'/purchaseorders/search/{search}')

    def PurchaseOrders_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/purchaseorders/searchexact/{search}')

    def PurchaseOrders_GetById(self, id):
        return self.ApiClient.getAPI(f'/purchaseorders/{id}')

    def PurchaseRequisitionLine_PutCollection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/purchaserequisitionlines/bulk')

    def PurchaseRequisitionLine_Collection(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/purchaserequisitionlines/bulk')

    def PurchaseRequisitionLine_Delete(self):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/purchaserequisitionlines')

    def PurchaseRequisitionLine_Get(self):
        return self.ApiClient.getAPI(f'/purchaserequisitionlines')

    def PurchaseRequisitionLine_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/purchaserequisitionlines')

    def PurchaseRequisitionLine_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/purchaserequisitionlines')

    def PurchaseRequisitionLine_DeleteById(self, id):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/purchaserequisitionlines/{id}')

    def PurchaseRequisitionLine_GetById(self, id):
        return self.ApiClient.getAPI(f'/purchaserequisitionlines/{id}')

    def PurchaseRequisitionLine_Search(self, search):
        return self.ApiClient.getAPI(f'/purchaserequisitionlines/search/{search}')

    def PurchaseRequisitionLine_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/purchaserequisitionlines/searchexact/{search}')

    def PurchaseRequisitionLine_LovSearch(self, search):
        return self.ApiClient.getAPI(f'/purchaserequisitionlines/lov/{search}')

    def PurchaseRequisitions_Collection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/purchaserequisitions/bulk')

    def PurchaseRequisitions_Get(self):
        return self.ApiClient.getAPI(f'/purchaserequisitions')

    def PurchaseRequisitions_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/purchaserequisitions')

    def PurchaseRequisitions_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/purchaserequisitions')

    def PurchaseRequisitions_Search(self, search):
        return self.ApiClient.getAPI(f'/purchaserequisitions/search/{search}')

    def PurchaseRequisitions_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/purchaserequisitions/searchexact/{search}')

    def PurchaseRequisitions_GetById(self, id):
        return self.ApiClient.getAPI(f'/purchaserequisitions/{id}')

    def PushNotifications_MarkAsRead(self, messageId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/messages/{messageId}/read')

    def PushNotifications_MarkAsDelivered(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/messages/MarkMessagesAsDelivered')

    def PushNotifications_GetUnreadMessagesForUserId(self, userId):
        return self.ApiClient.getAPI(f'/messages/{userId}/unread')

    def PushNotifications_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/messages/all')

    def PushNotifications_Users(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/messages/users')

    def PushNotifications_GetActiveUsers(self):
        return self.ApiClient.getAPI(f'/messages/activeusers')

    def PushNotifications_Get(self):
        return self.ApiClient.getAPI(f'/messages')

    def PushNotifications_Post2(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/messages')

    def PushNotifications_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/messages')

    def PushNotifications_Search(self, search):
        return self.ApiClient.getAPI(f'/messages/search/{search}')

    def PushNotifications_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/messages/searchexact/{search}')

    def PushNotifications_GetById(self, id):
        return self.ApiClient.getAPI(f'/messages/{id}')

    def RepairReasons_Get(self):
        return self.ApiClient.getAPI(f'/repairReasons')

    def RepairReasons_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/repairReasons')

    def RepairReasons_Search(self, search):
        return self.ApiClient.getAPI(f'/repairReasons/search/{search}')

    def RepairReasons_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/repairReasons/searchexact/{search}')

    def RepairReasons_GetById(self, id):
        return self.ApiClient.getAPI(f'/repairReasons/{id}')

    def ReportingSources_Get(self):
        return self.ApiClient.getAPI(f'/reportingSources')

    def ReportingSources_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/reportingSources')

    def ReportingSources_Search(self, search):
        return self.ApiClient.getAPI(f'/reportingSources/search/{search}')

    def ReportingSources_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/reportingSources/searchexact/{search}')

    def ReportingSources_GetById(self, id):
        return self.ApiClient.getAPI(f'/reportingSources/{id}')

    def ReturnReasons_Get(self):
        return self.ApiClient.getAPI(f'/returnReasons')

    def ReturnReasons_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/returnReasons')

    def ReturnReasons_Search(self, search):
        return self.ApiClient.getAPI(f'/returnReasons/search/{search}')

    def ReturnReasons_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/returnReasons/searchexact/{search}')

    def ReturnReasons_GetById(self, id):
        return self.ApiClient.getAPI(f'/returnReasons/{id}')

    def Seasons_Get(self):
        return self.ApiClient.getAPI(f'/seasons')

    def Seasons_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/seasons')

    def Seasons_Search(self, search):
        return self.ApiClient.getAPI(f'/seasons/search/{search}')

    def Seasons_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/seasons/searchexact/{search}')

    def Seasons_GetById(self, id):
        return self.ApiClient.getAPI(f'/seasons/{id}')

    def SerialInventoryCountItems_Get(self):
        return self.ApiClient.getAPI(f'/serialinventorycountitems')

    def SerialInventoryCountItems_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/serialinventorycountitems')

    def SerialInventoryCountItems_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/serialinventorycountitems')

    def SerialInventoryCountItems_Search(self, search):
        return self.ApiClient.getAPI(f'/serialinventorycountitems/search/{search}')

    def SerialInventoryCountItems_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/serialinventorycountitems/searchexact/{search}')

    def SerialInventoryCountItems_GetById(self, id):
        return self.ApiClient.getAPI(f'/serialinventorycountitems/{id}')

    def SerialInventoryCounts_Get(self):
        return self.ApiClient.getAPI(f'/serialinventorycounts')

    def SerialInventoryCounts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/serialinventorycounts')

    def SerialInventoryCounts_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/serialinventorycounts')

    def SerialInventoryCounts_Search(self, search):
        return self.ApiClient.getAPI(f'/serialinventorycounts/search/{search}')

    def SerialInventoryCounts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/serialinventorycounts/searchexact/{search}')

    def SerialInventoryCounts_GetById(self, id):
        return self.ApiClient.getAPI(f'/serialinventorycounts/{id}')

    def ServiceRequestParts_Get(self):
        return self.ApiClient.getAPI(f'/serviceRequestParts')

    def ServiceRequestParts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/serviceRequestParts')

    def ServiceRequestParts_Search(self, search):
        return self.ApiClient.getAPI(f'/serviceRequestParts/search/{search}')

    def ServiceRequestParts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/serviceRequestParts/searchexact/{search}')

    def ServiceRequestParts_GetById(self, id):
        return self.ApiClient.getAPI(f'/serviceRequestParts/{id}')

    def ServiceRequests_GetNotes(self, serviceRequestId):
        return self.ApiClient.getAPI(f'/ServiceRequests/{serviceRequestId}/notes')

    def ServiceRequests_AddNote(self, serviceRequestId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/ServiceRequests/{serviceRequestId}/notes')

    def ServiceRequests_Collection(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/ServiceRequests/bulk')

    def ServiceRequests_PutCollection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/ServiceRequests/bulk')

    def ServiceRequests_Get(self):
        return self.ApiClient.getAPI(f'/ServiceRequests')

    def ServiceRequests_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/ServiceRequests')

    def ServiceRequests_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/ServiceRequests')

    def ServiceRequests_Search(self, search):
        return self.ApiClient.getAPI(f'/ServiceRequests/search/{search}')

    def ServiceRequests_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/ServiceRequests/searchexact/{search}')

    def ServiceRequests_GetById(self, id):
        return self.ApiClient.getAPI(f'/ServiceRequests/{id}')

    def ServiceRequestTask_CreatePost(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/ServiceRequestTasks/bulk')

    def ServiceRequestTask_CreatePut(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/ServiceRequestTasks/bulk')

    def ServiceRequestTask_Get(self):
        return self.ApiClient.getAPI(f'/ServiceRequestTasks')

    def ServiceRequestTask_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/ServiceRequestTasks')

    def ServiceRequestTask_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/ServiceRequestTasks')

    def ServiceRequestTask_Search(self, search):
        return self.ApiClient.getAPI(f'/ServiceRequestTasks/search/{search}')

    def ServiceRequestTask_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/ServiceRequestTasks/searchexact/{search}')

    def ServiceRequestTask_GetById(self, id):
        return self.ApiClient.getAPI(f'/ServiceRequestTasks/{id}')

    def ServiceStatuses_Get(self):
        return self.ApiClient.getAPI(f'/serviceStatuses')

    def ServiceStatuses_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/serviceStatuses')

    def ServiceStatuses_Search(self, search):
        return self.ApiClient.getAPI(f'/serviceStatuses/search/{search}')

    def ServiceStatuses_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/serviceStatuses/searchexact/{search}')

    def ServiceStatuses_GetById(self, id):
        return self.ApiClient.getAPI(f'/serviceStatuses/{id}')

    def Settings_GetSettingsForUserGroup(self, userGroupId):
        return self.ApiClient.getAPI(f'/settings/forusergroup/{userGroupId}')

    def Settings_PutSettingForUserGroup(self, userGroupId):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/settings/forusergroup/{userGroupId}')

    def Settings_PutSettingsForUserGroup(self, userGroupId):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/settings/bulk/forusergroup/{userGroupId}')

    def Settings_DeleteSettingsForUserGroup(self, userGroupId):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/settings/bulk/forusergroup/{userGroupId}')

    def Settings_UpdateCollection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/settings/bulk')

    def Settings_GetVersion(self):
        return self.ApiClient.getAPI(f'/settings/getversion')

    def Settings_Get(self):
        return self.ApiClient.getAPI(f'/settings')

    def Settings_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/settings')

    def Settings_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/settings')

    def Settings_Search(self, search):
        return self.ApiClient.getAPI(f'/settings/search/{search}')

    def Settings_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/settings/searchexact/{search}')

    def Settings_GetById(self, id):
        return self.ApiClient.getAPI(f'/settings/{id}')

    def Shifts_GetCurrentShift(self, shiftId):
        return self.ApiClient.getAPI(f'/shifts/{shiftId}/today')

    def Shifts_GetNextShift(self, shiftId):
        return self.ApiClient.getAPI(f'/shifts/{shiftId}/next')

    def Shifts_GetShiftOn(self, shiftId, dayString):
        return self.ApiClient.getAPI(f'/shifts/{shiftId}/on/{dayString}')

    def Shifts_Get(self):
        return self.ApiClient.getAPI(f'/shifts')

    def Shifts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/shifts')

    def Shifts_Search(self, search):
        return self.ApiClient.getAPI(f'/shifts/search/{search}')

    def Shifts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/shifts/searchexact/{search}')

    def Shifts_GetById(self, id):
        return self.ApiClient.getAPI(f'/shifts/{id}')

    def SkillTypes_Get(self):
        return self.ApiClient.getAPI(f'/skillTypes')

    def SkillTypes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/skillTypes')

    def SkillTypes_Search(self, search):
        return self.ApiClient.getAPI(f'/skillTypes/search/{search}')

    def SkillTypes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/skillTypes/searchexact/{search}')

    def SkillTypes_GetById(self, id):
        return self.ApiClient.getAPI(f'/skillTypes/{id}')

    def StandardJobs_Get(self):
        return self.ApiClient.getAPI(f'/standardJobs')

    def StandardJobs_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/standardJobs')

    def StandardJobs_Search(self, search):
        return self.ApiClient.getAPI(f'/standardJobs/search/{search}')

    def StandardJobs_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/standardJobs/searchexact/{search}')

    def StandardJobs_GetById(self, id):
        return self.ApiClient.getAPI(f'/standardJobs/{id}')

    def Symptoms_GetForAsset(self, assetid):
        return self.ApiClient.getAPI(f'/symptoms/forasset/{assetid}')

    def Symptoms_Get(self):
        return self.ApiClient.getAPI(f'/symptoms')

    def Symptoms_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/symptoms')

    def Symptoms_Search(self, search):
        return self.ApiClient.getAPI(f'/symptoms/search/{search}')

    def Symptoms_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/symptoms/searchexact/{search}')

    def Symptoms_GetById(self, id):
        return self.ApiClient.getAPI(f'/symptoms/{id}')

    def TaskCodes_Get(self):
        return self.ApiClient.getAPI(f'/taskCodes')

    def TaskCodes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/taskCodes')

    def TaskCodes_Search(self, search):
        return self.ApiClient.getAPI(f'/taskCodes/search/{search}')

    def TaskCodes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/taskCodes/searchexact/{search}')

    def TaskCodes_GetById(self, id):
        return self.ApiClient.getAPI(f'/taskCodes/{id}')

    def TaskComponents_GetForAsset(self, assetid):
        return self.ApiClient.getAPI(f'/taskComponents/forasset/{assetid}')

    def TaskComponents_SearchByAsset(self, assetid, search):
        return self.ApiClient.getAPI(f'/taskComponents/forasset/{assetid}/search/{search}')

    def TaskComponents_SearchByAssetExact(self, assetid, search):
        return self.ApiClient.getAPI(f'/taskComponents/forasset/{assetid}/searchexact/{search}')

    def TaskComponents_Get(self):
        return self.ApiClient.getAPI(f'/taskComponents')

    def TaskComponents_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/taskComponents')

    def TaskComponents_Search(self, search):
        return self.ApiClient.getAPI(f'/taskComponents/search/{search}')

    def TaskComponents_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/taskComponents/searchexact/{search}')

    def TaskComponents_GetById(self, id):
        return self.ApiClient.getAPI(f'/taskComponents/{id}')

    def TaskReasons_Get(self):
        return self.ApiClient.getAPI(f'/taskReasons')

    def TaskReasons_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/taskReasons')

    def TaskReasons_Search(self, search):
        return self.ApiClient.getAPI(f'/taskReasons/search/{search}')

    def TaskReasons_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/taskReasons/searchexact/{search}')

    def TaskReasons_GetById(self, id):
        return self.ApiClient.getAPI(f'/taskReasons/{id}')

    def TaskStatusCodes_Get(self):
        return self.ApiClient.getAPI(f'/taskStatusCodes')

    def TaskStatusCodes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/taskStatusCodes')

    def TaskStatusCodes_Search(self, search):
        return self.ApiClient.getAPI(f'/taskStatusCodes/search/{search}')

    def TaskStatusCodes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/taskStatusCodes/searchexact/{search}')

    def TaskStatusCodes_GetById(self, id):
        return self.ApiClient.getAPI(f'/taskStatusCodes/{id}')

    def TaskSystems_GetForAsset(self, assetid):
        return self.ApiClient.getAPI(f'/taskSystems/forasset/{assetid}')

    def TaskSystems_SearchByAsset(self, assetid, search):
        return self.ApiClient.getAPI(f'/taskSystems/forasset/{assetid}/search/{search}')

    def TaskSystems_SearchByAssetExact(self, assetid, search):
        return self.ApiClient.getAPI(f'/taskSystems/forasset/{assetid}/searchexact/{search}')

    def TaskSystems_Get(self):
        return self.ApiClient.getAPI(f'/taskSystems')

    def TaskSystems_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/taskSystems')

    def TaskSystems_Search(self, search):
        return self.ApiClient.getAPI(f'/taskSystems/search/{search}')

    def TaskSystems_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/taskSystems/searchexact/{search}')

    def TaskSystems_GetById(self, id):
        return self.ApiClient.getAPI(f'/taskSystems/{id}')

    def TaxSchemes_Get(self):
        return self.ApiClient.getAPI(f'/taxSchemes')

    def TaxSchemes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/taxSchemes')

    def TaxSchemes_Search(self, search):
        return self.ApiClient.getAPI(f'/taxSchemes/search/{search}')

    def TaxSchemes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/taxSchemes/searchexact/{search}')

    def TaxSchemes_GetById(self, id):
        return self.ApiClient.getAPI(f'/taxSchemes/{id}')

    def TechSpecPartsUsed_Get(self):
        return self.ApiClient.getAPI(f'/techSpecPartsUsed')

    def TechSpecPartsUsed_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/techSpecPartsUsed')

    def TechSpecPartsUsed_Search(self, search):
        return self.ApiClient.getAPI(f'/techSpecPartsUsed/search/{search}')

    def TechSpecPartsUsed_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/techSpecPartsUsed/searchexact/{search}')

    def TechSpecPartsUsed_GetById(self, id):
        return self.ApiClient.getAPI(f'/techSpecPartsUsed/{id}')

    def TechSpecs_GetPartsUsed(self, techSpecId):
        return self.ApiClient.getAPI(f'/techspecs/{techSpecId}/partsused')

    def TechSpecs_Get(self):
        return self.ApiClient.getAPI(f'/techspecs')

    def TechSpecs_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/techspecs')

    def TechSpecs_Search(self, search):
        return self.ApiClient.getAPI(f'/techspecs/search/{search}')

    def TechSpecs_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/techspecs/searchexact/{search}')

    def TechSpecs_GetById(self, id):
        return self.ApiClient.getAPI(f'/techspecs/{id}')

    def TechSpecStandardParts_Get(self):
        return self.ApiClient.getAPI(f'/techSpecStandardParts')

    def TechSpecStandardParts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/techSpecStandardParts')

    def TechSpecStandardParts_Search(self, search):
        return self.ApiClient.getAPI(f'/techSpecStandardParts/search/{search}')

    def TechSpecStandardParts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/techSpecStandardParts/searchexact/{search}')

    def TechSpecStandardParts_GetById(self, id):
        return self.ApiClient.getAPI(f'/techSpecStandardParts/{id}')

    def TechSpecStandardTasks_GetForAsset(self, assetid):
        return self.ApiClient.getAPI(f'/techSpecStandardTasks/forasset/{assetid}')

    def TechSpecStandardTasks_SearchByAsset(self, assetid, search):
        return self.ApiClient.getAPI(f'/techSpecStandardTasks/forasset/{assetid}/search/{search}')

    def TechSpecStandardTasks_SearchByAssetExact(self, assetid, search):
        return self.ApiClient.getAPI(f'/techSpecStandardTasks/forasset/{assetid}/searchexact/{search}')

    def TechSpecStandardTasks_Get(self):
        return self.ApiClient.getAPI(f'/techSpecStandardTasks')

    def TechSpecStandardTasks_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/techSpecStandardTasks')

    def TechSpecStandardTasks_Search(self, search):
        return self.ApiClient.getAPI(f'/techSpecStandardTasks/search/{search}')

    def TechSpecStandardTasks_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/techSpecStandardTasks/searchexact/{search}')

    def TechSpecStandardTasks_GetById(self, id):
        return self.ApiClient.getAPI(f'/techSpecStandardTasks/{id}')

    def TestResultLineItems_Get(self):
        return self.ApiClient.getAPI(f'/testResultLineItems')

    def TestResultLineItems_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/testResultLineItems')

    def TestResultLineItems_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/testResultLineItems')

    def TestResultLineItems_Search(self, search):
        return self.ApiClient.getAPI(f'/testResultLineItems/search/{search}')

    def TestResultLineItems_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/testResultLineItems/searchexact/{search}')

    def TestResultLineItems_GetById(self, id):
        return self.ApiClient.getAPI(f'/testResultLineItems/{id}')

    def TestResults_GetNotes(self, testId):
        return self.ApiClient.getAPI(f'/testresults/{testId}/notes')

    def TestResults_AddNote(self, testId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/testresults/{testId}/notes')

    def TestResults_Cancel(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/testresults/complete')

    def TestResults_Get(self):
        return self.ApiClient.getAPI(f'/testresults')

    def TestResults_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/testresults')

    def TestResults_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/testresults')

    def TestResults_Search(self, search):
        return self.ApiClient.getAPI(f'/testresults/search/{search}')

    def TestResults_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/testresults/searchexact/{search}')

    def TestResults_GetById(self, id):
        return self.ApiClient.getAPI(f'/testresults/{id}')

    def TestTypes_Get(self):
        return self.ApiClient.getAPI(f'/testTypes')

    def TestTypes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/testTypes')

    def TestTypes_Search(self, search):
        return self.ApiClient.getAPI(f'/testTypes/search/{search}')

    def TestTypes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/testTypes/searchexact/{search}')

    def TestTypes_GetById(self, id):
        return self.ApiClient.getAPI(f'/testTypes/{id}')

    def TimeCards_NetLabor(self):
        return self.ApiClient.getAPI(f'/timecards/netlabor')

    def TimeCards_GetTimeSummary(self):
        return self.ApiClient.getAPI(f'/timecards/timesummary')

    def TimeCards_GetSubordinateTimeSummary(self, supervisorId):
        return self.ApiClient.getAPI(f'/timecards/timesummary/{supervisorId}/subordinate')

    def TimeCards_Get(self):
        return self.ApiClient.getAPI(f'/timecards')

    def TimeCards_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/timecards')

    def TimeCards_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/timecards')

    def TimeCards_Search(self, search):
        return self.ApiClient.getAPI(f'/timecards/search/{search}')

    def TimeCards_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/timecards/searchexact/{search}')

    def TimeCards_GetById(self, id):
        return self.ApiClient.getAPI(f'/timecards/{id}')

    def TimeSummaries_Get(self):
        return self.ApiClient.getAPI(f'/timeSummaries')

    def TimeSummaries_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/timeSummaries')

    def TimeSummaries_Search(self, search):
        return self.ApiClient.getAPI(f'/timeSummaries/search/{search}')

    def TimeSummaries_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/timeSummaries/searchexact/{search}')

    def TimeSummaries_GetById(self, id):
        return self.ApiClient.getAPI(f'/timeSummaries/{id}')

    def TimeTypes_Get(self):
        return self.ApiClient.getAPI(f'/timeTypes')

    def TimeTypes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/timeTypes')

    def TimeTypes_Search(self, search):
        return self.ApiClient.getAPI(f'/timeTypes/search/{search}')

    def TimeTypes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/timeTypes/searchexact/{search}')

    def TimeTypes_GetById(self, id):
        return self.ApiClient.getAPI(f'/timeTypes/{id}')

    def UnitsofMeasure_Get(self):
        return self.ApiClient.getAPI(f'/unitsofMeasure')

    def UnitsofMeasure_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/unitsofMeasure')

    def UnitsofMeasure_Search(self, search):
        return self.ApiClient.getAPI(f'/unitsofMeasure/search/{search}')

    def UnitsofMeasure_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/unitsofMeasure/searchexact/{search}')

    def UnitsofMeasure_GetById(self, id):
        return self.ApiClient.getAPI(f'/unitsofMeasure/{id}')

    def UserClasses_PostCollection(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/userclasses/bulk')

    def UserClasses_PutCollection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/userclasses/bulk')

    def UserClasses_Delete(self):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/userclasses')

    def UserClasses_Get(self):
        return self.ApiClient.getAPI(f'/userclasses')

    def UserClasses_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/userclasses')

    def UserClasses_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/userclasses')

    def UserClasses_DeleteById(self, id):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/userclasses/{id}')

    def UserClasses_GetById(self, id):
        return self.ApiClient.getAPI(f'/userclasses/{id}')

    def UserClasses_Search(self, search):
        return self.ApiClient.getAPI(f'/userclasses/search/{search}')

    def UserClasses_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/userclasses/searchexact/{search}')

    def UserClasses_LovSearch(self, search):
        return self.ApiClient.getAPI(f'/userclasses/lov/{search}')

    def UserGroups_Get(self):
        return self.ApiClient.getAPI(f'/userGroups')

    def UserGroups_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/userGroups')

    def UserGroups_Search(self, search):
        return self.ApiClient.getAPI(f'/userGroups/search/{search}')

    def UserGroups_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/userGroups/searchexact/{search}')

    def UserGroups_GetById(self, id):
        return self.ApiClient.getAPI(f'/userGroups/{id}')

    def Users_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/users/bulk')

    def Users_Update(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/users/bulk')

    def Users_Get(self):
        return self.ApiClient.getAPI(f'/users')

    def Users_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/users')

    def Users_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/users')

    def Users_Search(self, search):
        return self.ApiClient.getAPI(f'/users/search/{search}')

    def Users_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/users/searchexact/{search}')

    def Users_GetById(self, id):
        return self.ApiClient.getAPI(f'/users/{id}')

    def UserUserGroups_Get(self):
        return self.ApiClient.getAPI(f'/userUserGroups')

    def UserUserGroups_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/userUserGroups')

    def UserUserGroups_Search(self, search):
        return self.ApiClient.getAPI(f'/userUserGroups/search/{search}')

    def UserUserGroups_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/userUserGroups/searchexact/{search}')

    def UserUserGroups_GetById(self, id):
        return self.ApiClient.getAPI(f'/userUserGroups/{id}')

    def VendorAttributes_CreatePost(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/vendorAttributes/bulk')

    def VendorAttributes_CreatePut(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/vendorAttributes/bulk')

    def VendorAttributes_Delete(self):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/vendorAttributes')

    def VendorAttributes_Get(self):
        return self.ApiClient.getAPI(f'/vendorAttributes')

    def VendorAttributes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/vendorAttributes')

    def VendorAttributes_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/vendorAttributes')

    def VendorAttributes_DeleteById(self, id):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/vendorAttributes/{id}')

    def VendorAttributes_GetById(self, id):
        return self.ApiClient.getAPI(f'/vendorAttributes/{id}')

    def VendorAttributes_Search(self, search):
        return self.ApiClient.getAPI(f'/vendorAttributes/search/{search}')

    def VendorAttributes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/vendorAttributes/searchexact/{search}')

    def VendorAttributes_LovSearch(self, search):
        return self.ApiClient.getAPI(f'/vendorAttributes/lov/{search}')

    def VendorContractParts_Get(self):
        return self.ApiClient.getAPI(f'/vendorContractParts')

    def VendorContractParts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/vendorContractParts')

    def VendorContractParts_Search(self, search):
        return self.ApiClient.getAPI(f'/vendorContractParts/search/{search}')

    def VendorContractParts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/vendorContractParts/searchexact/{search}')

    def VendorContractParts_GetById(self, id):
        return self.ApiClient.getAPI(f'/vendorContractParts/{id}')

    def VendorContracts_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/vendorContracts/bulk')

    def VendorContracts_Update(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/vendorContracts/bulk')

    def VendorContracts_Get(self):
        return self.ApiClient.getAPI(f'/vendorContracts')

    def VendorContracts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/vendorContracts')

    def VendorContracts_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/vendorContracts')

    def VendorContracts_Search(self, search):
        return self.ApiClient.getAPI(f'/vendorContracts/search/{search}')

    def VendorContracts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/vendorContracts/searchexact/{search}')

    def VendorContracts_GetById(self, id):
        return self.ApiClient.getAPI(f'/vendorContracts/{id}')

    def Vendors_Search(self, search):
        return self.ApiClient.getAPI(f'/vendors/search/{search}')

    def Vendors_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/vendors/searchexact/{search}')

    def Vendors_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/vendors/bulk')

    def Vendors_Update(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/vendors/bulk')

    def Vendors_Get(self):
        return self.ApiClient.getAPI(f'/vendors')

    def Vendors_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/vendors')

    def Vendors_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/vendors')

    def Vendors_GetById(self, id):
        return self.ApiClient.getAPI(f'/vendors/{id}')

    def VendorTypes_Get(self):
        return self.ApiClient.getAPI(f'/vendorTypes')

    def VendorTypes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/vendorTypes')

    def VendorTypes_Search(self, search):
        return self.ApiClient.getAPI(f'/vendorTypes/search/{search}')

    def VendorTypes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/vendorTypes/searchexact/{search}')

    def VendorTypes_GetById(self, id):
        return self.ApiClient.getAPI(f'/vendorTypes/{id}')

    def VendorVendorTypes_Get(self):
        return self.ApiClient.getAPI(f'/vendorVendorTypes')

    def VendorVendorTypes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/vendorVendorTypes')

    def VendorVendorTypes_Search(self, search):
        return self.ApiClient.getAPI(f'/vendorVendorTypes/search/{search}')

    def VendorVendorTypes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/vendorVendorTypes/searchexact/{search}')

    def VendorVendorTypes_GetById(self, id):
        return self.ApiClient.getAPI(f'/vendorVendorTypes/{id}')

    def WarrantyCancelReasons_Get(self):
        return self.ApiClient.getAPI(f'/warrantyCancelReasons')

    def WarrantyCancelReasons_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/warrantyCancelReasons')

    def WarrantyCancelReasons_Search(self, search):
        return self.ApiClient.getAPI(f'/warrantyCancelReasons/search/{search}')

    def WarrantyCancelReasons_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/warrantyCancelReasons/searchexact/{search}')

    def WarrantyCancelReasons_GetById(self, id):
        return self.ApiClient.getAPI(f'/warrantyCancelReasons/{id}')

    def WarrantyCategories_Get(self):
        return self.ApiClient.getAPI(f'/warrantyCategories')

    def WarrantyCategories_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/warrantyCategories')

    def WarrantyCategories_Search(self, search):
        return self.ApiClient.getAPI(f'/warrantyCategories/search/{search}')

    def WarrantyCategories_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/warrantyCategories/searchexact/{search}')

    def WarrantyCategories_GetById(self, id):
        return self.ApiClient.getAPI(f'/warrantyCategories/{id}')

    def WarrantyClaimDetails_Get(self):
        return self.ApiClient.getAPI(f'/warrantyClaimDetails')

    def WarrantyClaimDetails_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/warrantyClaimDetails')

    def WarrantyClaimDetails_Search(self, search):
        return self.ApiClient.getAPI(f'/warrantyClaimDetails/search/{search}')

    def WarrantyClaimDetails_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/warrantyClaimDetails/searchexact/{search}')

    def WarrantyClaimDetails_GetById(self, id):
        return self.ApiClient.getAPI(f'/warrantyClaimDetails/{id}')

    def WarrantyClaims_UpdateCollection(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/warrantyclaims/bulk')

    def WarrantyClaims_Get(self):
        return self.ApiClient.getAPI(f'/warrantyclaims')

    def WarrantyClaims_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/warrantyclaims')

    def WarrantyClaims_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/warrantyclaims')

    def WarrantyClaims_Search(self, search):
        return self.ApiClient.getAPI(f'/warrantyclaims/search/{search}')

    def WarrantyClaims_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/warrantyclaims/searchexact/{search}')

    def WarrantyClaims_GetById(self, id):
        return self.ApiClient.getAPI(f'/warrantyclaims/{id}')

    def WarrantyDenyReasons_Get(self):
        return self.ApiClient.getAPI(f'/warrantyDenyReasons')

    def WarrantyDenyReasons_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/warrantyDenyReasons')

    def WarrantyDenyReasons_Search(self, search):
        return self.ApiClient.getAPI(f'/warrantyDenyReasons/search/{search}')

    def WarrantyDenyReasons_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/warrantyDenyReasons/searchexact/{search}')

    def WarrantyDenyReasons_GetById(self, id):
        return self.ApiClient.getAPI(f'/warrantyDenyReasons/{id}')

    def WorkAccomplishedCodes_GetForAsset(self, assetid):
        return self.ApiClient.getAPI(f'/workAccomplishedCodes/forasset/{assetid}')

    def WorkAccomplishedCodes_SearchByAsset(self, assetid, search):
        return self.ApiClient.getAPI(f'/workAccomplishedCodes/forasset/{assetid}/search/{search}')

    def WorkAccomplishedCodes_SearchByAssetExact(self, assetid, search):
        return self.ApiClient.getAPI(f'/workAccomplishedCodes/forasset/{assetid}/searchexact/{search}')

    def WorkAccomplishedCodes_Get(self):
        return self.ApiClient.getAPI(f'/workAccomplishedCodes')

    def WorkAccomplishedCodes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workAccomplishedCodes')

    def WorkAccomplishedCodes_Search(self, search):
        return self.ApiClient.getAPI(f'/workAccomplishedCodes/search/{search}')

    def WorkAccomplishedCodes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workAccomplishedCodes/searchexact/{search}')

    def WorkAccomplishedCodes_GetById(self, id):
        return self.ApiClient.getAPI(f'/workAccomplishedCodes/{id}')

    def WorkAssignments_DeleteTaskAssignment(self, workOrderId, taskId, employeeId):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/workAssignments/workorder/{workOrderId}/task/{taskId}/employee/{employeeId}')

    def WorkAssignments_DeleteWorkOrderAssignment(self, workOrderId, employeeId):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/workAssignments/workorder/{workOrderId}/employee/{employeeId}')

    def WorkAssignments_Get(self):
        return self.ApiClient.getAPI(f'/workAssignments')

    def WorkAssignments_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workAssignments')

    def WorkAssignments_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workAssignments')

    def WorkAssignments_Delete(self):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/workAssignments')

    def WorkAssignments_Search(self, search):
        return self.ApiClient.getAPI(f'/workAssignments/search/{search}')

    def WorkAssignments_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workAssignments/searchexact/{search}')

    def WorkAssignments_GetById(self, id):
        return self.ApiClient.getAPI(f'/workAssignments/{id}')

    def WorkClasses_Get(self):
        return self.ApiClient.getAPI(f'/workClasses')

    def WorkClasses_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workClasses')

    def WorkClasses_Search(self, search):
        return self.ApiClient.getAPI(f'/workClasses/search/{search}')

    def WorkClasses_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workClasses/searchexact/{search}')

    def WorkClasses_GetById(self, id):
        return self.ApiClient.getAPI(f'/workClasses/{id}')

    def WorkDelayCodes_Get(self):
        return self.ApiClient.getAPI(f'/workDelayCodes')

    def WorkDelayCodes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workDelayCodes')

    def WorkDelayCodes_Search(self, search):
        return self.ApiClient.getAPI(f'/workDelayCodes/search/{search}')

    def WorkDelayCodes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workDelayCodes/searchexact/{search}')

    def WorkDelayCodes_GetById(self, id):
        return self.ApiClient.getAPI(f'/workDelayCodes/{id}')

    def WorkDelays_Get(self):
        return self.ApiClient.getAPI(f'/workDelays')

    def WorkDelays_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workDelays')

    def WorkDelays_Search(self, search):
        return self.ApiClient.getAPI(f'/workDelays/search/{search}')

    def WorkDelays_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workDelays/searchexact/{search}')

    def WorkDelays_GetById(self, id):
        return self.ApiClient.getAPI(f'/workDelays/{id}')

    def WorkOrderAttributes_CreatePost(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workorderAttributes/bulk')

    def WorkOrderAttributes_CreatePut(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workorderAttributes/bulk')

    def WorkOrderAttributes_Get(self):
        return self.ApiClient.getAPI(f'/workorderAttributes')

    def WorkOrderAttributes_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workorderAttributes')

    def WorkOrderAttributes_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workorderAttributes')

    def WorkOrderAttributes_Search(self, search):
        return self.ApiClient.getAPI(f'/workorderAttributes/search/{search}')

    def WorkOrderAttributes_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workorderAttributes/searchexact/{search}')

    def WorkOrderAttributes_GetById(self, id):
        return self.ApiClient.getAPI(f'/workorderAttributes/{id}')

    def WorkOrderCommercials_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workordercommercials/bulk')

    def WorkOrderCommercials_Get(self):
        return self.ApiClient.getAPI(f'/workordercommercials')

    def WorkOrderCommercials_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workordercommercials')

    def WorkOrderCommercials_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workordercommercials')

    def WorkOrderCommercials_Search(self, search):
        return self.ApiClient.getAPI(f'/workordercommercials/search/{search}')

    def WorkOrderCommercials_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workordercommercials/searchexact/{search}')

    def WorkOrderCommercials_GetById(self, id):
        return self.ApiClient.getAPI(f'/workordercommercials/{id}')

    def WorkOrderLabor_Get(self):
        return self.ApiClient.getAPI(f'/workOrderLabor')

    def WorkOrderLabor_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workOrderLabor')

    def WorkOrderLabor_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workOrderLabor')

    def WorkOrderLabor_Search(self, search):
        return self.ApiClient.getAPI(f'/workOrderLabor/search/{search}')

    def WorkOrderLabor_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workOrderLabor/searchexact/{search}')

    def WorkOrderLabor_GetById(self, id):
        return self.ApiClient.getAPI(f'/workOrderLabor/{id}')

    def WorkOrderParts_Get(self):
        return self.ApiClient.getAPI(f'/workOrderParts')

    def WorkOrderParts_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workOrderParts')

    def WorkOrderParts_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workOrderParts')

    def WorkOrderParts_Create(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workOrderParts/bulk')

    def WorkOrderParts_Return(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workOrderParts/return')

    def WorkOrderParts_CollectionWithResults(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workOrderParts/bulk/returnresults')

    def WorkOrderParts_Search(self, search):
        return self.ApiClient.getAPI(f'/workOrderParts/search/{search}')

    def WorkOrderParts_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workOrderParts/searchexact/{search}')

    def WorkOrderParts_GetById(self, id):
        return self.ApiClient.getAPI(f'/workOrderParts/{id}')

    def WorkOrders_Get(self):
        return self.ApiClient.getAPI(f'/workorders')

    def WorkOrders_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workorders')

    def WorkOrders_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workorders')

    def WorkOrders_Delete(self):
        return self.ApiClient.deleteAPI(self.ApiClient.payload, f'/workorders')

    def WorkOrders_GetNotes(self, workOrderId):
        return self.ApiClient.getAPI(f'/workorders/{workOrderId}/notes')

    def WorkOrders_AddNote(self, workOrderId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workorders/{workOrderId}/notes')

    def WorkOrders_Cancel(self, workOrderId):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workorders/{workOrderId}/cancel')

    def WorkOrders_GetDelays(self, workOrderId):
        return self.ApiClient.getAPI(f'/workorders/{workOrderId}/delays')

    def WorkOrders_PostDelay(self, workOrderId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workorders/{workOrderId}/delays')

    def WorkOrders_PutDelay(self, workOrderId):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workorders/{workOrderId}/delays')

    def WorkOrders_Close(self, workOrderId):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workorders/{workOrderId}/close')

    def WorkOrders_Finish(self, workOrderId):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workorders/{workOrderId}/finish')

    def WorkOrders_UnFinish(self, workOrderId):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workorders/{workOrderId}/unfinish')

    def WorkOrders_Open(self, workOrderId):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workorders/{workOrderId}/open')

    def WorkOrders_UpdateMeters(self, workOrderId):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workorders/{workOrderId}/updatemeters')

    def WorkOrders_SavePmChecklist(self, workOrderId):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workorders/{workOrderId}/pmchecklist')

    def WorkOrders_AddStandardJob(self, workOrderId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workorders/{workOrderId}/standardjob')

    def WorkOrders_GetPartReserves(self, workOrderId):
        return self.ApiClient.getAPI(f'/workorders/{workOrderId}/partreserves')

    def WorkOrders_GetFinishAllowed(self, workOrderId):
        return self.ApiClient.getAPI(f'/workorders/{workOrderId}/finishallowed')

    def WorkOrders_GetCloseAllowed(self, workOrderId):
        return self.ApiClient.getAPI(f'/workorders/{workOrderId}/closeallowed')

    def WorkOrders_AddServiceRequests(self, workOrderId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workorders/{workOrderId}/addsrs')

    def WorkOrders_RemoveServiceRequests(self, workOrderId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workorders/{workOrderId}/removesrs')

    def WorkOrders_Search(self, search):
        return self.ApiClient.getAPI(f'/workorders/search/{search}')

    def WorkOrders_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workorders/searchexact/{search}')

    def WorkOrders_GetById(self, id):
        return self.ApiClient.getAPI(f'/workorders/{id}')

    def WorkOrderTasks_Get(self):
        return self.ApiClient.getAPI(f'/workordertasks')

    def WorkOrderTasks_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workordertasks')

    def WorkOrderTasks_Put(self):
        return self.ApiClient.putAPI(self.ApiClient.payload, f'/workordertasks')

    def WorkOrderTasks_GetNotes(self, workOrderId, taskId):
        return self.ApiClient.getAPI(f'/workordertasks/{workOrderId}/{taskId}/notes')

    def WorkOrderTasks_AddNote(self, workOrderId, taskId):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workordertasks/{workOrderId}/{taskId}/notes')

    def WorkOrderTasks_GetJobbedOnEmployees(self, workOrderId, taskId):
        return self.ApiClient.getAPI(f'/workordertasks/{workOrderId}/{taskId}/jobbedonemployees')

    def WorkOrderTasks_Search(self, search):
        return self.ApiClient.getAPI(f'/workordertasks/search/{search}')

    def WorkOrderTasks_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workordertasks/searchexact/{search}')

    def WorkOrderTasks_GetById(self, id):
        return self.ApiClient.getAPI(f'/workordertasks/{id}')

    def WorkOrderVendors_Get(self):
        return self.ApiClient.getAPI(f'/workordervendors')

    def WorkOrderVendors_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workordervendors')

    def WorkOrderVendors_Search(self, search):
        return self.ApiClient.getAPI(f'/workordervendors/search/{search}')

    def WorkOrderVendors_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workordervendors/searchexact/{search}')

    def WorkOrderVendors_GetById(self, id):
        return self.ApiClient.getAPI(f'/workordervendors/{id}')

    def WorkPlans_Get(self):
        return self.ApiClient.getAPI(f'/workPlans')

    def WorkPlans_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workPlans')

    def WorkPlans_Search(self, search):
        return self.ApiClient.getAPI(f'/workPlans/search/{search}')

    def WorkPlans_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workPlans/searchexact/{search}')

    def WorkPlans_GetById(self, id):
        return self.ApiClient.getAPI(f'/workPlans/{id}')

    def WorkPositions_GetForTask(self, taskId):
        return self.ApiClient.getAPI(f'/workpositions/fortask/{taskId}')

    def WorkPositions_Get(self):
        return self.ApiClient.getAPI(f'/workpositions')

    def WorkPositions_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workpositions')

    def WorkPositions_Search(self, search):
        return self.ApiClient.getAPI(f'/workpositions/search/{search}')

    def WorkPositions_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workpositions/searchexact/{search}')

    def WorkPositions_GetById(self, id):
        return self.ApiClient.getAPI(f'/workpositions/{id}')

    def WorkPriorities_Get(self):
        return self.ApiClient.getAPI(f'/workPriorities')

    def WorkPriorities_Post(self):
        return self.ApiClient.postAPI(self.ApiClient.payload, f'/workPriorities')

    def WorkPriorities_Search(self, search):
        return self.ApiClient.getAPI(f'/workPriorities/search/{search}')

    def WorkPriorities_SearchExact(self, search):
        return self.ApiClient.getAPI(f'/workPriorities/searchexact/{search}')

    def WorkPriorities_GetById(self, id):
        return self.ApiClient.getAPI(f'/workPriorities/{id}')

