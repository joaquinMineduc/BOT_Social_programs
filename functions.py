from datetime import datetime
import os

def get_last_four_years():
    list_years = []
    year = datetime.now().year -1
    for year_less in range(4):
        temp = year - year_less
        list_years.append(temp)
    return list_years  

