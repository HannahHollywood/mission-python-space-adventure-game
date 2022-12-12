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
    screen.blit(images.backdrop, (0, 0))
    # adding mars & the ship and positioning them via a tuple
    screen.blit(images.mars, (50, 50))
    screen.blit(images.ship, (130, 150))
