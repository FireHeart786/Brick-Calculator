def calculate_bricks(length, width, height, brick_length, brick_width, area_openings):
    # Calculate the area of the wall
    area_wall = length * height * 2 + width * height * 2

    # Deduct the area of openings from the wall area
    area_wall -= area_openings

    # Calculate the area of one brick
    area_brick = brick_length * brick_width

    # Calculate the number of bricks required
    num_bricks = int(area_wall / area_brick)

    return num_bricks

length = float(input("Enter the Length of wall in meters: ")) 
width = float(input("Enter the width of wall in meters: ")) 
height = float(input("Enter the height of wall in meters: ")) 
brick_length =float(input("Enter the Length of Bricks in meter: "))
brick_width = float(input("Enter the Width of Bricks in meter: ")) 
area_openings =float(input("Enter the area of openings in sqm: "))

num_bricks = calculate_bricks(length, width, height, brick_length, brick_width, area_openings)
print("Number of bricks required:", num_bricks)
