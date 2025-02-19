# This file contains the Game Map data

import time, random, math

###########
#VARIABLES#
###########

WIDTH = 800 #window size
HEIGHT = 800

#Player variables
PLAYER_NAME = "Hannah" 
FRIEND1_NAME = "Maria" 
FRIEND2_NAME = "Marlyn" 
current_room = 31 # start at room = 31

# this specifies where to start drawing the room
top_left_x = 100
top_left_y = 150

# image files to be displayed in the rooms
DEMO_OBJECTS = [images.floor, images.pillar, images.soil]

###########
##  MAP  ##
###########

MAP_WIDTH = 5
MAP_HEIGHT = 10 
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT

GAME_MAP = [ ["Room 0 - where unused objects are kept", 0, 0, False, False] ]

outdoor_rooms = range(1, 26)
# below generates rooms 1 - 25 which are all the dusty planet surface (so repeated)
for planetsectors in range(1, 26):
    GAME_MAP.append( ["The dusty planet surface", 13, 13, True, True] )

# adding rooms 26 - 50 to the Game Map by adding them to the list
GAME_MAP  += [
        #["Room name", height, width, Top exit?, Right exit?]
        ["The airlock", 13, 5, True, False], # room 26
        ["The engineering lab", 13, 13, False, False], # room 27
        ["Poodle Mission Control", 9, 13, False, True], # room 28
        ["The viewing gallery", 9, 15, False, False], # room 29
        ["The crew's bathroom", 5, 5, False, False], # room 30
        ["The airlock entry bay", 7, 11, True, True], # room 31
        ["Left elbow room", 9, 7, True, False], # room 32
        ["Right elbow room", 7, 13, True, True], # room 33
        ["The science lab", 13, 13, False, True], # room 34
        ["The greenhouse", 13, 13, True, False], # room 35
        [PLAYER_NAME + "'s sleeping quarters", 9, 11, False, False], # room 36
        ["West corridor", 15, 5, True, True], # room 37
        ["The briefing room", 7, 13, False, True], # room 38
        ["The crew's community room", 11, 13, True, False], # room 39
        ["Main Mission Control", 14, 14, False, False], # room 40
        ["The sick bay", 12, 7, True, False], # room 41
        ["West corridor", 9, 7, True, False], # room 42
        ["Utilities control room", 9, 9, False, True], # room 43
        ["Systems engineering bay", 9, 11, False, False], # room 44
        ["Security portal to Mission Control", 7, 7, True, False], # room 45
        # Adding friend names to the name of the room via a string
        [FRIEND1_NAME + "'s sleeping quarters", 9, 11, True, True], # room 46
        [FRIEND2_NAME + "'s sleeping quarters", 9, 11, True, True], # room 47
        ["The pipeworks", 13, 11, True, False], # room 48
        ["The chief scientist's office", 9, 7, True, True], # room 49
        ["The robot workshop", 9, 11, True, False] # room 50
        ]

#simple sanity check on map above to check data entry
# we do this because we didn't include room 0 when we calculated the map size
assert len(GAME_MAP)-1 == MAP_SIZE, "Map size and GAME_MAP don't match"
