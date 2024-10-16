# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define a = Character("An Phiast")
define f = Character("Fungie")
define p = Character("Priest")

transform bgspace:
    xalign 0.0,
    yalign 0.0,
    xysize(1920, 1080),

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.s

    scene bg map at bgspace

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show an phiast talking happy

    # These display lines of dialogue.

    a "Hey there! I'm An Phiast!"

    show an phiast happy

    a "Are you going to the Animation Dingle as well?"









    # This ends the game.

    return


