from base import Base


class Facility(Base):
    def __init__(self, facility_name, year, age_category, gender, region, district, cycle, households_visited, result):
        super.__init__(year, age_category, gender, region,
                       district, cycle)
        self.facility_name = facility_name
        self.households_visited = households_visited
        self.result = result
