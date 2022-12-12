room_map = [ [1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 1, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]
        ]

# we've used a for loop command to repeat the piece of code a certiain number of times
for y in range(7):
    for x in range(5):
        # we want it to loop through and show each map spot on the y & x axis'
        # [x] and [y] are lists here as above
        # printing it this way will remove the square brackets
        print(room_map[y][x], end="")
        # we put end="" at the end so that it doesn't add a line after each index 
    print()

# print out a distress call 3 times
##for distress_message in range(3):
##    print("Mayday!")
