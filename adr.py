from base import Base


class ADR(Base):

    def __init__(self, adr_name, year, age_category, gender, region, district, cycle, result):
        super.__init__(year, age_category, gender, region,
                       district, cycle)
        self.adr_name = adr_name
        self.result = result
