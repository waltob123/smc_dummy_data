import csv


class FileStorage:

    def __init__(self, filename):
        self.filename = filename

    def write_header(self, fieldnames: list):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

    def save(self, data: dict):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            writer.writerow(data)
