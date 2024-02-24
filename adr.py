from base import Base


class ADR(Base):

    def __init__(self, adr_name=None, year=None, age_category=None, gender=None, region=None, district=None, cycle=None,no_of_reported_cases=None,round=None):
        super().__init__(year, age_category, gender, region,
                       district, cycle,round)
        self.adr_name = adr_name
        self.no_of_reported_cases = no_of_reported_cases
       

    def to_dict(self):
        return{
            "adr_name": self.adr_name,
            "year": self.year,
            "age_category":self.age_category,
            "gender":self.gender,
            "region":self.region,
            "district":self.district,
            "circle":self.cycle,
            "no_of_reported_cases":self.no_of_reported_cases,
            "round":self.round,
        }

