import random
import csv


class Base:

    def __init__(self, year, age_category, gender, region, district, cycle):
        self.year = year
        self.age_category = age_category
        self.gender = gender
        self.region = region
        self.district = district
        self.cycle = cycle

    def to_dict(self):
        return {
            "year": self.year,
            "age_category": self.age_category,
            "gender": self.gender,
            "region": self.region,
            "district": self.district,
            "cycle": self.cycle
        }

    def __str__(self):
        return f"""
        {self.__class__.__name__} <{self.__dict__}>
    """
