# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")  #character customizable stats: font size, font colour, text box (image background or none), bold, italic, font family, outlines, dropshadow 
define a = Character("An Phiast")   #using who_ and what_
define f = Character("Fungie")
define c = Character("St. Cuan")
define n = Character("You")
define n_thought = Character("You", what_italic =True)
define u = Character("???")

define fast_fade = Dissolve(0.5)
define slow_fade = Dissolve(1.5)




#g "Looks like they're{nw}"
#show trebuchet
#g "Looks like they're{fast} playing with their trebuchet again."    

#nw - instantly goes to next line
#fast - everything before it starts displayed

# define APRelationship = 0;


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

    scene dingle town
    with   fast_fade

    "before you know it, you arrive at Dingle town."
    "The weather is surprisingly warm today, although your professors let you know that it won't stay that way."
    "The kickoff event of Animation Dingle starts tomorrow. you're not really sure what to do."
    "Just waiting in the hotel seems like a waste. And all your classmates already headed off somewhere."
    "guess it's time to explore the town a little."

    scene street_beach_fence
    with fast_fade

    "You wander around, mostly following the view"
    n_thought"The bay looks wonderful."
    "You sit in the grass for a little bit, taking in the view."
    "You didn't really get to sleep much, you had to wake up early for the bus, and couldn't fall asleep while on it."
    n "Yawn..."
    "And before you know it, you're slowly..."
    "falling... {w=1.0} "
    scene black_screen
    with fast_fade
    "asleep...{w=1.0}\n ...{w=1.0} \n ..."
    

    scene street_beach_fence
    with hpunch
    u "Heya!"
    n "{w=0.3}Huh??"
    
    show an phiast happy 
    with hpunch
    u "Oh, I'm sorry, did I startle you?"
    
    show an phiast  unhappy 
    with hpunch
    
    n "{w=0.1}???????"
    with vpunch
    n_thought "What the heck is this sea monster??" 
    with vpunch
    "You reach into you bag for-"
    u "Whoa, whoa, whoa!" 
    u "I'm not gonna hurt you!"
    show an phiast unhappy:
        xalign 0.5 yalign 1.0
        linear 0.3 yalign 1.1
    u "Sorry for scaring you like that, I just thought I would walk by and say hello"
    n_thought "What... Who is this... thing? creature?"
    show an phiast unhappy:
        xalign 0.5 yalign 1.1
        linear 1.5 xalign 1.5
    u "Okay, um. I'm just gonna go then. {w=0.3}  {i} Gosh this is awkward...{/i}"
    with vpunch
    n "Wait!"
    
    n_thought "They seem friendly enough, and you're actually kind of curious"
    show an phiast unhappy: 
        xalign 1.5 yalign 1.1
        linear 1.0 xalign 0.5

    n "{w=0.3}...What's your name?"
    u "..."
    show an phiast happy
    a "...{w=0.3}I'm An Phiast"
    n "Sorry if I seemed unfriendly. I've just never met someone...{w=0.3} like you before."
    a "Oh, I get that a lot."
    show an phiast talking happy
    a "Apology accepted!"
    show an phiast happy
    a"{w=0.3} ..."
    "You both look at each other, awkwardly.{w=0.2} Now that you started a conversation, you're not sure what to talk about."
    n"..."
    n "{w=0.3}...You know, I'm here for the Animation Dingle tomorrow, and I need to kill some time before it starts tomorrow... "
    n "{w=0.3}...do you want to walk around town a little bit?"
    show an phiast happy:
        xalign 0.5 yalign 1.1
        linear 0.3 yalign 1.0
    "an phiast perks up!"
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
    "ignoring that little hiccup, you continue"
    n "Great! I actually have a-"
    "but before you can continue your thought..."
    


    

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
    "Fungie ignores him and instead, he turns to you."
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
        f "Oh, I see how it is."
        f "Very well.{w=0.4} enjoy your time with the sea monster. Everyone knows they're soooo inteligent."
        with vpunch
        a "Hey!" 
        f "Anyways.{w=0.4} I can't kick you out of Dingle, but that doesn't mean you're welcome."
        f "There's only one mascot in Dingle, and that is {i}Me!{/i}"
        f "And I will make sure it stays that way."
        jump after_choice_prologue_1

    label choice_prologue_1_whoareyou:
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
        "And just like that, Fungie speeds off."
        a "soo...{w=0.5} that's Fungie."
        a "He...{w=0.2} doesn't like me."
        n "What is his deal?"
        a "He's the famous dolphin of Dingle. The people love him here. He's like their mascot"
        a "He thinks I'm out to steal his title or something. I dunno."
        a "Anyways, I don't really want to talk about that right now. Let's just go somewhere else."

        n_thought "What was all that about???"
        n_thought "Fungie seems so hostile towards him, but you can't see why."
        n_thought "What did you get yourself into..."
        "You let it go for now, before you remember once again"
        n "Oh yeah! here, have a look."
    
        
        scene dingle map at bgspace
        with fast_fade
        
            
        n "Our professors gave us this map. The Hotel where the Animation Dingle is taking place is a bit out of town."
        scene darkened map at bgspace
        with fast_fade
        n"for now, we could see where we wanna go. I can already see a few clear options..."

        label map_screen:  
            scene darkened map at bgspace
            with fast_fade
            "Click where you would like to go!"
            call screen MapUI      # call the buttons
            



