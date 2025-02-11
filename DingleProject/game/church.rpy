# town center script


label church_pressed:
    scene dingle town at bgspace
    

    n "You step into the garden of St. Mary's church, greeted by scents of lavender and
    rosemary."

    n "As you round a corner, you spot a small statue on a pedestal - it's a statue of Fungie
    leaping over a small boat."

    n "You take in the sight before moving on through the garden. However, your elbow grazes
    the pedestal, and the statue tumbles to the ground with a loud smack."

    a "Uh oh, Fungie won't be happy with that."
    show an phiast happy
    n "An Phiast enters, a cheeky grin on his face."

    player "I didn't mean to, I just-"
    a "*An Phiast waves off your apology* It's alright, happens more than you think."

    a "Though I have to say.. this one is pretty famous around town."

    player "Really? How come?"
    show an phiast unhappy
    a " *Pause* This is the day Fungie saved some tourists who strayed too far from the pier.
    Always 'Fungie to the rescue'…"
    show an phiast happy
    a "There's a bunch of these statues around the place, each made to immortalise his 'heroic
    moments'. There are so many that I'm not surprised you bumped into one."


    menu:
        "So where's your statue?":
            jump choice_church_APStatue
        "Honestly, I think they're kind of great.":
            jump choice_church_ILikeThem
        "There's too many of those here.":
            jump choice_church_SoMany
    

    label choice_church_APStatue:

        player "I mean, you're a mascot too, right?"
        show an phiast very happy
        a "*With a smirk* Right? I'd love to have a grand statue near the bay. Give it a grand pose,
        something like this!"
        show an phiast happy
        n "He stands on his tippy toes and flexes his arms in the air on both sides. You can't help but
        laugh."
        jump after_choice_church_1
    
    label choice_church_ILikeThem:
        player "it shows how much he's done for the town."
        show an phiast unhappy
        a "*Rolls his eyes* Yeah, I get it… Everyone needs their local hero, right?"
        jump after_choice_church_1

    
    label choice_church_SoMany:
        show an phiast very happy
        player "It's clear he's done a lot for this town… but that's a lot of
            statues"
        a "*With a low chuckle* It certainly is."
        jump after_choice_church_1


    label after_choice_church_1:

        n "The conversation lingers as someone else enters the park."

        n "He looks like a priest?"

        u "What's this? Another tragic accident?"
        n "The priest picks up the statue and observes the large, jagged crack at the base."

        player "I'm sorry I-"

        c "Oh, nonsense. Lord knows there's plenty of these to go around. Too many if you ask me."


        n "He winks at you?"

        c "I'll take this to the 'shop' for 'repairs'."

        n "As he walks away, you watch him casually throw the statue into a clump of bushes,
        swallowing it whole."

        player "who... was that?"

        a  "Don't you know St. Cuan? I guess he's not as well known nowadays..."

        player "Does he not like Fungie?"

        a "... {w=1.0} The town can be very divided on their choice of mascot. He's one of the few who
        really knows what happened back then when we were…"

        n "He trails off, avoiding your gaze."

        player "...When you were what?"

    if (APRelationship > 1):
        jump church_Trust
    else:
        jump church_NoTrust

    label church_Trust:
        a "We uh… we used to be really close friends a while ago."
        player "What happened?"
        a "Fungie has a way of telling stories, people love them. Once they're out there, well… it's
        hard to convince people to believe otherwise."
        n "You pause, encouraging him to continue"
        a "Eventually, I stopped being the 'misunderstood monster' and just became, well… the
        monster."
        a "But hey, maybe that's all I ever was to begin with."
    
        jump after_church_trust_1

    label church_NoTrust:
        a "I'd rather not get into it… Let's just say things weren't always this way."
        
        jump after_church_trust_1



    label after_church_trust_1:


        player "But-"
        c "Come on you two, I'm locking up the church now. Unless you'd rather sleep out in the
        garden?"
        a "I, uh… guess it's time for me to head out. It's been nice talking to you."
        n "You watch An Phiast hesitate before he leaves, as if he's going to say more, but he simply
        gives a small nod instead."
        n "St. Cuan nods at you, encouraging you to head out too. You nod back and make your way
        out of the church."
        player "An Phiast, wait!"
        show an phiast unhappy
        n "...do you wanna go somewhere else, to take you mind off of things?"
        a "...sure."


        jump after_house_choice

