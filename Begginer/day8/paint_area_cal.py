print("Paint Area Calculator")

def paint_cal(h, w, c):
    return round((h * w) / c)

height = int(input("Height of wall : "))
width = int(input("Width of wall : "))

coverage  = 5

print(paint_cal(height, width, coverage))