label bay_pressed:
    scene dingle bay at bgspace
    with fast_fade
    
    show an phiast talking happy
    with fast_fade
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
        show an phiast happy
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
        show an phiast offscreen_right
        show an phiast cg at bgspace
        a "...That's SO hardcore."                                                                                                      
        jump after_choice_bay_1


    label after_choice_bay_1:
        scene bay sea view at bgspace
        with fast_fade
        "You both set up your fishing rods and take in the view of the sea in front of you."
        "An Phiast seems happy just watching the view, but you can't help but start a conversation."
        "After all, you still don't know much about him, and this seems like the perfect opportunity."
        n_thought"..."
        menu:

            "What do you usually do when you wait for a bite?":
                jump choice_bay_2_question
            "So about Fungie...":
                jump choice_bay_2_fungie
            "What kind of fish are here?":
                jump choice_bay_2_fish
            "{i}stay silent{/i}":
                jump choice_bay_2_silent


    label choice_bay_2_question:

        show an phiast happy:
            xalign 0.65 yalign 1.0
        with fast_fade

        a"oh?"
        a"..."
        a"I usually just think about stuff..."
        a"It's really calming, you know? I get a chance to sort through my thoughts, or think about my other hobbies."
        n "Other hobbies? like what?"
        a"Well, you're probably not gonna be surprised when I say this, but..."
        show an phiast talking happy
        a"I'm a bit of an artist."
        a"I like to draw, i even tried animating a little, but that's not really my specialty."
        show an phiast happy
        a"That would be writing. I even brought a notebook with me!"
        n"Do you usually write while fishing?"
        a"Yeah! it's great for that. I just didn't want to start scribbling and being in my own little bubble while I'm here with you, {w=0.2} y'know?"
        "An phiast stares into your eyes for a second, before turning back to the sea."
        scene bay sea view at bgspace
        "..."
        "This is great."


        jump after_choice_bay_2
    
    label choice_bay_2_fungie:
        show an phiast unhappy:
            xalign 0.65 yalign 1.0
        with fast_fade
        a"oh?"
        a "I suppose you want to know more about why we're fighting."
        a "When I first came into town, it was different."
        a "It was same as this year. I came a few days before the Animation Dingle, and we met."
        a "We got on much better back then."
        show an phiast happy
        a "He can be charming when he wants to."
        show an phiast unhappy
        a "...{w=0.5}"
        a "Anyways, when it came to animation Dingle, we went together."
        show an phiast happy
        a "I didn't expect my face to be plastered everywhere. It was... {w=0.5}nice."
        show an phiast angry
        a "But Fungie didn't think so."
        a "I thought that this was something we both have in common - We're mascots."
        show an phiast unhappy
        a "But I think he saw it as an attack."
        a "I know how much Dingle means to him. He used to also be an outcast, until he came here. {w=0.5} It means a lot to him."
        show an phiast angry
        a "But that doesn't mean he can push me around..."
        show an phiast unhappy
        a "And to think we could have been friends if it wasn't for that."
        "An Phiast pauses."
        "You get the feeling like he never had the chance to tell this to anyone."
        n "I'm sorry that's how things turned out between you two."
        a "It's alright."
        "You both turn back towards the sea."
        scene bay sea view at bgspace
        with fast_fade
        "..."




        jump after_choice_bay_2

    label choice_bay_2_fish:

        "fish convo TBA"
        
        jump after_choice_bay_2


    label choice_bay_2_silent:

        "silent convo TBA"

        jump after_choice_bay_2


    label after_choice_bay_2:

        "You feel like you understand An Phiast a little more."
        "{w=1.5}...You both stay there for a while, hoping to catch some fish. but unfortunately, nothing bites."
        show an phiast unhappy
        with fast_fade
        a "I think I see Fungie in the water..."
        a "I'd rather not talk to him right now. Do you want to go somewhere else before he sees us?"
        "You pull up you town map again."
        n "Let's see..."
        
    jump after_house_choice
























label town_pressed:
    scene dingle town at bgspace
    "Welcome to the town! I hope you like colourful houses!"
    jump after_house_choice


label tourist_pressed:
    scene dingle town at bgspace
    "House 3 was pressed!"
    jump after_house_choice


label church_pressed:
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


