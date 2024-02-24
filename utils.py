import random

YEARS = [{"yr":2018,"weight":1}, {"yr":2019,"weight":1.15},{ "yr":2020,"weight":1.22},{ "yr":2021,"weight":1.13},{ "yr":2022,"weight":1.08}, {"yr":2023,"weight":1.03}]

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
