# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define e = Character("Eileen", window_background=Frame("gui/textbox.png"))  #character customizable stats: font size, font colour, text box (image background or none), bold, italic, font family, outlines, dropshadow 
define a = Character("An Phiast", window_background=Frame("gui/textboxGreen.png"), color = '#004418', what_font = "RujisHandwritingFontv.2.0.ttf")   #using who_ and what_
define f = Character("Fungie", window_background=Frame("gui/textboxGrey.png"),color = '#45455c', what_font = "ArchitectsDaughter.ttf" ,what_size = 33)
define c = Character("St. Cuan", window_background=Frame("gui/textbox.png"))
define player = Character("You", window_background=Frame("gui/textbox.png"))
define n = Character("", what_italic = True, window_background=Frame("gui/thoughtbox.png"))
define u = Character("???", window_background=Frame("gui/textbox.png"))
define n = Character("", window_background=Frame("gui/thoughtbox.png"))
define fast_fade = Dissolve(0.5, window_background=Frame("gui/textbox.png"))
define slow_fade = Dissolve(1.5, window_background=Frame("gui/textbox.png"))
define ver_slow_fade = Dissolve(5, window_background=Frame("gui/textbox.png"))



#g "Looks like they're{nw}"
#show trebuchet
#g "Looks like they're{fast} playing with their trebuchet again."    

#nw - instantly goes to next line
#fast - everything before it starts displayed


#Relationship values to keep track of which ending the player receives.
#of note, the relationship doesnt increase over and over if the player goes back and selects the same choice

define APRelationship = 1

define FRelationship = 1

define TimeProgress = 0

define FungieTime = "false"

define WentToChurch = "false"
define WentToBay = "false"
define WentToTown = "false"
define WentToTouristCenter = "false"




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

