# data_tuple = ()
#
# with open("weather_data.csv") as data_file:
#     data = data_file.readline()
#     print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for x in data:
        if x[1] != "temp":
            temperatures.append(x[1])

for temp in temperatures:
    print(temp)