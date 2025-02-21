# town center script

transform galleryItem(size, posX, posY, delay, offset, deadTime):
    subpixel True
    align(posX,posY) zoom(size) xoffset 0.0
    blur 16.0
    alpha 0.0
    pause delay
    
    block:
        subpixel True
        align(posX,posY) zoom(size) xoffset 0.0
        blur 16.0
        alpha 0.0

        # Dissolve in, slide img
        parallel:
            ease 5.0 alpha 1.0 
        parallel:
            ease 5.0 blur 0.0
        parallel:
            ease 15.0 xoffset absolute(offset) 

        pass

        # Dissolve out
        parallel:
            ease 3.0 alpha 0.0
        parallel:
            ease 3.0 blur 16.0

        pause deadTime

        repeat

label town_pressed:
    if(WentToTown==True):
        n "I think I've seen enough there, let's go somewhere else for a change!"
        jump map_screen
    

label town_scene:
    scene dingle town at bgspace with fade:
        blur 0.0
        pause 1.0
        ease 2.0 blur 16.0

    pause 1.5
    
    show street_art_boatmen at galleryItem(0.3, 0.2, 0.6, 0.0, -50.0, 36.0) 
    show street_art_rage at galleryItem(0.6, 0.8, 0.6, 1.4, 50.0, 36.0) 
    show maxresdefault at galleryItem(0.4, 0.5, 0.1, 2.2, 0.0, 36.0)
    
    show street_art_spiral_wave at galleryItem(0.2, 0.15, 0.5, 18.0, -50.0, 36.0) 
    show mural-rowers at galleryItem(0.6, 0.9, 0.5, 19.4, 50.0, 36.0) 
    show cat_streetart at galleryItem(0.2, 0.5, 0.1, 20.2, 0.0, 36.0)

    show street_art_archer at galleryItem(0.3, 0.5, 0.5, 38.2, 0.0, 36.0)

    n "The town centre of Dingle feels like a living gallery. Colourful murals decorate walls and
    shop fronts, transforming dull facades into a burst of colourful creativity."
    n "You stop beside An Phiast, who's admiring a colourful wall full of murals of Dingle - murals
    of the harbour, horses, and even men playing music in a pub."

    show an phiast happy:
        anchor(0.5,1.0) ypos 1.0 xpos 1.5
        ease 2.0 xpos 0.8 

    a "They really went all out with this one!"
    n "He motions towards the mural of the men playing music in a pub."
    player "Do you enjoy this kind of stuff?{w=0.2} Art and all that?"

    show an phiast talking happy at jump

    a "Oh absolutely!{w=0.2} The details, the humour -{w=0.1} it's like each mural has its own story to tell, and
    they're all{cps=*0.2}...{/cps} unique."
    a "It's comforting."
    f "Well, well,{w=0.2} what's this?{w=0.3} An Phiast pretending to enjoy culture?"

    show an phiast unhappy:
        parallel:
            ease 0.4 xzoom -1.0
        parallel:
            ease 1.5 xpos 0.2

    show fungie smug:
        xanchor 0.5
        ypos 0.2 xpos 2.0
        ease 1.5 xpos 0.8

    n "Fungie strides in, surrounded by townsfolk who clearly idolise him. They laugh along with
    him."
    a "{i}*Mumbles*{/i}\nHere we go{cps=*0.2}...{/cps}"
    f "I'll be honest, I didn't think you had it in you.{w=0.2} Now that's art, wouldn't you
    agree?"

    show fungie smug:
        ease 0.4 xzoom -1.0

    n "Fungie gestures to a mural of the harbour, where Fungie himself takes centre stage,
    gleaming in the sunlight.{w=0.2} The group of townsfolk nod in agreement."

    show fungie smug:
        ease 0.4 xzoom 1.0

    f "So, what are you doing?\n{i}*He turns to you*{/i}\nIf you wanted a real tour, you could've just asked
    me."
    f "I mean, I would have loved to show you around, but I get it{cps=*0.5}...{/cps} you were probably{cps=*0.2}...{/cps}{w=0.2} busy."
    n "One of the townsfolk pipes up, seizing their moment"
    u "Pretty sure his version of a tour is lurking around and hiding in the bushes!"
    n "The group burst into laughter, while An Phiast shifts uncomfortably beside you."
    f "But the offer still stands."
    

    menu:
        "That's not fair.":
            jump choice_town_NotFair
        "I would like a tour from you.":
            jump choice_town_Tour
        "(stay silent)":
            jump choice_town_Silence

    label choice_town_NotFair:

        $ APRelationship +=1;
    
        n "Your voice cuts through the laughter.{w=0.15} Both An Phiast and Fungie are surprised."
        show fungie sad at jump
        f "Oh? I didn't realise you two were so{cps=*0.2}...{/cps} close."


        n "There's a hint of sadness in Fungie's voice, which he quickly masks with a layer of forced
        cheer."

        show fungie smug

        f "Aren't I lucky to witness this budding friendship firsthand? Go ahead, don't let me
        interrupt your{cps=*0.2}...{/cps} moment."

        show fungie sad

        n "Fungie's attempt to sound playful falls flat, leaving tension in the air."
        f "Well, I{cps=*0.2}...{/cps}{w=0.15} I'll leave you be, enjoy your little adventure."

        show fungie sad:
            parallel:
                ease 0.4 xzoom -1.0
            parallel:
                ease 1.5 xpos 2.0

        n "Fungie and his entourage leave the town center, leaving you and An Phiast in silence."
        a "Thank you, really.{w=1.5} It means a lot."
        player "You can't let him treat you like that.{w=1.5} You're just as important to Dingle as he is."
        show an phiast happy
        a "{i}*He gives a weak smile*{/i}\nI'm used to it.{w=0.2} Have you seen this mural yet?"
        a "It's about this old man who went fishing on his boat every morning. I used to{cps=*0.2}...{/cps}"

        show an phiast happy:
            ease 1.5 alpha 0.0
    
        n "You stay with An Phiast in the town centre for hours, listening to the story of each mural
        with excitement."
        jump after_choice_town_1


    label choice_town_Tour:
        $ FRelationship +=1;
        $ APRelationship -=1;
        n "You hesitate before speaking."
        f "I mean it{cps=*0.2}...{/cps} If you ever want a tour, I'd be more than happy to give you one."
        n "You glance between Fungie and An Phiast."
        n "Finally, you nod."

        show an phiast unhappy at jump

        player "Yeah{cps=*0.2}...{/cps} I'd like that."
        f "{i}*His face lights up*{/i}\nGreat!"
        f "Well{cps=*0.2}...{/cps} I'll leave you be, enjoy your little adventure."
        
        show fungie smug:
            parallel:
                ease 0.4 xzoom -1.0
            parallel:
                ease 1.5 xpos 2.0

        n "Fungie and his entourage leave the town centre, leaving you and An Phiast in silence."
        a "I, uh{cps=*0.2}...{/cps} I should also get going."
        player "Wait, An Phiast-"

        show an phiast unhappy:
            parallel:
                ease 0.4 xzoom 1.0
            parallel:
                ease 1.5 xpos -0.5


        n "You call after him, but he has already walked away, slipping into the shadows."
        n "You stay at the town centre, admiring the remaining murals in silence."
        jump after_choice_town_1
        # THIS SCENE COULD ANGER AN PHIAST AND LEAD INTO A SCENE WITH FUNGIE ONLY

    label choice_town_Silence:
        $ APRelationship -=1;
        n "You're not going to humor him.{w=0.15} It's better to just ignore them."
        f "Dolphin got your tongue?{w=0.2} Can't say I blame you."
        f "In any case, if you change your mind, do let me know."
        f "It would certainly be better than what he could ever offer you."
        
        show fungie smug:
            parallel:
                ease 0.4 xzoom -1.0
            parallel:
                ease 1.5 xpos 2.0

        n "Fungie and his entourage leave the town center, leaving you and An Phiast in silence."
        a "Finally, they're gone{cps=*0.2}...{/cps}"
        player "Sorry about him.{w=0.15} What he said was so mean."
        show an phiast happy
        a "*He gives a weak smile*\nI'm used to it.{w=0.2} Have you seen this mural yet?"
        a "It's about this old man who went fishing on his boat every morning."
        show an phiast unhappy
        n "You take in the remaining murals in silence. An Phiast still seems a bit down."
        jump after_choice_town_1
       
    
    label after_choice_town_1:
        stop music fadeout 1.0
        $  TimeProgress+=1;
        $ WentToTown=True;


        jump after_house_choice



