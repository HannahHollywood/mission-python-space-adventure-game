# SPACEWALK
# Listing 1-1

# creating variables to set the size of the game window
# using CONSTANT variables (uppercase) as these are not meant to change later
WIDTH = 800
HEIGHT = 600
# storing your position on the screen as you carry out the spacewalk
player_x = 600
player_y = 350

# defining a function that will create the backdrop of the games' title screen
# utilises the image files in the images folder
def draw():
    # screen.blit draws an image on the screen
    # to position the image we've used a tuple (numbers separated by a comma)
    # uses the x, y axis (with 0 being the top left corner)
    screen.blit(images.backdrop, (0, 0))
    # adding mars, astronaut & the ship and positioning them via a tuple
    screen.blit(images.mars, (50, 50))
    screen.blit(images.astronaut, (player_x, player_y))
    screen.blit(images.ship, (550, 300))

# creating the player movement depending on keystrokes
# because the players need to be accessed via both the draw() and game_loop functions
# we set them up as global variables
def game_loop():
    global player_x, player_y
    if keyboard.right:
        # += means 'increase by'
        player_x += 5
    elif keyboard.left:
        # -= means 'decrease by'
        player_x -= 5
    elif keyboard.up:
        player_y -= 5
    elif keyboard.down:
        player_y += 5

# sets the speed at which the astronaut moves around on screen
clock.schedule_interval(game_loop, 0.03)
