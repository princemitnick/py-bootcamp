import pandas

data = pandas.read_csv("weather_data.csv")


# Convert DataFrame to Dictionary

# data_dict = data.to_dict()
#
# temp_list = data['temp'].to_list()
#
#
# # Average
#
# print(f"Average : { round((sum(temp_list) / len(temp_list)), 2)}")
# print(round((data['temp'].mean()), 2))
#
# # Max value
#
# print(data['temp'].max())
#
# # Get Data in column
# print(data['condition'].to_list())
# print(data.condition.to_list())

# Get Data in Row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# print(data[data.temp == data.temp.min()])
#
# monday = data[data.day == "Monday"]
#
# print(type(monday.condition))

monday = data[data.day == "Monday"]

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32

print(monday_temp_F)

# Create a DataFrame from Scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [67, 89., 35]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")