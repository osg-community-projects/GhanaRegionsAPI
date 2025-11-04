# Sample data for Ghana regions, districts, and towns

REGIONS_DATA = [
    {"id": 1, "name": "AHAFO", "capital": "GOASO"},
    {"id": 2, "name": "ASHANTI", "capital": "KUMASI"},
    {"id": 3, "name": "BONO EAST", "capital": "TECHIMAN"},
    {"id": 4, "name": "BRONG AHAFO", "capital": "SUNYANI"},
    {"id": 5, "name": "CENTRAL", "capital": "CAPE COAST"},
    {"id": 6, "name": "EASTERN", "capital": "KOFORIDUA"},
    {"id": 7, "name": "GREATER ACCRA", "capital": "ACCRA"},
    {"id": 8, "name": "NORTH EAST", "capital": "NALERIGU"},
    {"id": 9, "name": "NORTHERN", "capital": "TAMALE"},
    {"id": 10, "name": "OTI", "capital": "DAMBAI"},
    {"id": 11, "name": "SAVANNAH", "capital": "DAMONGO"},
    {"id": 12, "name": "UPPER EAST", "capital": "BOLGATANGA"},
    {"id": 13, "name": "UPPER WEST", "capital": "WA"},
    {"id": 14, "name": "VOLTA", "capital": "HO"},
    {"id": 15, "name": "WESTERN", "capital": "SEKONDI-TAKORADI"},
    {"id": 16, "name": "WESTERN NORTH", "capital": "SEFWI WIASO"}
]

DISTRICTS_DATA = [
    # Greater Accra Region
    {"id": 1, "name": "Accra Metropolitan", "region_id": 7},
    {"id": 2, "name": "Tema Metropolitan", "region_id": 7},
    {"id": 3, "name": "Ga East Municipal", "region_id": 7},
    {"id": 4, "name": "Ga West Municipal", "region_id": 7},
    {"id": 5, "name": "Ga South Municipal", "region_id": 7},
    
    # Ashanti Region
    {"id": 6, "name": "Kumasi Metropolitan", "region_id": 2},
    {"id": 7, "name": "Obuasi Municipal", "region_id": 2},
    {"id": 8, "name": "Ejisu Municipal", "region_id": 2},
    {"id": 9, "name": "Asante Akim North Municipal", "region_id": 2},
    {"id": 10, "name": "Asante Akim South Municipal", "region_id": 2},
    
    # Central Region
    {"id": 11, "name": "Cape Coast Metropolitan", "region_id": 5},
    {"id": 12, "name": "Komenda-Edina-Eguafo-Abirem Municipal", "region_id": 5},
    {"id": 13, "name": "Abura-Asebu-Kwamankese", "region_id": 5},
    {"id": 14, "name": "Mfantsiman Municipal", "region_id": 5},
    
    # Eastern Region
    {"id": 15, "name": "New-Juaben Municipal", "region_id": 6},
    {"id": 16, "name": "Akuapem North Municipal", "region_id": 6},
    {"id": 17, "name": "East Akim Municipal", "region_id": 6},
    {"id": 18, "name": "West Akim Municipal", "region_id": 6},
    
    # Northern Region
    {"id": 19, "name": "Tamale Metropolitan", "region_id": 9},
    {"id": 20, "name": "Sagnarigu Municipal", "region_id": 9},
    {"id": 21, "name": "Yendi Municipal", "region_id": 9},
    {"id": 22, "name": "Savelugu Municipal", "region_id": 9},
    
    # Western Region
    {"id": 23, "name": "Sekondi-Takoradi Metropolitan", "region_id": 15},
    {"id": 24, "name": "Shama", "region_id": 15},
    {"id": 25, "name": "Ahanta West Municipal", "region_id": 15},
    {"id": 26, "name": "Nzema East Municipal", "region_id": 15}
]

TOWNS_DATA = [
    # Greater Accra Region - Accra Metropolitan
    {"id": 1, "name": "Accra", "district_id": 1, "population": 2291352},
    {"id": 2, "name": "Osu", "district_id": 1, "population": 45000},
    {"id": 3, "name": "Labadi", "district_id": 1, "population": 35000},
    {"id": 4, "name": "Dansoman", "district_id": 1, "population": 120000},
    
    # Greater Accra Region - Tema Metropolitan
    {"id": 5, "name": "Tema", "district_id": 2, "population": 402637},
    {"id": 6, "name": "Community 1", "district_id": 2, "population": 25000},
    {"id": 7, "name": "Community 25", "district_id": 2, "population": 18000},
    
    # Ashanti Region - Kumasi Metropolitan
    {"id": 8, "name": "Kumasi", "district_id": 6, "population": 2035064},
    {"id": 9, "name": "Bantama", "district_id": 6, "population": 85000},
    {"id": 10, "name": "Asokwa", "district_id": 6, "population": 95000},
    {"id": 11, "name": "Suame", "district_id": 6, "population": 110000},
    
    # Ashanti Region - Obuasi Municipal
    {"id": 12, "name": "Obuasi", "district_id": 7, "population": 175043},
    {"id": 13, "name": "Tutuka", "district_id": 7, "population": 12000},
    
    # Central Region - Cape Coast Metropolitan
    {"id": 14, "name": "Cape Coast", "district_id": 11, "population": 169894},
    {"id": 15, "name": "Elmina", "district_id": 11, "population": 25000},
    {"id": 16, "name": "Pedu", "district_id": 11, "population": 8000},
    
    # Eastern Region - New-Juaben Municipal
    {"id": 17, "name": "Koforidua", "district_id": 15, "population": 183727},
    {"id": 18, "name": "Effiduase", "district_id": 15, "population": 15000},
    
    # Northern Region - Tamale Metropolitan
    {"id": 19, "name": "Tamale", "district_id": 19, "population": 371351},
    {"id": 20, "name": "Kalpohin", "district_id": 19, "population": 12000},
    {"id": 21, "name": "Vittin", "district_id": 19, "population": 8500},
    
    # Western Region - Sekondi-Takoradi Metropolitan
    {"id": 22, "name": "Sekondi", "district_id": 23, "population": 289787},
    {"id": 23, "name": "Takoradi", "district_id": 23, "population": 145000},
    {"id": 24, "name": "Essikado", "district_id": 23, "population": 35000}
]