window show

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.s

    show bus inside at bgspace
    with fast_fade
   
    play music "audio/soft-jazz-piano-music-233868.mp3" fadeout 1
    # These display lines of dialogue.
    

    n "It's your third year of college, and your lecturers arranged for your class to go to Animation Dingle."
    n "You're not exactly sure what the event is about, but you like art, and apparently animators from all over are going to be there!"

    show bus_window_windmill at bgspace
    with fast_fade

    n "While on the bus, you start to think to yourself."
    n "A bit of a strange place to get together. It's on the exact opposite coast from Dublin, in the middle of the countryside."
    n "how did all the animators from america get there?"
    n "we're lucky the college ordered this bus, otherwise it would be impossible"
    n "Too bad my friends couldn't come. There's my classmates, sure, but I've never really talked to them... "
    n "hopefully it won't get too lonely."

    n "..."

    n "at least the views are lovely."

    scene dingle town
    with   fast_fade

    n "before you know it, you arrive at Dingle town."
    n "The weather is surprisingly warm today, although your professors let you know that it won't stay that way."
    n "The kickoff event of Animation Dingle starts tomorrow. you're not really sure what to do."
    n "Just waiting in the hotel seems like a waste. And all your classmates already headed off somewhere."
    n "guess it's time to explore the town a little."

    scene street_beach_fence
    with fast_fade

    n "You wander around, mostly following the view"
    n "The bay looks wonderful."
    n "You sit in the grass for a little bit, taking in the view."
    n "You didn't really get to sleep much, you had to wake up early for the bus, and couldn't fall asleep while on it."
    player "Yawn..."
    n "And before you know it, you're slowly..."
    n "falling... {w=1.0} "
    scene black_screen
    with fast_fade
    n "asleep...{w=1.0}\n ...{w=1.0} \n ..."
    

    scene street_beach_fence
    with hpunch
    u "Heya!"
    player "{w=0.3}Huh??"
    
    show an phiast happy 
    with hpunch
    u "Oh, I'm sorry, did I startle you?"
    
    show an phiast  unhappy 
    with hpunch
    
    player "{w=0.1}???????"
    with vpunch
    n  "What the heck is this sea monster??" 
    with vpunch
    n "You reach into you bag for-"
    u "Whoa, whoa, whoa!" 
    u "I'm not gonna hurt you!"
    show an phiast unhappy:
        xalign 0.5 yalign 1.0
        linear 0.3 yalign 1.1
    u "Sorry for scaring you like that, I just thought I would walk by and say hello"
    n  "What... Who is this... thing? creature?"
    show an phiast unhappy:
        xalign 0.5 yalign 1.1
        linear 1.5 xalign 1.5
    u "Okay, um. I'm just gonna go then. {w=0.3}  {i} Gosh this is awkward...{/i}"
    with vpunch
    player "Wait!"
    
    n  "They seem friendly enough, and you're actually kind of curious"
    show an phiast unhappy: 
        xalign 1.5 yalign 1.1
        linear 1.0 xalign 0.5

    player "{w=0.3}...What's your name?"
    u "..."
    show an phiast happy
    a "...{w=0.3}I'm An Phiast"
    player "Sorry if I seemed unfriendly. I've just never met someone...{w=0.3} like you before."
    a "Oh, I get that a lot."
    show an phiast talking happy
    a "Apology accepted!"
    show an phiast happy
    a"{w=0.3} ..."
    n "You both look at each other, awkwardly.{w=0.2} Now that you started a conversation, you're not sure what to talk about."
    player"..."
    player "{w=0.3}...You know, I'm here for the Animation Dingle tomorrow, and I need to kill some time before it starts tomorrow... "
    player "{w=0.3}...do you want to walk around town a little bit?"
    show an phiast happy:
        xalign 0.5 yalign 1.1
        linear 0.3 yalign 1.0
    n "an phiast perks up!"
    a "Oh!"
    a "Now that's a coincidence!"
    show an phiast talking happy
    a "I'm actually kind of the mascot of Animation Dingle!"
    show an phiast happy
    a "I come by every year, It's like a little tradition."
    show an phiast unhappy
    a "Although I can't exactly say people here are used to me..."
    show an phiast happy
    a "But yeah! I would love to just walk around town with someone!{w=0.3} ...I mean...{w=0.1} you!"
    n "ignoring that little hiccup, you continue"
    player "Great! I actually have a-"
    n "but before you can continue your thought..."
    


    

    show fungie smug at offscreen_right

    show fungie smug:
        xalign 2.0 yalign -1.0
        linear 0.2 xalign 0.7
    with vpunch

    show an phiast unhappy:
        xalign 0.5 yalign 1.0
        linear 0.2 xalign -0.2
        xzoom -1.0


    

    

    u "Oh.{w=1.0}  You're here."
    u "Guess it's that time of year again, huh?"
    u "Just make sure not to scare anymore people this year."
    a "Ugh.{w=0.2}  leave me alone, Fungie."
    f "Well, I have to look after my people, don't I?"
    f "This is my town, An Phiast.{w=0.4}  I don't want you making a mess."
    a "You do this every year, Fungie.{w=0.2} I don't need to hear your lectures."
    n "Fungie ignores him and instead, he turns to you."
    f "I don't believe I've seen you around.{w=0.4} Are you new here?{w=0.4} Is he bothering you?"

    menu:

        "I came for the Animation Dingle.":
            jump choice_prologue_1_AD
        "No, leave him alone.":
            jump choice_prologue_1_leave
        "Who are you?":
            jump choice_prologue_1_whoareyou

    
    label choice_prologue_1_AD:
        
        f "Oh, you're one of them?"
        f "I'm sorry,{w=0.4} I mistook you for someone else."
        f "You might think you can just bring An Phiast-boy over here and take over me and my town, but you're wrong."
        f "Don't forget, Dingle is letting {i}You{/i} be here.{w=1.0} Not the other way around."
        jump after_choice_prologue_1

    label choice_prologue_1_leave:
        $APRelationship +=1;
        $ FRelationship -=1;
        f "Oh, I see how it is."
        f "Very well.{w=0.4} enjoy your time with the sea monster. Everyone knows they're soooo inteligent."
        with vpunch
        a "Hey!" 
        f "Anyways.{w=0.4} I can't kick you out of Dingle, but that doesn't mean you're welcome."
        f "There's only one mascot in Dingle, and that is {i}Me!{/i}"
        f "And I will make sure it stays that way."
        jump after_choice_prologue_1

    label choice_prologue_1_whoareyou:
        $ FRelationship+=1;
        f "Oh, where are my manners. I'm Fungie.{w=0.4} Fungie the Dolphin."
        f "Surely you've heard of me? I'm basically the guardian of Dingle!"
        f "Guarding it from sea monsters like An Phiast here."
        show an phiast angry
        with vpunch
        a "Hey!" 
        f "Anyways, this is my town. Make sure you remember that."
        f "There's space for only one mascot in Dingle."
        jump after_choice_prologue_1




    label after_choice_prologue_1:

        show fungie smug at offscreen_left
        show an phiast unhappy at middle
        n "And just like that, Fungie speeds off."
        a "soo...{w=0.5} that's Fungie."
        a "He...{w=0.2} doesn't like me."
        player "What is his deal?"
        a "He's the famous dolphin of Dingle. The people love him here. He's like their mascot"
        a "He thinks I'm out to steal his title or something. I dunno."
        a "Anyways, I don't really want to talk about that right now. Let's just go somewhere else."

        n "What was all that about???"
        n "Fungie seems so hostile towards him, but you can't see why."
        n "What did you get yourself into..."
        n "You let it go for now, before you remember once again"
        player "Oh yeah! {w=0.3} here, have a look."
    
        
        scene dingle map at bgspace
        with fast_fade
        
            
        player "Our lecturers gave us this map. The Hotel where the Animation Dingle is taking place is a bit out of town."
        scene darkened map at bgspace
        with fast_fade
        player"for now, we could see where we wanna go. I can already see a few clear options..."
        stop music fadeout 1.0

        label map_screen:  
            scene darkened map at bgspace
            with fast_fade
            call screen MapUI      # call the buttons
        









