import sys
import random

from facility import Facility
from adr import ADR
from storage import FileStorage
from utils import YEARS, AGE_CATEGORIES, REGIONS_DISTRICTS, GENDER, ADR_NAMES


def main(filename, type_of_record):
    if type_of_record == "Facility":
        results = []
        new_facility = Facility()
        storage = FileStorage(filename)
        storage.write_header(new_facility.to_dict().keys())
        for year in YEARS:
            weight = year["weight"]
            for region in REGIONS_DISTRICTS.keys():
                for district_name, facilities in REGIONS_DISTRICTS.get(region).items():
                    for facility in facilities:
                        new_facility.facility_name = facility
                        new_facility.year = year["yr"]
                        new_facility.region = region
                        new_facility.district = district_name
                        new_facility.number_of_households = int(random.randint(
                            50, 200) * weight)
                        for i in range(1, 5):
                            new_facility.cycle = i
                            for j in range(1, 4):
                                new_facility.round = j
                                new_facility.households_visited = int(random.randint(
                                    50, new_facility.number_of_households)*weight)
                                new_facility.number_of_children_in_households = random.randint(
                                    new_facility.households_visited, new_facility.households_visited*5)
                                for age in AGE_CATEGORIES:
                                    new_facility.age_category = age
                                   
                                    new_facility.blisters_received = int(random.randint(
                                       new_facility.number_of_children_in_households,int(1000*weight))*weight)
                                    
                                    number_of_children_dosed  = random.randint(
                                        new_facility.households_visited, new_facility.number_of_children_in_households)
                                    number_of_children_not_dosed = new_facility.number_of_children_in_households-number_of_children_dosed
                                    new_facility.blisters_used =number_of_children_dosed
                                    
                                          # original blisters used before commenting

                                    # new_facility.blisters_used = random.randint(
                                    #     0, new_facility.number_of_children_in_households)   # new blisters used
                                    new_facility.blisters_wasted = random.randint(
                                        0, (new_facility.blisters_received - new_facility.blisters_used))
                                    new_facility.blisters_remaining = new_facility.blisters_received - \
                                        new_facility.blisters_used - new_facility.blisters_wasted
                                    random_percentage = round(
                                        random.uniform(0.3, 0.8), 1)
                                    
                                    
                                    # new_facility.number_of_children_not_dosed = new_facility.number_of_children_in_households - \
                                    #     - new_facility.blisters_used
                                       
                                    for gender in GENDER:
                                        new_facility.gender = gender
                                        if gender == "Male":
                                            # Calculate the number of children dosed for males
                                            new_facility.number_of_children_dosed = int(number_of_children_dosed * random_percentage)
                                            # Calculate the number of children not dosed for males
                                            new_facility.number_of_children_not_dosed = int(number_of_children_not_dosed * random_percentage)
                                        else:
                                            # Calculate the number of children dosed for females
                                            new_facility.number_of_children_dosed = number_of_children_dosed - new_facility.number_of_children_dosed
                                            # Calculate the number of children not dosed for females
                                            new_facility.number_of_children_not_dosed = number_of_children_not_dosed - new_facility.number_of_children_not_dosed

                                    # Ensure that the sum of dosed children for male and female equals number_of_children_dosed
                                   
                                        new_facility.adr_reported = random.randint(
                                                    0, int(new_facility.number_of_children_dosed * 0.2))

                                        results.append(new_facility.to_dict())
                                        storage.save(new_facility.to_dict())
            print(results)

    if type_of_record == "ADR":
        results = []
        storage = FileStorage(filename)
        storage.write_header(ADR().to_dict().keys())

        for year in YEARS:
            weight = year["weight"]
            for region in REGIONS_DISTRICTS.keys():
                for district_name, facilities in REGIONS_DISTRICTS.get(region).items():
                    for i in range(1, 5):
                        for j in range(1, 4):
                            new_adr = ADR()  # Create a new instance of ADR inside the loop
                            new_adr.year = year["yr"]
                            new_adr.region = region
                            new_adr.district = district_name
                            new_adr.cycle = i
                            new_adr.round = j
                            for age in AGE_CATEGORIES:
                                new_adr.age_category = age
                                new_adr.adr_name = random.choice(ADR_NAMES)
                                random_percentage = round(
                                    random.uniform(0.3, 0.8), 1)

                                no_of_reported_cases = int(random.randint(
                                    400, 800)*weight)
                                for gender in GENDER:
                                    new_adr.gender = gender

                                    if gender == "Male":
                                        new_adr.no_of_reported_cases = int(
                                            no_of_reported_cases * random_percentage)

                                    else:
                                        new_adr.no_of_reported_cases = int(
                                            no_of_reported_cases * (1 - random_percentage))

                                    results.append(new_adr.to_dict())
                                    storage.save(new_adr.to_dict())

        print("ADR data")

    if type_of_record == "Blisters":
        print("Blisters")


if __name__ == "__main__":
    filename = sys.argv[1]
    type_of_record = sys.argv[2]
    main(filename, type_of_record)
