# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define a = Character("An Phiast")
define f = Character("Fungie")
define c = Character("St. Cuan")
define n = Character(" ")

transform bgspace:
    xalign 0.0,
    yalign 0.0,
    xysize(1920, 1080),

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.s

    scene dingle bay at bgspace

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show an phiast talking happy

    # These display lines of dialogue.

    a "Hey there! I'm An Phiast!"

    show an phiast happy

    a "Are you going to the Animation Dingle as well?"

    n "An Phiast seems eager to show you around! But where would you like to go?"

    

    n "let'see"


    # call the screen with the map and buttons
    label map_screen:
        scene dingle map at bgspace
        call screen MapUI
        
        n " "
    

label house1_pressed:
    scene dingle bay at bgspace
    
    show an phiast talking happy
    a "This is the bay!"
    a "I like to ge here every once in a while to fish. Here, I can show you how it's done!"
    jump after_house_choice


label house2_pressed:
    scene dingle town at bgspace
    "Welcome to the town! I hope you like colourful houses!"
    jump after_house_choice


label house3_pressed:
    scene dingle town at bgspace
    "House 3 was pressed!"
    jump after_house_choice


label house4_pressed:
    scene dingle town at bgspace
    "House 4 was pressed!"
    jump after_house_choice


label house5_pressed:
    scene dingle town at bgspace
    "House 5 was pressed!"
    jump after_house_choice




label after_house_choice:
    "This was fun, but let's move on!"
    jump map_screen








    # This ends the game.

    return


