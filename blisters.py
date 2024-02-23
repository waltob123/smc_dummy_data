from base import Base


class Blisters(Base):

    def __init__(self, year, age_category, gender, region, district, cycle, received, used, wasted, remaining):
        super.__init__(year, age_category, gender, region, district, cycle)
        self.received = received
        self.used = used
        self.wasted = wasted
        self.remaining = remaining
