import random

YEARS = [2018, 2019, 2020, 2021, 2022, 2023]

REGIONS = [
    'Ashanti', 'Brong Ahafo', 'Central',
    'Eastern', 'Greater Accra', 'Northern',
    'Upper East', 'Upper West', 'Volta', 'Western',
    'Savannah', 'Bono East', 'Oti',
    'Ahafo', 'Western North', 'North East'
]

AGE_CATEGORIES = ['3-11 months', '12-59 months', '60-62 months']

GENDER = ["Male", "Female"]

REGIONS_DISTRICTS = {
    region: {f"{region}_DIST_{i}": [f"FCT{random.randint(10000, 99999)}" for j in range(10, 21)] for i in range(random.randint(7, 16))} for region in REGIONS
}

# print(REGIONS_DISTRICTS.get('Ashanti').get('Ashanti_DIST_1'))
