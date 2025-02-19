# town center script

transform jump:
    ease 0.1 yoffset -50
    ease 0.1 yoffset 0


label tourist_pressed:
    if(WentToTouristCenter==True):
        n "I think I've seen enough there, let's go somewhere else for a change!"
    else:
        jump tourist_scene;
    


label tourist_scene:

    scene dingle town at bgspace
    "Tourist Center Pressed! There's a statue of Fungie here."

    # FUNGIE ONLY DIALOGUE

    show fungie smug with dissolve:
        matrixcolor BrightnessMatrix(-0.1) * SaturationMatrix(0.0)
        xalign 0.5 yalign -1.0
        
    n "You make your way to the tourist centre, where you come across a large statue of a very
    familiar dolphin."

    n "The statue is in pristine condition, and is almost lifelike.{w=0.1}You reach out to touch its smooth
    surface{cps=*0.05}...{/cps}"

    show fungie annoyed with hpunch:
        ease 0.1 yoffset -100
        matrixcolor IdentityMatrix()
        ease 0.2 yoffset 0

    f "Did you need something?"
    n "*You jump back in shock as the statue comes to life*"
    player "No, I'm sorry!{w=0.1} I thought you were a
    statue..."

    show fungie smug at jump

    f "*He chuckles*\nThey did a good job, didn't they?{w=0.1} But don't mistake me for some cold block
    of stone - I'm the real deal."
    n "*You take a brief moment to look him up and down*"
    player "{cps=*0.2}...{/cps}The resemblance is uncanny. {w=0.3}Is it not weird to see
    yourself in stone every day?"
    f "Not at all, in fact - I'm grateful for the honour. It's a big responsibility being the face of this
    town; people come from all over just to catch a glimpse of me!"
    player "Well{cps=*0.3}...{/cps} people seem to talk about An Phiast{nw}{done} more than you{cps=*0.3}...{/cps} He's a mascot like you,
    right?"
    
    show fungie annoyed at jump

    player "Well{cps=*0.3}...{/cps} people seem to talk about An Phiast{fast} more than you{cps=*0.3}...{/cps} He's a mascot like you,
    right?"
    f "An Phiast{cps=*0.2}...?{/cps}\nI'm not surprised.{w=0.2} He has a way of{cps=*0.25}...{/cps} lurking in people's heads, even
    when he doesn't belong there."


    menu:
        "What do you mean by that? Is he dangerous?":
            jump choice_tourist_Dangerous
        "Are you sure he's as bad as you say?":
            jump choice_tourist_AreYouSure
        "People seem to have strong options on him. Why is that?":
            jump choice_tourist_Why

    

    label choice_tourist_Dangerous:
        $FRelationship +=1;
        f "Let's just say… I had to work hard to make this town what it is today - a place people love
        to visit. But not everyone shared that vision."
        player "But-"
        f "*Interrupts*\nJust{cps=*0.2}...{/cps} keep your distance.{w=0.4}\nTrust me on this - this town needs me more than
        it needs him."
        jump after_choice_tourist_1
    

    label choice_tourist_AreYouSure:
        $ FRelationship -=1;
        player "I've met him. He seemed{cps=*0.3}...{/cps}{w=0.1} kind.{w=0.4} Are you sure he's as bad as
        you say?"

        show fungie angry at jump

        f "{w=0.1}{cps=*1.5}{shader=jitter:u__jitter=0.0, 3.0}Kind?{/shader}{/cps}{w=0.35} Sure -{w=0.2} that's how he wants you to see him.{w=0.2}\nIt's all an act, nothing
        more."
        player "No,{w=0.1} he's not like that! He genuinely cares for the people in this town, just like you."

        show fungie annoyed

        f "Forget it.{w=0.2} Believe what you want, but don't say I didn't warn you."
        jump after_choice_tourist_1

    label choice_tourist_Why:
        $ FRelationship+=1;
        $ APRelationship+=1;

        show fungie neutral

        f "{cps=*0.1}...{/cps}{w=0.2}{nw}"

        f "He's{cps=*0.3}...{/cps} complicated.{w=0.2} People don't know what to make of him.{w=0.2} Some see a
        monster, others see him as misunderstood."
        player "And what do you see?"
        f "I see someone who doesn't belong here.{w=0.2} Someone who never has.{w=0.2} But I don't expect you
        to understand."
        jump after_choice_tourist_1
    
    
    label after_choice_tourist_1:


        player "Wait, but-"

        show fungie dontlaugh at jump

        u "Mammy, look!{w=0.1} It's Fungie!"

        show fungie smug:
            ease 0.5 xzoom -1.0 xalign 0.7

        n "Your conversation is interrupted by a child pointing excitedly at Fungie. His demeanor
        snaps back into his polished, public self upon hearing his name."
        f "Well hello there,{w=0.1} little one!"

        show fungie smug:
            ease 1.5 xalign 0.9

        n "As Fungie begins to walk away to join the mother and child for pictures, he pauses."

        show fungie sad:
            easein 0.4 xzoom 1.0

        f "Look{cps=*0.2}...{/cps} Dingle has a lot to offer and explore but just{cps=*0.2}...{/cps} keep to what's safe.{w=0.2} Some things are
        better left alone."
        n "With that, Fungie walks away."
        $TimeProgress+=1;
        $WentToTouristCenter=True;
    
        jump after_house_choice