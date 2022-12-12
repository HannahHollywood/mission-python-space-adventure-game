room_map = [ [1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 1, 1, 0, 0, 0, 0],
             [1, 0, 0, 0, 1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 0, 0, 0, 1, 1, 1]
        ]

WIDTH = 800
HEIGHT = 800

top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar]

# these variables store the size of our rooms
# and tell how many times Python should repeat the loops
room_height = 9
room_width = 9

def draw():
    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = DEMO_OBJECTS[room_map[y][x]]
            screen.blit(image_to_draw,
                # placing the location of the images (floor/pillar) on the x/y axis
                (top_left_x + (x * 30),
                top_left_y + (y * 30) - image_to_draw.get_height()))