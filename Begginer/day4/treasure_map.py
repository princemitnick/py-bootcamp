

row1 = ["🌫", "🌫", "🌫"]
row2 = ["🌫", "🌫", "🌫"]
row3 = ["🌫", "🌫", "🌫"]


print(f"{row1}\n{row2}\n{row3}")
treasure_map = [row1, row2, row3]

where_to_put_treasure = input("Where do you want to put the treasure : ")
column = int(where_to_put_treasure[0])
line = int(where_to_put_treasure[1])

treasure_map[line-1][column-1] = "X"

print("Here we are")
print(f"{row1}\n{row2}\n{row3}")



'''
row4 = ["a", "b", "c"]
row5 = ["d", "e", "f"]
row6 = ["g", "h", "i"]



map2 = [row4, row5, row6]
column = 3
line = 1

map2[line-1][column-1] = "X"

print(f"{row4}\n{row5}\n{row6}")

print(map2[line-1][column-1])
'''








#print(map)