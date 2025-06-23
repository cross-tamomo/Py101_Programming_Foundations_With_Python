SQUARE_METERS_TO_SQUARE_FEET = 10.7639
length = float(input('Enter the length of the room (in meters): '))
width = float(input('Enter the width of the room (in meters): '))
area_square_meter = length * width
area_square_feet = SQUARE_METERS_TO_SQUARE_FEET * area_square_meter
print(f'The area in square meters is {area_square_meter:.2f} and area in square feet is {area_square_feet:.2f}')