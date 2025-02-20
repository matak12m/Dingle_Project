# town center script

define slowFlash = Fade(1.0, 0.3, 0.3, color="#fff")


label church_pressed:
    if(WentToChurch==True):
        n "I think I've seen enough there, let's go somewhere else for a change!"
        jump map_screen
    


label church_scene:
    scene Church 
    show street_monastery at bgspace with Fade(0.0, 0.3, 2.5)

    pause 1.0
    show street_monastery_garden_spiral at bgspace with slowFlash

    play music "audio/BirdsChirpingLong.mp3" fadeout 1

    n "You step into the garden of St. Mary's church, greeted by scents of lavender and
    rosemary."

    show street_monastery_garden at bgspace with fade

    n "As you round a corner, you spot a small statue on a pedestal - it's a statue of Fungie
    leaping over a small boat."

    # Doubled up lines in order to specify where the vpunch occurs
    # {done} will remove the line from the history buffer, so it won't come up when using BACK
    n "You take in the sight before moving on through the garden.{w=0.2} However, your elbow grazes
    the pedestal, and the statue tumbles to the ground with a loud{nw}{done}"
    play sound "audio/falling sound.mp3"
    n "You take in the sight before moving on through the garden. However, your elbow grazes
    the pedestal, and the statue tumbles to the ground with a loud{fast} {size=+4}{shader=jitter:u__jitter=0.0, 3.0}smack{/shader}." with vpunch
    
    a "Uh oh, Fungie won't be happy with that."
    show an phiast happy with moveinright:
        xalign 0.8 yalign 1.0

    n "An Phiast enters, a cheeky grin on his face."

    player "I didn't mean to, I just-"

    show an phiast talking happy
    a "*An Phiast waves off your apology*\n It's alright, happens more than you think."

    show an phiast happy
    a "Though I have to say..{w=0.1} this one is pretty famous around town."

    player "Really? How come?"
    show an phiast unhappy
    a "{w=0.1}.{w=0.1}.{w=0.1}.{w=0.3}This is the day Fungie saved some tourists who strayed too far from the pier.
    Always 'Fungie to the rescue'{w=0.3}.{w=0.23}.{w=0.2}.{w=0.16}"
    show an phiast happy
    a "There's a bunch of these statues around the place, each made to immortalise his {i}'heroic
    moments'{/i}.{w=0.1} There are so many that I'm not surprised you bumped into one."


    menu:
        "So where's your statue?":
            jump choice_church_APStatue
        "Honestly, I think they're kind of great.":
            jump choice_church_ILikeThem
        "There's too many of those here.":
            jump choice_church_SoMany
    

    label choice_church_APStatue:
        $ APRelationship+=1;
        player "I mean, you're a mascot too, right?"
        show an phiast happy
        a "*With a smirk*\nRight? I'd love to have a grand statue near the bay. Give it a grand pose,
        something like this!"
        show an phiast happy:
            easeout 0.2 yalign 1.0 xalign 0.5

        # Strike a pose!!
        show an phiast talking happy:
            easein 0.3 xalign 0.4
            easeout 0.1 xalign 0.5
            linear 0.2 xzoom -1.0
            pause 1.0
            easein 0.1 yalign 1.2
            linear 0.2 xzoom 1.0
            pause 0.1
            easeout 0.3 yalign 1.0
        
            
        n "He stands on his tippy toes and flexes his arms in the air on both sides. You can't help but laugh."
        jump after_choice_church_1
    
    label choice_church_ILikeThem:
        player "It shows how much he's done for the town."
        
        show an phiast unhappy
        n "He rolls his eyes"
        a "Yeah, I get it...{w=0.2} Everyone needs their local hero,{w=0.1}{nw}{done} right?"
        
        # lil shrug
        show an phiast unhappy:
            easein 0.3 yalign 0.9
            easeout 0.35 yalign 1.0
        
        a "Yeah, I get it... Everyone needs their local hero,{fast} right?"
            
        jump after_choice_church_1

    
    label choice_church_SoMany:
        $ APRelationship+=1;
        $ FRelationship-=1;
        player "It's clear he's done a lot for this town...{w=0.3}\nbut that's a lot of
            statues"
        show an phiast talking happy
        n"he chuckles"
        a "It certainly is."
        jump after_choice_church_1


    label after_choice_church_1:
        show an phiast happy:
            linear 0.2 xalign 0.8
        play sound "audio/footsteps.mp3"
        n "The conversation lingers as someone else enters the park."

        n "He looks like a priest?"
        stop sound fadeout 1.0
        show an phiast unhappy:
            linear 0.4 xalign 1.5

        show fungie angry:
            xzoom -1.0
            xalign -0.5 yalign 1.0
            easein 0.6 xalign 0.1

        u "What's this? Another tragic accident?"
        n "The priest picks up{nw}{done}"
        
        show fungie angry:
            easein 0.3 yalign 1.3
            easein 0.3 yalign 1.0


        n "The priest picks up{fast} the statue and observes the large, jagged crack at the base."

        player "I'm sorry I-"

        c "Oh, nonsense. Lord knows there's plenty of these to go around.{w=0.3}\nToo many if you ask me."

        n "He..{w=0.3} winks at you?"

        c "I'll take this to the {i}'shop'{/i} for {i}'repairs'{/i}."

        n "As he walks away,{nw}{done} you watch him casually throw the statue into a clump of bushes,
        swallowing it whole."

        show fungie angry:
            ease 1.5 xalign 1.5

        show an phiast unhappy:
            pause 0.3
            easein 0.8 xalign -0.5 xzoom -1.0
        
        n "As he walks away,{fast} you watch him casually throw the statue{nw}{done} into a clump of bushes,
        swallowing it whole."
        
        n "As he walks away, you watch him casually throw the statue{fast} into a clump of bushes,
        swallowing it whole." with vpunch

        player "who...{w=0.3} was that?"

        show an phiast happy:
            ease 0.4 xalign -0.2

        a  "Don't you know St. Cuan? I guess he's not as well known nowadays..."

        player "Does he not like Fungie?"

        a ".{w=0.4}.{w=0.4}{nw}{done}.{w=0.2}.{w=0.5}{nw}"

        show an phiast unhappy

        a "..{fast}.{w=0.4}.{w=0.7}{nw}"

        a "The town can be very divided on their choice of mascot. He's one of the few who
        really knows what happened back then when we were{w=0.1}.{w=0.2}.{w=0.3}."

        n "He trails off, avoiding your gaze."

        player "{cps=*0.15}...{/cps}{w=0.6}{nw}"
        player "When you were what?"

    if (APRelationship > 1):
        jump church_Trust
    else:
        jump church_NoTrust

    label church_Trust:
        a "We uh...\n{w=0.2}we used to be really close friends a while ago."
        player "What happened?"
        a "Fungie has a way of telling stories, people love them. Once they're out there, well...\n{w=0.2}it's
        hard to convince people to believe otherwise."
        n "You pause, encouraging him to continue."
        a "Eventually, I stopped being the 'misunderstood monster' and just became, well...\n{w=0.25}the
        monster."
        a "But hey, maybe that's all I ever was to begin with."
    
        jump after_church_trust_1

    label church_NoTrust:
        a "I'd rather not get into it...{w=0.3}\nLet's just say things weren't always this way."
        
        jump after_church_trust_1



    label after_church_trust_1:


        player "But-"

        show fungie angry:
            xzoom 1.0
            ease 0.6 xalign 0.9

        c "Come on you two, I'm locking up the church now. Unless you'd rather sleep out in the
        garden?"
        a "I, uh...{w=0.1} guess it's time for me to head out.{w=0.2}\nIt's been nice talking to you."
        n "You watch An Phiast hesitate before he leaves, as if he's going to say more, but he simply
        gives a small nod instead."

        show an phiast unhappy:
            ease 1.2 xalign -1.3

        n "St. Cuan nods at you, encouraging you to head out too. You nod back and make your way
        out of the church."

        scene street_monastery_garden_two at bgspace with fade

        player "An Phiast, wait!"
        
        show an phiast unhappy:
            xalign 2.3 xzoom 1.0 yalign 1.0
            ease 1.2 xalign 1.3

        pause 1.6

        player "...do you wanna go somewhere else, to take your mind off of things?"
        a "{cps=*0.1}...{/cps}{w=0.5}\nsure."
        stop music fadeout 1
        $ TimeProgress+=1;
        $ WentToChurch=True;

        jump map_screen

