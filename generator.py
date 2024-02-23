import csv


class Generator(object):
    def __init__(self, filename: str):
        self.filename = filename


    def read_csv(self) -> list:
        '''
        Reads a CSV file and returns a list of dictionaries.
        
        Return (List): List of dictionaries.
        '''
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def write_csv(self, data: dict) -> None: pass

# generator = Generator('data.csv')
