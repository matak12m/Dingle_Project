# town center script


label town_pressed:
    scene dingle town at bgspace
    "Welcome to the town! I hope you like colourful houses!"

    player "The town centre of Dingle feels like a living gallery. Colourful murals decorate walls and
    shop fronts, transforming dull facades into a burst of colourful creativity."
    player "You stop beside An Phiast, who's admiring a colourful wall full of murals of Dingle - murals
    of the harbour, horses, and even men playing music in a pub."
    a "They really went all out with this one"
    player "He motions towards the mural of the men playing music in a pub."
    player "Do you enjoy this kind of stuff? Art and all that?"
    a "Oh absolutely! The details, the humour - it's like each mural has its own story to tell, and
    they're all... unique."
    a "It's comforting."
    f "Well, well, what's this? An Phiast pretending to enjoy culture?"
    player "Fungie strides in, surrounded by townsfolk who clearly idolise him. They laugh along with
    him."
    a "*Mumbles* Here we go…"
    f "I'll be honest, I didn't think you had it in you. *Pause* Now that's art, wouldn't you
    agree?"
    player "Fungie gestures to a mural of the harbour, where Fungie himself takes centre stage,
    gleaming in the sunlight. The group of townsfolk nod in agreement."
    f "So, what are you doing? *He turns to you* If you wanted a real tour, you could've just asked
    me. I mean, I would have loved to show you around, but I get it… you were probably… busy."
    player "One of the townsfolk pipes up, seizing their moment"
    u "Pretty sure his version of a tour is lurking around and hiding in the bushes!"
    player "The group burst into laughter, while An Phiast shifts uncomfortably beside you."
    # ***************************************************************************
    # *******
    # Option 1. player "That's not fair."
    # player "Your voice cuts through the laughter. Both An Phiast and Fungie are surprised."
    # f "Oh? I didn't realise you two were so… close."
    # player "There's a hint of sadness in Fungie's voice, which he quickly masks with a layer of forced
    # cheer."
    # f "Aren't I lucky to witness this budding friendship firsthand? Go ahead, don't let me
    # interrupt your… moment."
    # player "Fungie's attempt to sound playful falls flat, leaving tension in the air."
    # f "Well, I… I'll leave you be, enjoy your little adventure."
    # player "Fungie and his entourage leave the town center, leaving you and An Phiast in silence."
    # a "Thank you, really. It means a lot."
    # player "You can't let him treat you like that. You're just as important to Dingle as he is."
    # a "*He smiles weakly* I'm used to it. *Pause* Have you seen this mural yet?"
    # a "It's about this old man who went fishing on his boat every morning. I used to…"
    # player "You stay with An Phiast in the town centre for hours, listening to the story of each mural
    # with excitement."




    # Option 2. player "…"
    # player "You hesitate, unsure of whether to speak."
    # f "I mean it… If you ever want a tour, I'd be more than happy to give you one."
    # player "You glance between Fungie and An Phiast."
    # player "Finally, you nod."
    # player "Yeah… I'd like that."
    # f "*His face lights up* Great!"
    # f "Well… I'll leave you be, enjoy your little adventure."
    # player "Fungie and his entourage leave the town centre, leaving you and An Phiast in silence."
    # a "*sad* I, uh… I should also get going."
    # player "Wait, An Phiast-"
    # player "You call after him, but he has already walked away, slipping into the shadows."
    # player "You stay at the town centre, admiring the remaining murals in silence."




    # THIS SCENE COULD ANGER AN PHIAST AND LEAD INTO A SCENE WITH FUNGIE ONLY
    
    jump after_house_choice



