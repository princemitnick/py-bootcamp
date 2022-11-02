import colorgram

colors = colorgram.extract('images.jpg', 6)

first_color = colors[0]

print(first_color.rgb.r)