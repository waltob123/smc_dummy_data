from base import Base


class Facility(Base):
    def __init__(self, facility_name=None, 
                 year=None, age_category=None, gender=None, 
                 region=None, district=None, cycle=None, round=None, 
                 number_of_households=None, households_visited=None, number_of_children_dosed=None,
                  blisters_received=None, blisters_used=None, blisters_wasted=None, 
                  blisters_remaining=None,
                  adr_reported=None, number_of_children_in_households=None):
        super().__init__(year, age_category, gender, region,
                       district, cycle, round)
        self.facility_name = facility_name
        self.number_of_households = number_of_households
        self.households_visited = households_visited
        self.number_of_children_in_households = number_of_children_in_households
        self.number_of_children_dosed = number_of_children_dosed
        self.number_of_children_not_dosed = None
        self.blisters_received = blisters_received
        self.blisters_used = blisters_used
        self.blisters_wasted = blisters_wasted
        self.blisters_remaining = blisters_remaining
        self.adr_reported = adr_reported

        

    def to_dict(self):
        return {
            "facility_name": self.facility_name,
            "year": self.year,
            "age_category": self.age_category,
            "gender": self.gender,
            "region": self.region,
            "district": self.district,
            "cycle": self.cycle,
            "round": self.round,
            "number_of_households": self.number_of_households,
            "households_visited": self.households_visited,
            "number_of_children_in_households": self.number_of_children_in_households,
            "number_of_children_dosed": self.number_of_children_dosed,
            "number_of_children_not_dosed": self.number_of_children_not_dosed,
            "blisters_received": self.blisters_received,
            "blisters_used": self.blisters_used,
            "blisters_wasted": self.blisters_wasted,
            "blisters_remaining": self.blisters_remaining,
            "adr_reported": self.adr_reported
        }