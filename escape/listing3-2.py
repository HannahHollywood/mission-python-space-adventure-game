room_map = [ [1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]
        ]

# we've used a for loop command to repeat the piece of code a certiain number of times
# print each item in our map (which we've called 'y') (up to index 6 (excluding 7))
for y in range(7):
    print(room_map[y])

# print out a distress call 3 times
for distress_message in range(3):
    print("Mayday!")
