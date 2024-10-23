# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")  #character customizable stats: font size, font colour, text box (image background or none), bold, italic, font family, outlines, dropshadow 
define a = Character("An Phiast")   #using who_ and what_
define f = Character("Fungie")
define c = Character("St. Cuan")
define n = Character("You")
define n_thought = Character("You", what_italic =True)

define fast_fade = Dissolve(0.5)

transform middle:
    linear 0.3 xalign 0.5
    yalign 1.0

transform little_left:
    linear 0.3 xalign 0.2
    yalign 1.0

transform little_right:
    linear 0.3 xalign 0.8
    yalign 1.0

transform full_left:
    linear 0.3 xalign 0.0
    yalign 1.0

transform full_right:
    linear 0.3 xalign 1.0
    yalign 1.0

transform offscreen_right:
    linear 0.3 xalign 2.0
    yalign 1.0

transform offscreen_left:
    linear 0.3 xalign -1.0
    yalign 1.0




transform look_left:
    xzoom 1.0 yzoom 1.0



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

    "It's your third year of college, and your lecturers arranged for your class to go to Animation Dingle."
    "You're not exactly sure what the event is about, but you like art, and apparently animators from all over are going to be there!"

    show bus_window_windmill at bgspace
    with fast_fade

    "While on the bus, you start to think to yourself."
    n_thought"A bit of a strange place to get together. It's on the exact opposite coast from Dublin, in the middle of the countryside."
    n_thought"how did all the animators from america get there?"
    n_thought"we're lucky the college ordered this bus, otherwise it would be impossible"
    n_thought"Too bad my friends couldn't come. There's my classmates, sure, but I've never really talked to them... "
    n_thought"hopefully it won't get too lonely."

    n_thought"..."

    n_thought"at least the views are lovely."

    show dingle town at bgspace 
    with   fast_fade

    "before you know it, you arrive at Dingle town."
    "The weather is surprisingly warm today, although your professors let you know that it won't stay that way."
    "You still have plenty of time before the kickoff event of Animation Dingle starts. you're not really sure what to do."
    "Just waiting in the hotel seems like a waste. And all your classmates already headed off somewhere."
    "guess it's time to explore the town a little."




    show an phiast talking happy 
    
    with vpunch

    
    a "pekaboo!"
    n "AAAAAAAAAAAAAA!"
    a "yo chill, i'm an phiast. I'm your new friend. wana explore Dingle town? sure, let's go! let's go!"
    a "btw i'm the mascot of Animation Dingle in case you didnt know. so, yea."

    show fungie smug at offscreen_right

    show an phiast unhappy:
        xalign 0.5 yalign 1.0
        linear 0.3 xalign 0.2
        xzoom -1.0


    

    show fungie smug:
        xalign 2.0 yalign 1.0
        linear 0.3 xalign 0.8

        
    with vpunch
    
    f "yo bitches this is my town"
    f "An Phiast? pffft. more like sore loser-Phiast."
    f "don't even try taking over my town."
    f "anyways cya"
    show fungie smug at offscreen_left
    show an phiast unhappy at middle

    a "soo... that Fungie."
    a "yeah he's a bit of a dick."
    a "anyways, let's go!"

    n_thought "What was all that about???"



    

    

    

    

    

    


   
    
    scene dingle map at bgspace
       
        
    n "Our professors gave us this map of the town. The Hotel where the Animation Dingle is taking place is a bit out of town."
    scene darkened map at bgspace
    with fast_fade
    n"for now, let's explore the town. I can already see a few clear options..."

    label map_screen:  
        scene darkened map at bgspace
        with fast_fade
        call screen MapUI      # call the buttons



label bay_pressed:
    scene dingle bay at bgspace
    
    show an phiast talking happy
    a "This is the bay!"
    a "I like to ge here every once in a while to fish."
    show an phiast unhappy
    a "well, until Fungie shows up, usually. He likes to swim around the boats here, getting gawked at by people."
    show an phiast happy
    a "but that's besides the point. Have you ever fished before?"

    menu:

        "My brother used to fish, i came with him a few times.":
            jump choice_bay_1_medium
        "I've never held a rod in my life.":
            jump choice_bay_1_no
        "I'm a fishing machine!":
            jump choice_bay_1_yes


    label choice_bay_1_medium:

        show an phiast happy 
        a "Oh that's nice! so you at least know the basics, right?"
        a "I'll spare you the nitty gritty then, But if you need to know anything, just ask."
        jump after_choice_bay_1
    
    label choice_bay_1_no:
        show an phiast blush
        a "Well let's change that then! it's not too hard."
        show an phiast talking happy
        a "You neeed to put your bait on the hook first, and the you cast the line."
        show an phiast happy
        a "These waters are pretty rich with fish, so hopefully we won't have to wait too long before something bites."
        show an phiast talking happy
        a "That's when the best part starts, You gotta reel it in! but careful not to snap the line!"
        a "and then we'll have a nice fish!"
        jump after_choice_bay_1

    label choice_bay_1_yes:
        show an phiast unhappy
        a "Whoa, dude that's..."
        show an phiast blush
        a "...That's SO hardcore."
        jump after_choice_bay_1


    label after_choice_bay_1:
        show bay sea view at bgspace
        "You both set up your fishing rods and take in the view of the sea in front of you."
        "An Phiast seems happy just watching the view, but you can't help but start a conversation."
        "After all, you still don't know much about him, and this seems like the perfect opportunity."





    



    jump after_house_choice
























label town_pressed:
    scene dingle town at bgspace
    "Welcome to the town! I hope you like colourful houses!"
    jump after_house_choice


label tourist_pressed:
    scene dingle town at bgspace
    "House 3 was pressed!"
    jump after_house_choice


label church_pressed_pressed:
    scene dingle town at bgspace
    "House 4 was pressed!"
    jump after_house_choice


label house5_pressed:
    scene dingle town at bgspace
    "House 5 was pressed!"
    "This is a test button. back to the map you go!"
    jump map_screen










label after_house_choice:
    "Let's take a look at the map again..."
    jump map_screen








    # This ends the game.

    return


