import csv
import random

class Table:
    def __init__(self, tableName,Ttype, col1, col2, col3, col5, col6, col7, col8, col9, col4=None, col10=None, col11=None, col12=None, col13=None, col14=None, DATA_SIZE=1, max_district=5,max_facility=5, child=False):
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3
        self.col4 = col4
        self.col5 = col5
        self.col6 = col6
        self.col7 = col7
        self.col8 = col8
        self.col9 = col9
        self.col10 = col10
        self.col11 = col11
        self.col12 = col12
        self.col13 = col13
        self.col14 = col14
        self.Ttype=Ttype
        self.tableName = tableName
        self.DATA_SIZE = DATA_SIZE
        self.max_district = max_district
        self.max_facility = max_facility
        self.DATA_FILE = f"{self.tableName}.csv"
        self.Tablecolumns = []
        self.adr = ["Nausea","Vomiting","Diarrhea","Abdominal pain","Drowsiness","Dizziness","Irritability","Insomnia","Rash", "Itching","Hives"]

        # Iterate through columns from col1 to col14
        for col in [col1, col2, col3, col5, col6, col7, col8, col9, col10, col4, col11, col12, col13, col14]:
            if col is not None:
                self.Tablecolumns.append(col)
    
    def generate_district_list(self) -> list:
        return [f'DISTRICT{random.randint(100, 9990)}' for _ in range(random.randint(1,  self.max_district))]
    
    def generate_number(self, min, max) -> int:
        return random.randint(min, max)

    def generate_facility_list(self) -> str:
        return [f'FAC{random.randint(100, 9990)}' for _ in range(random.randint(1,  self.max_facility))]

    def save_to_csv(self, filename: str, data: dict) -> None:
        with open(filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            writer.writerow(data)

    def generate_records(self) -> dict:
        
        REGION = ['Ashanti','Brong Ahafo','Central','Eastern','Greater Accra','Northern','Upper East','Upper West','Volta','Western','Savannah','Bono East','Oti','Ahafo','Western North','North East']
        firstTwolined=2
        for yr in range(2018, 2024):
            for rg in REGION:
                district_list = self.generate_district_list()
                for ds in district_list:
                    facilities = self.generate_facility_list()
                   
                    if self.col4 is not None:

                        for fc in facilities:
                            for ci in range(1, 5):
            
                                col1x = yr
                                col2x = rg
                                col3x = ds
                                if self.Ttype == "ADR":
                                    col4x =  random.choice(self.adr)
                                if self.Ttype == "Registration":
                                    col4x=fc
                                if self.Ttype == "Blisters":
                                    col4x=self.generate_number(500, 2000)
                                col5x = ci
                                col6x = self.generate_number(1000, 10000)
                                col7x = self.generate_number(500, 2000)
                                col8x = self.generate_number(800, 5000)
                                col9x = self.generate_number(500, 2000)
                                col10x = self.generate_number(800, 5000)
                                row = {self.col1: col1x, self.col2: col2x, self.col3: col3x, self.col5: col5x, self.col6: col6x, self.col7: col7x, self.col8: col8x, self.col9: col9x}
                                
                                if self.col10 is not None:
                                    row[self.col10] = col10x
                                if self.col4 is not None:
                                    row[self.col4] = col4x
                                self.save_to_csv(self.DATA_FILE, row)
                    else:
                        for ci in range(1, 5):
                            col1x = yr
                            col2x = rg
                            col3x = ds
                            if self.Ttype == "ADR":
                                col4x =  random.choice(self.adr)
                            if self.Ttype == "Registration":
                                col4x=fc
                            if self.Ttype == "Blisters":
                                col4x=self.generate_number(500, 2000)
                            col5x = ci
                            col6x = self.generate_number(1000, 10000)
                            col7x = self.generate_number(500, 2000)
                            col8x = self.generate_number(800, 5000)
                            col9x = self.generate_number(500, 2000)
                            col10x = self.generate_number(800, 5000)
                            
                            row = {self.col1: col1x, self.col2: col2x, self.col3: col3x, self.col5: col5x, self.col6: col6x, self.col7: col7x, self.col8: col8x, self.col9: col9x}
                            if self.col4 is not None:
                                row[self.col4] = col4x
                            self.save_to_csv(self.DATA_FILE, row)

                            

    def writeToDoc(self):
        with open(self.DATA_FILE, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.Tablecolumns)
            writer.writeheader()
            for i in range(self.DATA_SIZE):
                self.generate_records()




if __name__ == '__main__':
  #table = Table(tableName="ADRTABLE", Ttype="ADR", col1="Year", col2="Region", col3="District",  col5="Cycle", col6="3 to 11 months male", col7="3 to 11 months female", col8="12 to 59 months male", col9="12 to 59 months female",col4="ADR Name")
 # table = Table(tableName="Registration", Ttype="Registration", col1="Year", col2="Region", col3="District",col5="Cycle", col6="Number of households",  col7="3 to 11 months male", col8="3 to 11 months female", col9="12 to 59 months male",col10="12 to 59 months female", col4="Facilities")
  table = Table(tableName="Blisters", Ttype="Blister", col1="Year", col2="Region", col3="District", col5="Cycle", col6="3 to 11 months male", col7="3 to 11 months female", col8="12 to 59 months male", col9="12 to 59 months female")
  table.writeToDoc()