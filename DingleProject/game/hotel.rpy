# hotel script

label hotel_pressed_early:
    
    player "This is the hotel where Animation Dingle will take place. It hasn't started yet..."
    player "Let's go somewhere else for now."
    jump map_screen






label hotel_pressed_ontime:
    scene dingle town at bgspace
    player "The hotel lobby is buzzing with energy. Posters and tote bags of An Phiast in various animated styles line the walls and tables. Banners hang from the ceiling, featuring An Phiast's beaming smile."

    player "You make your way past a crowd gathered around a life-sized cutout of An Phiast, stopping at a display case showcasing multiple animation awards."

    f "Well, isn't this charming…"

    player "Fungie's voice drips with forced enthusiasm as he stands beside you, his gaze sweeping over a display of awards."

    f "A real tribute to Dingle's finest, isn't it?"
    player "There's something sharp in his tone, but his expression is unreadable. You follow his gaze to the lowest shelf of the awards cabinet to a familiar stone mascot."

    player "What was that award for? *You motion towards the award*"

    f "Ah… *He shifts uncomfortably* It was one of the first awards ever given by the festival."

    player "You were part of the festival?"

    f "Oh, I wasn't just 'part of it' - I helped create it. But, alas, you know how it is. Stories change. So do people."

    player "What happened?"

    f "*Scoffs* Good question. Let's just say… things didn't exactly go to script." 

    f "Still, who can blame them? *He gestures towards the crowd* Everyone loves a hero."

    menu:

        "It doesn't seem fair that you've been left out of all this.":
            jump choice_hotel_1_notfair
        "Maybe they just appreciate what An Phiast has done for them.":
            jump choice_hotel_1_appreciateAP
        "It sounds like the festival meant a lot to both of you.":
            jump choice_hotel_1_meantalot

    label choice_hotel_1_notfair:

        f "Oh, look at you, standing up for me."

        player "His trademark smirk softens a little, and for a moment, there's almost something genuine in his expression."

        f "Don't waste your energy though, I've made my peace with it. Mostly."
        jump after_hotel_choice_1

    label choice_hotel_1_appreciateAP:

        f "Oh of course, the people love a good redemption story. Inspiring, really."

        f "Who wouldn't want to root for the one everyone used to fear?"
        jump after_hotel_choice_1

    label choice_hotel_1_meantalot:

        f "It did."

        player "For the first time, there's no sarcasm - just honesty. But just as quickly as it appears, it's gone, buried beneath a chuckle."

        f "But hey, things change, right? That's life."
        jump after_hotel_choice_1


    label after_hotel_choice_1:
        player "Before you can say anything else, a sea of people storms its way through the lobby, separating you and Fungie."

        player "You try call for him, but he's slinked his way back into the crowd, leaving you alone."

        player "Eager to escape the crowd, you slip away into an open conservatory, taking in the views."

        a "Escaping the crowd?"

        player "Maybe. You?"

        a "Sort of. {w=1.0} It's funny. I should be soaking it all in.. I mean - this festival is supposed to be for me, isn't it?"

        player "{w=1.0} …Isn't it?"

        a "That's what they say."

        player "*Hesitantly* Fungie said you used to run it together."

        a "Did he now? {w=1.0} He's not wrong."

        player "What happened?"

        a "*Chuckles* That's always the question, isn't it?"

        a "We all want this town to have something special - something that will bring people together."

        player "But?..."

        a "*Sighs* Sometimes… even if you want the same thing, you don't see it in the same way."

        a "The past has a way of pulling people apart."

    menu:

        "You've done a lot for this town, don't forget that.":
            jump choice_hotel_2_youvedonealot
        "It doesn't feel right that Fungie's been excluded.":
            jump choice_hotel_2_fungieexcluded
        "It sounds like there's more to this than just a festival...":
            jump choice_hotel_2_moretothis



    label choice_hotel_2_youvedonealot:

        a "I appreciate that. I just wonder if it was worth the cost."
        jump after_hotel_choice_2

    label choice_hotel_2_fungieexcluded:

        a "Well he's not exactly forgotten, is he?"

        player "There's a stern bitterness in his tone."
        a "People remember what they want to remember."
        jump after_hotel_choice_2

    label choice_hotel_2_moretothis:

        a "There always is something more to things isn't there? *Chuckles*"
        jump after_hotel_choice_2



    label after_hotel_choice_2:
        a "Anyway… you should head back down. The introductory talk should be starting soon."

        player "What about you?"

        a "I'll be down in a minute. *Sighs* Enjoy it while you can. Things don't stay the same forever."

        player "With that, he turns back to admire the view, lost in thought."

        player "You hesitate, sensing there's more to be said, but eventually you step away back into the busy lobby."




    if APRelationship >= 1 and FRelationship >= 1:
        "both An Phiast and Fungie seem to like you."
    elif APRelationship >= 1 :
        "An Phiast seems to like you."

    elif FRelationship >= 1 :
        "Fungie seems to like you!"

    if APRelationship > 1 or FRelationship > 1:
        "bug report."

    "This is a test button. back to the map you go!"
    jump map_screen



