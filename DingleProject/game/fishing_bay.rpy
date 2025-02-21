# Fishing bay script.
# TBA: final dialogue tree responses


#xalign 0.5 yalign 1.0
#linear 0.3 yalign 1.1
# easein 0.3 xalign 0.4
#             easeout 0.1 xalign 0.5
#             linear 0.2 xzoom -1.0
#             pause 1.0
#             easein 0.1 yalign 1.2
#             linear 0.2 xzoom 1.0
#             pause 0.1
#             easeout 0.3 yalign 1.0

label bay_pressed:
    if(WentToBay==True):
        n "I think I've seen enough there, let's go somewhere else for a change!"
        jump map_screen
    


label bay_scene:
    
    show street_beach_fence at bgspace with Fade(0.0, 0.3, 2.5)
    if (FungieTime==True):
        show an phiast happy:
            xalign 0.5 yalign 1.1
            easein 0.1 yalign 1.0
            easein 0.1 yalign 1.1
        a "Oh, there you are!"
        player "Hey, I'm sorry about that..."
        show an phiast somber:
            easein 0.1 yalign 1.1
        a "It's fine."
        a "I don't want to dwell on it. Let's just head somewhere together, okay?"
        n "And as if nothing happened, An Phiast returns to his regular smiley self."
        $ FungieTime=False;


    
    scene dingle bay at bgspace
    with fast_fade
    pause 1.0

    show an phiast talking happy
    with fast_fade
    a "This is the bay!"
    a "I like to ge here every once in a while to fish."
    show an phiast unhappy:
        easein 0.3 yalign 1.1
    a "well, until Fungie shows up, usually. He likes to swim around the boats here, getting gawked at by people."
    show an phiast happy:
        easeout 0.2 yalign 1.0
    a "but that's besides the point. Have you ever fished before?"

    menu:

        "My brother used to fish, I came with him a few times.":
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
        show an phiast talking happy:
            easein 0.1 yalign 0.95
            easeout 0.1 yalign 1.0
        a "You neeed to put your bait on the hook first, and the you cast the line."
        show an phiast happy
        a "These waters are pretty rich with fish, so hopefully we won't have to wait too long before something bites."
        show an phiast talking happy
        a "That's when the best part starts, You gotta reel it in! but careful not to snap the line!"
        a "and then we'll have a nice fish!"
        jump after_choice_bay_1

    label choice_bay_1_yes:
        $ APRelationship+=1;
        show an phiast unhappy:
            easein 0.5 yalign 1.1
        a "Whoa, dude that's{w=0.1}.{w=0.1}.{w=0.1}."
        show an phiast offscreen_right
        show an phiast cg at bgspace
        a "...That's SO hardcore."                                                                                                      
        jump after_choice_bay_1


    label after_choice_bay_1:
        scene bay sea view at bgspace
        with fast_fade
        play music "audio/Sea waves.mp3" fadeout 1.0
        n "You both set up your fishing rods and take in the view of the sea in front of you."
        n "An Phiast seems happy just watching the view, but you can't help but start a conversation."
        n "After all, you still don't know much about him, and this seems like the perfect opportunity."
        n"..."
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

        $ APRelationship+=1;

        show an phiast unhappy:
            xalign 0.5 yalign 1.05
        with fast_fade

        a"Oh?"
        a"..."
        show an phiast somber:
            easein 0.1 yalign 1.0
        a"I usually just think about stuff..."
        a"It's really calming, you know? I get a chance to sort through my thoughts, or think about my other hobbies."
        player "Other hobbies? like what?"
        a"Well, you're probably not gonna be surprised when I say this, but..."
        show an phiast talking happy:
            easein 0.1 yalign 0.95
            easeout 0.1 yalign 1.05
        a"I'm a bit of an artist."
        a"I like to draw, i even tried animating a little, but that's not really my specialty."
        show an phiast happy:
            easein 0.1 yalign 1.0
        a"That would be writing. I even brought a notebook with me!"
        player "Do you usually write while fishing?"
        show an phiast talking happy
        a"Yeah! it's great for that. I just didn't want to start scribbling in my own {nw}{done}little bubble while I'm here with you, {w=0.2} y'know?"
        show an phiast somber:
            easeout 0.1 yalign 1.05
        a"Yeah! it's great for that. I just didn't want to start scribbling in my own {fast}little bubble while I'm here with you, {w=0.2} y'know?"
        n "An phiast stares into your eyes for a second, before turning back to the sea."
        scene bay sea view at bgspace
        with fast_fade
        n "{w=0.1}.{w=0.1}.{w=0.1}.{w=0.3}"
        n "This is nice."


        jump after_choice_bay_2
    
    label choice_bay_2_fungie:

        $ FRelationship+=1;
        $ APRelationship +=1;
        show an phiast happy:
            xalign 0.65 yalign 1.0
        with fast_fade
        a "Oh?"
        show an phiast unhappy:
            easeout 0.1 yalign 1.1
        a "I suppose you want to know more about why we're fighting."
        a "When I first came into town, it was different."
        a "It was same as this year. I came a few days before the Animation Dingle, and we met."
        a "We got on much better back then."
        show an phiast happy
        a "He can be charming when he wants to."
        show an phiast unhappy
        a "...{w=0.5}"
        a "Anyways, when it came to animation Dingle, we went together."
        
        a "I didn't expect my face to be plastered everywhere. It was... {nw}{done}"
        show an phiast happy:
            easein 0.1 yalign 1.0
            easeout 0.1 yalign 1.1
        a "I didn't expect my face to be plastered everywhere. It was... {fast} {w=0.5}nice." 

        show an phiast angry:
            easein 0.1 yalign 1.0
        a "But Fungie didn't think so."
        a "I thought that this was something we both have in common - We're mascots."
        show an phiast unhappy:
            easeout 0.1 yalign 1.1
        a "But I think he saw it as an attack."
        a "I know how much Dingle means to him. He used to also be an outcast, until he came here. {w=0.5} It means a lot to him."
        # show an phiast angry
        # a "But that doesn't mean he can push me around..."
        show an phiast somber:
            easeout 0.1 yalign 1.1
        a "And to think we could have been friends if it wasn't for that."
        "An Phiast pauses."
        "You get the feeling like he never had the chance to tell this to anyone."
        player "I'm sorry that's how things turned out between you two."
        a "It's alright."
        "You both turn back towards the sea."
        scene bay sea view at bgspace
        with fast_fade
        "..."




        jump after_choice_bay_2

    label choice_bay_2_fish:
        show an phiast happy:
            yalign 1.1
        a "Oh?"
        a "Where to even start... {w=0.5}There's all the standard ocean fish, like cods, lings, and pollocks."
        a "What's more interesting is what fish people eat here!"
        a "One of the fish and chips spots makes rays, and even monkfish!"
        show an phiast talking happy:
            easein 0.1 yalign 1.0
        a "Don't know if you've ever seen a monkfish, but they look weird. You definitely wouldn't like its ugly face on your plate!"
        show an phiast happy:
            easein 0.1 yalign 1.1
        a "and still, they manage to make it delicious."
        
        jump after_choice_bay_2


    label choice_bay_2_silent:
        $ APRelationship+=1;
        n "You see no reason to spoil the moment with words."
        n "Hanging out with An Phiast can be hectic. {w=1.0} Not in a bad way, but still. A peaceful break like this is welcome."
        show an phiast somber
        n "He seems to be content. Despite what he said about the excitement of getting a catch, it's cler he likes the wait just as much."
        n "..."

        jump after_choice_bay_2


    label after_choice_bay_2:

        "You feel like you understand An Phiast a little more."
        ".{w=0.3}.{w=0.3}.{w=0.3}You both stay there for a while, hoping to catch some fish. But unfortunately, nothing bites."
        show an phiast unhappy
        with fast_fade
        a "I think I see Fungie in the water..."
        a "I'd rather not talk to him right now. Do you want to go somewhere else before he sees us?"
        "You pull up you town map again."
        player "Let's see..."

        stop music fadeout 1
        $ TimeProgress+=1;
        $ WentToBay=True;
    jump map_screen

