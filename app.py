import csv
import random


DATA_FILE = 'data.csv'
DATA_SIZE = 1000
FIELDNAMES = [
    'facility_name', 'region', 'district', 'cycle', 'number_of_households',
    'three_to_eleven_months_males', 'three_to_eleven_months_females',
    'twelve_to_fifty_nine_months_males', 'twelve_to_fifty_nine_months_females'
]


def generate_facility_name(rand_min: int, rand_max: int) -> str:
    '''
    Generates a facility name.
    
    rand_min (int): minimum value for the random number.
    rand_max (int): maximum value for the random number.
    
    Return (str): facility name.
    '''
    return f'FCT{random.randint(rand_min, rand_max)}'


def generate_regions() -> list:
    '''
    Generates a list of regions.

    Return (List): List of regions
    '''
    return [f"REG{i}" for i in range(1, 17)]


def save_to_csv(filename: str, data: dict) -> None:
    '''
    Saves a data to a CSV file.

    filename (str): path to the CSV file to save to.
    data (dict): dictionary containing data to save.

    Return: None
    '''
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writerow(data)



def generate_records() -> dict:
    facility_name = generate_facility_name(10000, 99999)
    region = random.choice(generate_regions())
    district = f'DST{random.randint(1, 10)}'
    for i in range(1, 5):
        cycle = i
        number_of_households = random.randint(50, 200)
        three_to_eleven_months_males = random.randint(50, 500)
        three_to_eleven_months_females = random.randint(50, 500)
        twelve_to_fifty_nine_months_males = random.randint(50, 500)
        twelve_to_fifty_nine_months_females = random.randint(50, 500)
        data = {
            'facility_name': facility_name,
            'region': region,
            'district': district,
            'cycle': cycle,
            'number_of_households': number_of_households,
            '3_to_11_months(males)': three_to_eleven_months_males,
            '3_to_11_months(females)': three_to_eleven_months_females,
            '12_to_59_months(males)': twelve_to_fifty_nine_months_males,
            '12_to_59_months(females)': twelve_to_fifty_nine_months_females 
        }
        
        save_to_csv(DATA_FILE, data)


def main():
    with open(DATA_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
    for i in range(DATA_SIZE):
        generate_records()



if __name__ == '__main__':
    main()
