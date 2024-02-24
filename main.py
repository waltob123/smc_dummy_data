import sys
import random

from facility import Facility
from adr import ADR
from storage import FileStorage
from utils import YEARS, AGE_CATEGORIES, REGIONS_DISTRICTS, GENDER


def main(filename, type_of_record):
    if type_of_record == "Facility":
        results = []
        new_facility = Facility()
        storage = FileStorage(filename)
        storage.write_header(new_facility.to_dict().keys())
        for year in YEARS:
            weight=year["weight"]
            for region in REGIONS_DISTRICTS.keys():
                for district_name, facilities in REGIONS_DISTRICTS.get(region).items():
                    for facility in facilities:
                        new_facility.facility_name = facility
                        new_facility.year = year["yr"]
                        new_facility.region = region
                        new_facility.district = district_name
                        new_facility.number_of_households =int( random.randint(
                            50, 300) *weight)
                        for i in range(1, 5):
                            new_facility.cycle = i
                            for j in range(1, 4):
                                new_facility.round = j
                                new_facility.households_visited =int( random.randint(
                                    50, new_facility.number_of_households)*weight)
                                for age in AGE_CATEGORIES:
                                    new_facility.age_category = age
                                    new_facility.blisters_received =int(random.randint(
                                        300, 350)*weight) 
                                    new_facility.blisters_used =int( random.randint(
                                        300, new_facility.blisters_received)*weight)
                                    new_facility.blisters_wasted =int( random.randint(
                                        0, (new_facility.blisters_received - new_facility.blisters_used))
                                   *weight )
                                    new_facility.blisters_remaining = new_facility.blisters_received - \
                                        new_facility.blisters_used - new_facility.blisters_wasted
                                    random_percentage = round(
                                        random.uniform(0.3, 0.8), 1)
                                    for gender in GENDER:
                                        new_facility.gender = gender
                                        if gender == "Male":
                                            new_facility.number_of_children = int(
                                                new_facility.blisters_used * random_percentage)
                                        else:
                                            new_facility.number_of_children = int(
                                                new_facility.blisters_used * (1 - random_percentage))
                                        new_facility.adr_reported = random.randint(
                                            0, int(new_facility.number_of_children * 0.2))
                                        results.append(new_facility.to_dict())
                                        storage.save(new_facility.to_dict())
                                        
        print(results)

    if type_of_record == "ADR":
        print("ADR")

    if type_of_record == "Blisters":
        print("Blisters")


if __name__ == "__main__":
    filename = sys.argv[1]
    type_of_record = sys.argv[2]
    main(filename, type_of_record)
