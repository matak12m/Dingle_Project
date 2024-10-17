# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define a = Character("An Phiast")
define f = Character("Fungie")
define c = Character("St. Cuan")
define n = Character(" ")

define fast_fade = Dissolve(0.5)


transform bgspace:
    xalign 0.0,
    yalign 0.0,
    xysize(1920, 1080),

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.s

    show bus inside at bgspace
    with fast_fade


    # These display lines of dialogue.

    n "It's your third year of college, and your lecturers arranged for your class to go to Animation Dingle."
    n"You're not exactly sure what the event is about, but you like art, and apparently animators from all over are going to be there!"

    show bus_window_windmill at bgspace
    with fast_fade

    n"A bit of a strange place to get together. It's on the exact opposite coast from Dublin, in the middle of the countryside."
    n"how did all the animators from america get there?"
    n"you're lucky your college ordered this bus, otherwise it would be impossible for you."
    n"unfortunately, your friends couldn't come. There's your classmates, sure, but you don't really talk to them... "
    n"hopefully it won't get too lonely."

    n"..."

    n"at least the views are lovely."

    show dingle town at bgspace 
    with   fast_fade

    show an phiast talking happy 
    
    with vpunch

    
    a "pekaboo!"
    
    

    

    

    

    

    


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


