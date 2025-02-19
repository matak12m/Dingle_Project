# town center script


label town_pressed:
    if(WentToTown==True):
        n "I think I've seen enough there, let's go somewhere else for a change!"
    else:
        jump town_scene
    


label town_scene:
    scene dingle town at bgspace
    

    n "The town centre of Dingle feels like a living gallery. Colourful murals decorate walls and
    shop fronts, transforming dull facades into a burst of colourful creativity."
    n "You stop beside An Phiast, who's admiring a colourful wall full of murals of Dingle - murals
    of the harbour, horses, and even men playing music in a pub."
    a "They really went all out with this one"
    n "He motions towards the mural of the men playing music in a pub."
    player "Do you enjoy this kind of stuff? Art and all that?"
    a "Oh absolutely! The details, the humour - it's like each mural has its own story to tell, and
    they're all... unique."
    a "It's comforting."
    f "Well, well, what's this? An Phiast pretending to enjoy culture?"
    n "Fungie strides in, surrounded by townsfolk who clearly idolise him. They laugh along with
    him."
    a "*Mumbles* Here we go…"
    f "I'll be honest, I didn't think you had it in you. *Pause* Now that's art, wouldn't you
    agree?"
    n "Fungie gestures to a mural of the harbour, where Fungie himself takes centre stage,
    gleaming in the sunlight. The group of townsfolk nod in agreement."
    f "So, what are you doing? *He turns to you* If you wanted a real tour, you could've just asked
    me. I mean, I would have loved to show you around, but I get it… you were probably… busy."
    n "One of the townsfolk pipes up, seizing their moment"
    u "Pretty sure his version of a tour is lurking around and hiding in the bushes!"
    n "The group burst into laughter, while An Phiast shifts uncomfortably beside you."
    f "But the offer still stands. "
    

    menu:
        "That's not fair.":
            jump choice_town_NotFair
        "I would like a tour from you.":
            jump choice_town_Tour
        "(stay silent)":
            jump choice_town_Silence

    label choice_town_NotFair:

        $ APRelationship +=1;
    
        n "Your voice cuts through the laughter. Both An Phiast and Fungie are surprised."
        f "Oh? I didn't realise you two were so… close."
        n "There's a hint of sadness in Fungie's voice, which he quickly masks with a layer of forced
        cheer."
        f "Aren't I lucky to witness this budding friendship firsthand? Go ahead, don't let me
        interrupt your… moment."
        n "Fungie's attempt to sound playful falls flat, leaving tension in the air."
        f "Well, I… I'll leave you be, enjoy your little adventure."
        n "Fungie and his entourage leave the town center, leaving you and An Phiast in silence."
        a "Thank you, really. It means a lot."
        player "You can't let him treat you like that. You're just as important to Dingle as he is."
        a "*He smiles weakly* I'm used to it. *Pause* Have you seen this mural yet?"
        a "It's about this old man who went fishing on his boat every morning. I used to…"
        n "You stay with An Phiast in the town centre for hours, listening to the story of each mural
        with excitement."
        jump after_choice_town_1


    label choice_town_Tour:
        $ FRelationship +=1;
        $ APRelationship -=1;
        n "You hesitate before speaking."
        f "I mean it… If you ever want a tour, I'd be more than happy to give you one."
        n "You glance between Fungie and An Phiast."
        n "Finally, you nod."
        player "Yeah… I'd like that."
        f "*His face lights up* Great!"
        f "Well… I'll leave you be, enjoy your little adventure."
        n "Fungie and his entourage leave the town centre, leaving you and An Phiast in silence."
        a "*sad* I, uh… I should also get going."
        player "Wait, An Phiast-"
        n "You call after him, but he has already walked away, slipping into the shadows."
        n "You stay at the town centre, admiring the remaining murals in silence."
        jump after_choice_town_1
        # THIS SCENE COULD ANGER AN PHIAST AND LEAD INTO A SCENE WITH FUNGIE ONLY

    label choice_town_Silence:
        $ APRelationship -=1;
        n "you're not going to humor him. It's better to just ignore them."
        f "Dolphin got your tongue? Can't say I blame you."
        f "in any case, if you change your mind, do let me know."
        f "it would certainly be better than what he could ever offer you."
        n "Fungie and his entourage leave the town center, leaving you and An Phiast in silence."
        a "Finally, they're gone..."
        player "Sorry about him. What he said was so mean."
        a "*He smiles weakly* I'm used to it. *Pause* Have you seen this mural yet?"
        a "It's about this old man who went fishing on his boat every morning."
        n "You take in the remaining murals in silence. An Phiast still seems a bit down."
        jump after_choice_town_1
       
    
    label after_choice_town_1:
        stop music fadeout 1.0
        $  TimeProgress+=1;
        $ WentToTown=True;


        jump after_house_choice



