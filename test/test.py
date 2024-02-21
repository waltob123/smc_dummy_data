import csv
import unittest
from app import generate_facility_name, generate_regions


class TestApp(unittest.TestCase):
    def test_generate_facility_name(self):
        name = generate_facility_name(10000, 99999)
        self.assertTrue(name.startswith('FCT'))

    def test_generate_regions(self):
        regions = generate_regions()
        self.assertTrue(len(regions) == 16)

    # Testing if test is working
    def test_true(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()


# def get_facility_data(facility_name: str) -> list:
#     '''
#     Returns a list of facility data.

#     facility_name (str): name of the facility to retrieve data for.

#     Return (List): List of facility data.
#     '''
#     with open('data.csv') as file:
#         reader = csv.DictReader(file)
#         return [row for row in reader if row['facility_name'] == facility_name]


# a = get_facility_data('FCT51577')
# print(a)
