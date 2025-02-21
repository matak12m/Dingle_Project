# hotel script

label hotel_pressed_early:
    
    player "This is the hotel where Animation Dingle will take place. It hasn't started yet..."
    player "Let's go somewhere else for now."
    jump map_screen






label hotel_pressed_ontime:
    scene street_hotel_road_sunny at bgspace with fade:
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 xzoom 1.1 yzoom 1.1
        pause 0.5
        easeout 4.0 xzoom 1.4 yzoom 1.4

    pause 2.0

    scene dingle_window_stickers at bgspace with fade

    play music "audio/soft-dreams-lofi-vibes-216576" fadeout 1
    n "The hotel lobby is buzzing with energy.{w=0.2} Posters and tote bags of An Phiast in various animated styles line the walls and tables.{w=0.2} Banners hang from the ceiling, featuring An Phiast's beaming smile."
    show an phiast unhappy
    a "Oh shoot, I forgot, I need to go meet up with the organizers!"
    a "I'll catch up to you later, okay?"
    player "Oh, alright. see you around then!"
    show an phiast happy:
        ease 1.8 xalign 2.0 
    n"And he's gone."
    n "You make your way past a crowd gathered around a life-sized cutout of An Phiast, stopping at a display case showcasing multiple animation awards."

    f "Well, isn't this charming{cps=*0.5}...{/cps}"

    show fungie neutral:
        xalign 1.5 yalign -1.0
        ease 0.8 xalign 0.8

    n "Fungie's voice drips with forced enthusiasm as he stands beside you, his gaze sweeping over a display of awards."

    f "A real tribute to Dingle's finest, isn't it?"
    n "There's something sharp in his tone, but his expression is unreadable. You follow his gaze to the lowest shelf of the awards cabinet to a familiar stone mascot."

    player "What was that award for?"

    n "{i}He shifts uncomfortably.{/i}"
    f "Ah{cps=*0.2}...{/cps}{w=0.2} It was one of the first awards ever given by the festival."

    player "You were part of the festival?"

    f "Oh, I wasn't just {i}'part of it'{/i} - I helped create it.{w=0.3} But alas, you know how it is.{w=0.2} Stories change.{w=0.2} So do people."

    player "What happened?"

    show fungie neutral at jump

    f "{i}*He scoffs before continuing*{/i}\nGood question. Let's just say{cps=*0.4}...{/cps}{w=0.3} things didn't exactly go to script." 

    f "Still,{w=0.1} who can blame them?\n{i}*He gestures towards the crowd*{/i}\n{w=0.2}Everyone loves a hero."

    menu:

        "It doesn't seem fair that you've been left out of all this.":
            jump choice_hotel_1_notfair
        "Maybe they just appreciate what An Phiast has done for them.":
            jump choice_hotel_1_appreciateAP
        "It sounds like the festival meant a lot to both of you.":
            jump choice_hotel_1_meantalot

    label choice_hotel_1_notfair:

        $ FRelationship+=1;

        show fungie smug

        f "Oh, look at you,{w=0.3} standing up for me."

        player "His trademark smirk softens a little, and for a moment, there's almost something genuine in his expression."

        f "Don't waste your energy though, I've made my peace with it.{w=0.25} Mostly."
        jump after_hotel_choice_1

    label choice_hotel_1_appreciateAP:

        show fungie annoyed

        f "Oh of course, the people love a good redemption story.{w=0.2} Inspiring, really."

        f "Who wouldn't want to root for the one everyone used to fear?"
        jump after_hotel_choice_1

    label choice_hotel_1_meantalot:
        $ FRelationship+=1;
        $ APRelationship-=1;

        show fungie smug

        f "It did."

        n "For the first time, there's no sarcasm - just honesty.{w=0.15} But just as quickly as it appears, it's gone, buried beneath a frown."

        show fungie sad

        f "But hey, things change, right?{w=0.15} That's life."
        jump after_hotel_choice_1


    label after_hotel_choice_1:

        show fungie neutral:
            ease 0.4 xzoom -1.0

        n "He turns away from you, and before you can say anything else, a sea of people storms{nw}{done} its way through the lobby, separating you and Fungie."

        show fungie neutral:
            ease 1.8 xalign 2.0 

        n "He turns away from you, and before you can say anything else, a sea of people storms{fast} its way through the lobby, separating you and Fungie."

        n "You try call for him, but he's slinked his way back into the crowd, leaving you alone."

        n "Eager to escape the crowd, you slip away into an open conservatory, taking in the views."

        show an phiast happy:
            ypos 1.0 xpos -0.3 yanchor 1.0 xanchor 0.5 xzoom -1.0
            ease 1.3 xpos 0.2

        a "Escaping the crowd?"

        player "Maybe.{w=0.15} You?"

        a "Sort of. {w=0.45} It's funny. I should be soaking it all in..{w=0.3} I mean - this festival is supposed to be for me, isn't it?"

        player "{w=0.2}{cps=*0.2}...{/cps}Isn't it?"

        a "That's what they say."

        player "{cps=*0.4}...{/cps}Fungie said you used to run it together."

        show an phiast angry

        a "Did he now?{w=0.3} {cps=*0.1}..{/cps}{nw}{done}.. He's not wrong."

        show an phiast unhappy

        a "Did he now? ..{fast}{cps=*0.1}..{/cps}He's not wrong."

        player "What happened?"

        show an phiast talking happy at jump

        a "{i}*Chuckles*{/i}\nThat's always the question, isn't it?"

        show an phiast happy

        a "We all want this town to have something special - something that will bring people together."

        show an phiast unhappy

        player "But..?"

        a "{i}*Sighs*{/i}\nSometimes{cps=*0.2}....{/cps} even if you want the same thing,{w=0.2} you don't see it in the same way."

        a "The past has a way of pulling people apart{cps=*0.4}....{/cps}"

    menu:

        "You've done a lot for this town, don't forget that.":
            jump choice_hotel_2_youvedonealot
        "It doesn't feel right that Fungie's been excluded.":
            jump choice_hotel_2_fungieexcluded
        "It sounds like there's more to this than just a festival...":
            jump choice_hotel_2_moretothis



    label choice_hotel_2_youvedonealot:
        $ APRelationship+=1;

        a "I appreciate that. I just{cps=*0.2}...{/cps} wonder if it was worth the cost."
        jump after_hotel_choice_2

    label choice_hotel_2_fungieexcluded:
        $ FRelationship+=1;
        $ APRelationship-=1;

        show an phiast angry

        a "Well he's not exactly forgotten, is he?"

        n "There's a stern bitterness in his tone."

        show an phiast unhappy
        
        a "People remember what they want to remember."
        jump after_hotel_choice_2

    label choice_hotel_2_moretothis:
        $ APRelationship +=1;
        $ FRelationship +=1;

        show an phiast talking happy
        a "{i}*Chuckles*{/i}\nThere always is something more to things isn't there?"

        show an phiast happy

        jump after_hotel_choice_2



    label after_hotel_choice_2:

        

        a "Anyway, you should head back down. The introductory talk should be starting soon."

        player "What about you?"

        show an phiast unhappy

        a "I'll be down in a minute.{w=0.35}\n{i}*Sigh*{/i}{w=0.2}\nEnjoy it while you can.{w=0.2} Things don't stay the same forever."

        show an phiast unhappy:
            ease 0.6 xzoom 1.0 
            ease 1.2 xpos -0.3

        n "With that, he turns back to admire the view, lost in thought."

        n "You hesitate, sensing there's more to be said, but eventually you step away back into the busy lobby."
        stop music fadeout 1.0



    # if APRelationship >= 1 and FRelationship >= 1:
    #     "both An Phiast and Fungie seem to like you."
    # elif APRelationship >= 1 :
    #     "An Phiast seems to like you."

    # elif FRelationship >= 1 :
    #     "Fungie seems to like you!"

    # if APRelationship > 1 or FRelationship > 1:
    #     "bug report."

    # "This is a test button. back to the map you go!"
    jump epilogue



