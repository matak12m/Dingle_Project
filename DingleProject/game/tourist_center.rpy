# town center script


label tourist_pressed:
    if(WentToTouristCenter==True):
        n "I think I've seen enough there, let's go somewhere else for a change!"
    else:
        jump tourist_scene
    


label tourist_scene:

    scene dingle town at bgspace

    play music "audio/Seagulls.mp3" fadeout 1.0

    # FUNGIE ONLY DIALOGUE

    n "You make your way to the tourist centre, where you come across a large statue of a very
    familiar dolphin."
    n "The statue is in pristine condition, and is almost lifelike. You reach out to touch it's smooth
    surface..."
    f "Did you need something?"
    n " *You jump back in shock as the statue comes to life* No, I'm sorry! I thought you were a
    statue…"
    f " *He chuckles* They did a good job, didn't they? But don't mistake me for some cold block
    of stone - I'm the real deal."
    n " *You look him up and down* …The resemblance is uncanny. Is that not weird to see
    yourself in stone every day?"
    f "Not at all, in fact - I'm grateful for the honour. It's a big responsibility being the face of this
    town; people come from all over just to catch a glimpse of me!"
    player "Well… people seem to talk about An Phiast more than you… He's a mascot like you,
    right?"
    f "An Phiast? *Pause* I'm not surprised. He has a way of… lurking in people's heads, even
    when he doesn't belong there."


    menu:
        "What do you mean by that? Is he dangerous?":
            jump choice_tourist_Dangerous
        "Are you sure he's as bad as you say?":
            jump choice_tourist_AreYouSure
        "People seem to have strong options on him. Why is that?":
            jump choice_tourist_Why

    

    label choice_tourist_Dangerous:
        $ FRelationship +=1;
        f "Let's just say… I had to work hard to make this town what it is today - a place people love
        to visit. But not everyone shared that vision."
        player "But-"
        f " *Interrupts* Just… keep your distance. Trust me on this - this town needs me more than
        it needs him."
        jump after_choice_tourist_1
    

    label choice_tourist_AreYouSure:
        $ FRelationship -=1;
        player "I've met him. He seemed… kind. Are you sure he's as bad as
        you say?"
        f " *Flicker of anger* Kind? Sure - that's how he wants you to see him. It's all an act, nothing
        more."
        player "No, he's not like that! He genuinely cares for the people in this town, just like you."
        f "Forget it. Believe what you want, but don't say I didn't warn you."
        jump after_choice_tourist_1

    label choice_tourist_Why:
        $ FRelationship+=1;
        $ APRelationship+=1;
        f "*Pause* He's… complicated. People don't know what to make of him. Some see a
        monster, others see him as misunderstood."
        player "And what do you see?"
        f "I see someone who doesn't belong here. Someone who never has. But I don't expect you
        to understand."
        jump after_choice_tourist_1
    
    
    label after_choice_tourist_1:


        player "Wait but-"
        u "Mammy, look! It's Fungie!"
        n "Your conversation is interrupted by a child pointing excitedly at Fungie. His demeanor
        snaps back into his polished, public self upon hearing his name."
        f "Well hello there, little one!"
        n "As Fungie begins to walk away to join the mother and child for pictures, he pauses."
        f "Look… Dingle has a lot to offer and explore but just… keep to what's safe. Some things are
        better left alone."
        n "With that, Fungie walks away."
        stop music fadeout 1.0
        $ TimeProgress+=1;
        $ WentToTouristCenter=True;
    
        jump after_house_choice