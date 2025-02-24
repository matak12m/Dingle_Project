# ending script


#max AP points you can gain: 8
#max F points you can gain: 5
#currently you start with 1 in each.


label epilogue:
    scene hotel_event_presentation at bgspace
    with fast_fade

    n "The day flies by, filled with exciting talks, breathtaking short films, and addictive games."
    show hotel_event_speech at bgspace
    with fast_fade
    n "There's so many people..."
    show dingle_window_stickers at bgspace
    with fast_fade
    n "And the whole event is plastered with the visage or An Phiast, with stickers of him everywhere."

    n "It's an amazing experience, all in his honour."  
    show hotel_outside at bgspace
    with fast_fade
    n "As you reluctantly leave the electric buzz of the busy hotel, you see An Phiast and Fungie on opposite sides of the hotel yard, each surrounded by their own crowd of fans."

    n "Cameras flash as they pose for photos, their smiles polished, their presence commanding. Two legendary mascots of Dingle, both larger than life, yet separated by something unspoken."

    n "Your bus leaves soon. Who do you want to say goodbye to?"




    menu:
        "An Phiast":
            jump choice_epilogue_anphiast
        "Fungie":
            jump choice_epilogue_fungie
        "Make both of them talk together":
            jump choice_epilogue_both
        "Go on the bus":
            jump choice_epilogue_bus







label choice_epilogue_anphiast:
    play music "audio/EmotionalPianoMusic" fadeout 1.0

    if (APRelationship > 4):

        n "You make your way towards An Phiast, making your way through the group of fans now heading back to the hotel."
        show an phiast happy with fast_fade:
            xalign 0.5 yalign 1.1
        a "You stuck around?"

        player "Of course! I had a really good time."
        show an phiast talking happy:
            easein 0.1 yalign 1.0
            easein 0.1 yalign 1.1 
        a "Good!"

        n "An Phiast beams with happiness, knowing you enjoyed his festival."
        show an phiast happy:
            easein 0.1 yalign 1.0
        a "That's what it's all about, isn't it? Something to bring people together. I hope it was worth your long trip."

        player "It was."

        n "You nod, thinking of all the great memories you've made here in Dingle. Memories within the festival, with the townspeople…"

        n "…and with An Phiast."

        n "There's an understanding silence between you as you admire the bustling hotel from afar, people from all over the world admiring An Phiast's legacy."
        show an phiast somber:
            easein 0.1 yalign 1.1
        a "Before you go… *Pause* I just want to say thank you - for sticking by me. It means a lot to me, and I'll never forget it."
        

        n "His voice is steady, assured, with a new confidence to him."
        show an phiast happy
        n "You smile, remembering the shy little green mascot he used to be."

        n "Looking at him now, he's a completely changed person. He stands taller, no longer afraid to stand out."

        n "He smiles excitedly as more fans emerge from the hotel, calling his name."
        show an phiast somber
        a "I should go… {nw} {done} Have a safe journey home."
        show an phiast happy
        a "I should go… {fast}Have a safe journey home."

        show an phiast happy:
            linear 1.0 xalign 1.0

        n "He smiles softly as he begins to walk away. Before he's out of earshot, he stops and turns around."
        show an phiast happy:
            linear 0.2 xzoom -1.0
        a "You'll come back next year, won't you?"

        n "You laugh" 

        player "Of course!"
        
        n "With that, you part ways.{nw}{done} He returns to his adoring fans as you make your way back into Dingle to catch the bus."
        show an phiast happy:
            linear 0.3 xzoom 1.0
            linear 1.5 xalign 3.0
        n "With that, you part ways.{fast} He returns to his adoring fans as you make your way back into Dingle to catch the bus."

        n "You meant every word you said, and you can't wait to come back."

        show sunset an phiast at bgspace
        with slow_fade

        n "Dingle is going to be great next year..."
        pause 3.0
        scene black_screen
        with slow_fade
        return
    else:

        n "You make your way towards An Phiast, making your way through the group of fans excitedly asking for photos."
        show an phiast happy with fast_fade:
            xalign 0.5 yalign 1.1
        n "You fail to catch his eye as he poses for silly selfies. As a last resort, you give him a light tap on the arm."
        show an phiast talking happy:
            easein 0.1 yalign 1.0
        a "Oh, Can I help you?"

        n "His smile to you is forced, for the sake of the public eye."

        player "Oh sorry, I uh… I just wanted to say goodbye."
        show an phiast happy:
            easein 0.1 yalign 1.1
        a "You're leaving?"

        n "He continues to pose for pictures with fans, speaking in between each photo."

        player "Yeah…"

        a "Well, I hope you enjoyed Animation Dingle. We hope to see you again next year!"

        n "His response is recited, almost robotic. He avoids your eyes as he speaks."

        player "Thanks…"
        hide an phiast happy with dissolve
        n "He turns away for more photos with fans, leaving his back turned to you."

        n "With nothing left to do, you take one last look at the beach."

        show sunset at bgspace
        with slow_fade

        n "While you had a fantastic time, you wish you had gotten to know An Phiast a little better."

        n "There's always next year..."
        
        n "...right?"
        pause 3.0
        scene black_screen
        with slow_fade
        return
label choice_epilogue_fungie:
    play music "audio/EmotionalPianoMusic" fadeout 1.0
    if (FRelationship > 3):

        n "You make your way towards Fungie, making your way through the group of fans who have just bombarded him with selfies."

        show fungie smug:
            xalign 0.5 yalign -1.0
            
        f "Well, well. Look who it is!"

        n "He looks at you fondly as you roll your eyes with a smirk."

        f "Did you enjoy your time at Dingle?"

        player "I had a great time."

        f "You're very welcome for that."

        n "He teases, but you can't help but laugh."

        f "Really, though, I'm glad. And uh..."
        show fungie neutral:
            easein 0.1 yalign -1.1
        f "Thank you."

        player "For what?"

        f "For seeing past all the noise."

        player "What do you mean?"

        f "Oh, you know… {i} This? {/i} All that arrogant, golden boy act..."
        show fungie sad:
            easein 0.1 yalign -1.0
        f "It's nice to be reminded that there's… well, that there's more to me than that."

        player "There always was."

        show fungie smug
        n "He smiles softly with a chuckle"

        f "Don't go making me soft now."    
        show fungie smug:
            easein 0.1 yalign -1.1

        f "Get home safe, won't you?"

        n "You smile"

        player " I will."
            
        n "With that, he reluctantly walks away, re-joining his group of fans by the hotel entrance, eager to take photos."

        n "You make your way back to your bus, with only one thought on your mind:"

        show sunset fungie at bgspace
        with slow_fade

        n "Dingle is going to be great next year..."
        pause 3.0
        scene black_screen
        with slow_fade
        return
    else:

        n "You make your way towards Fungie, making your way through the group of photographers and eager fans taking photos."

        player "Fungie?"

        n "You call out to him amidst the bright flashes of cameras, people asking him to pose, and people with microphones asking questions."

        n "You call out once again, waving your arms to catch his attention."
        show fungie annoyed:
            xalign 0.5 yalign -1.0
        n "His eyes meet yours, and a wave of annoyance washes over his face."
        show fungie angry with vpunch:
            easein 0.1 yalign -1.1
        f "Can't you see I'm busy?"
        show fungie smug:
            easein 0.1 -1.0
        n "He speaks through a small gap in his mouth, before snapping back to his smile for the cameras."

        player "I just want to say goodbye..."
        show fungie annoyed
        n "His sharp eyes meet yours yet again. He rolls his eyes before {nw}{done} resuming his poses and answering questions for fans."
        show fungie smug
        n "His sharp eyes meet yours yet again. He rolls his eyes before {fast} resuming his poses and answering questions for fans."
        hide an phiast happy with dissolve
        n "Defeated, you leave him alone and make your way to the bus station."

        n "You're positive that there's more to Fungie than his arrogant façade.  Maybe if you had gotten to know him better, things would be different…"

        n "At least there's always next year."

        show sunset at bgspace
        with slow_fade
        
        n "...right?"
        pause 3.0
        scene black_screen
        with slow_fade
        return

label choice_epilogue_both:
    play music "audio/EmotionalPianoMusic" fadeout 1.0
    if ((APRelationship + FRelationship) > 8):

        n "You manage to catch the eyes of both Fungie and An Phiast, who tower over the crowd below them."

        n "You wave them over. As they approach you, their excited smiles quickly fade as they realise the other is also heading for you."

        show fungie annoyed with dissolve:
            xalign 0.7 yalign -1.1 

        show an phiast unhappy with dissolve:
            xalign -0.2 yalign 1.0 xzoom -1.0

        f "Did you need something?"

        n "Fungie turns his nose at An Phiast, who is sheepishly looking away."

        player "I wanted to speak to you both. Together."
        show fungie annoyed:
            easein 0.1 yalign -1.1 

        show an phiast unhappy:
            easein 0.1 yalign 1.0

        n "You watch as they shift uncomfortably, looking for a way out."

        player "Aren't you both tired of this?"
        show fungie angry:
            easein 0.1 yalign -1.0
        f "Of what?"

        n "This whole… rivalry thing. You both clearly care about this town, but you act like there's not enough space for the both of you."
        
        show fungie dontlaugh with vpunch:
            easein 0.1 yalign -1.1

        n "An Phiast and Fungie stand in stunned silence, mouths agape like a fish out of water."

        player "{w=0.5}Well?"
        show fungie sad
        n "You stand your ground, arms crossed as you wait for a response."

        n "Fungie, now oddly sheepish, rubs the back of his neck before speaking to An Phiast."
        show fungie sad:
            easein 0.1 yalign -1.2
        f "{i}I mean… I guess… I don't know… this whole festival… it's all about you, you know?{/i}"

        n "He mumbles, barely a whisper."
        show an piast unhappy:
            easein 0.1 yalign 1.0
            easein 0.1 yalign 1.1 
        a "What?"
        show fungie annoyed
        f "You heard me. {nw} {done} I guess I was just… jealous? {cps=*0.5}{i}Sigh{/i}{/cps} I hated seeing your name on everything. A whole festival about you? While I get a statue here, a mention there?"
        show fungie sad
        f "You heard me. {fast} I guess I was just… jealous? {cps=*0.5}{i}Sigh{/i}{/cps} I hated seeing your name on everything. A whole festival about you? While I get a statue here, a mention there?"

        n "Fungie looks away, refusing to meet An Phiast's eyes."

        a "Jealous of me? {nw} {done} I was jealous of you!"
        show an phiast angry:
            easein 0.1 yalign 1.0
            easein 0.1 yalign 1.1             
        a "Jealous of me? {nw} {done} I was jealous of you!"

        n "An Phiast exclaims in utter shock."
        show an phiast somber
        a "You don't need a festival to be remembered. This town adores you every single day! {nw} {done}No matter what I do, how many events are held with my name on it… It's your name they always come back to."
        show an phiast unhappy:
            easein 0.1 yalign 1.0
        a "You don't need a festival to be remembered. This town adores you every single day! {fast}No matter what I do, how many events are held with my name on it…{nw}{done} It's your name they always come back to."
        show an phiast somber:
            easein 0.1 yalign 1.1
        a "You don't need a festival to be remembered. This town adores you every single day! No matter what I do, how many events are held with my name on it…{fast} It's your name they always come back to."


        n "The weight of An Phiast's words hangs in the air. Heavy, but honest."
        show fungie neutral

        f "{w=0.5}...We were good at this, you know."
        show an phiast unhappy
        a "At what?"

        f "Working together."

        a "Yeah… we were."

        n "There's a long pause before Fungie exhales with a small chuckle."
        show fungie smug
        f "{w=0.5}What do you say? One last time - for old time's sake?"
        show an phiast somber
        a "*Chuckles* You always were persistent."

        n "A small smile tugs at the corners of An Phiast's mouth before he finally nods. There's no grand handshake, no dramatic reconciliation - just an understanding. A quiet truce."

        show sunset both at bgspace
        with slow_fade

        n "With that, they both walk away from the bustle of the event, just to take a moment together."

        n "But you don't mind. They have so much to talk about, and finally, they're talking."

        n "{w=0.2}.{w=0.2}.{w=0.2}.And for now, that's enough."
        pause 3.0
        scene black_screen
        with slow_fade
        return

    else:

        n "You stand outside the hotel, waiting to catch the eyes of both An Phiast and Fungie."
        n "A few minutes go by without success, so you resort to jumping and waving your hands in the air. People are staring but you don't care."

        n "Your plan has worked successfully, as An Phiast and Fungie stare at you in shock."
        show fungie annoyed with dissolve:
            xalign 0.7 yalign -1.1 

        show an phiast unhappy with dissolve:
            xalign -0.2 yalign 1.0 xzoom -1.0
        n "You wave them over and they reluctantly come. Even more reluctantly when they see the other making their way to you as well."

        player "Guys… you need to talk this out!"
        show fungie angry:
            easein 0.1 yalign -1.0
        f "What?"

        n "This whole... rivalry thing. You're both mascots of Dingle! Why are you fighting like this?"

        n "{w=0.5}There's an awkward silence as they refuse to speak."

        player "{w=0.1}.{w=0.1}.{w=0.1}.Well?"
        show an phiast seething:
            easein 0.1 yalign 1.0
        a "It's not that simple."

        player "Yes it is! Just talk!"
        show fungie annoyed:
            easein 0.1 yalign -1.1 
        f "And how would you know? You've been here what… a day? And you think you know us?"

        show an phiast unhappy:
            easein 0.1 yalign 1.1
        n "You look to An Phiast for some backup, but he looks away."

        player "Seriously?"
        show an phiast unhappy:
            easein 0.1 yalign 1.0
        a "He's right... You don't know the whole story."

        player "But can't you just talk about why you avoid each other like the plague?"
        show fungie angry
        f "I have nothing to say to him."
        show an phiast angry
        a "Likewise."

        n "This is not going well..."

        n "The situation is tense - both An Phiast and Fungie have a stern look on their face, arms crossed and avoiding eye contact with the other."
        show fungie annoyed
        f "Is that all you wanted to say?"

        n "Fungie is impatient, wanting to return to his waiting fans."

        player "Can't you guys just… I don't know, go for coffee together or something? Talk it out?"
        show an phiast seething
        a "I don't like coffee."
        show fungie angry:
            easein 0.1 yalign -1.1
        f "Well, I don't like you."
        show fungie angry:
            easein 0.3 yalign -1.1
            easein 0.3 yalign -1.0
        n "Fungie huffs at An Phiast in anger, a slight spray of water emerging from his blowhole."
        show an phiast angry:
            easein 2.0 xalign 3.0
        a "Alright, that's enough. I'm leaving now."
        show fungie annoyed
        f "That's right, coward. Walk away like you always do."

        n "An Phiast returns to his group of fans, a forced smile plastered on his face for photos."

        player "Did you really need to do all that?"
        show fungie annoyed:
            easein 0.1 yalign -1.0
        f "I'm doing this for the good of the town. Someone needs to keep the monster away."
        show fungie neutral:
            easein 0.3 yalign -1.1
            easein 0.3 yalign -1.0
        n "With another huff, Fungie turns and walks away,{nw} {done} his perfected, polished smile returning for the cameras."
        hide fungie neutral with dissolve
        n "With another huff, Fungie turns and walks away,{fast} his perfected, polished smile returning for the cameras."

        n "You walk away in complete utter defeat, back towards the bus station."

        n "You're convinced that you can repair their friendship. If only you had gotten to know them both better…"

        n "Maybe you could have another chance"
        
        show sunset at bgspace
        with slow_fade

        n "There's always next year..."

        n "...right?"
        pause 3.0
        scene black_screen
        with slow_fade
        return

label choice_epilogue_bus:
    play music "audio/EmotionalPianoMusic" fadeout 1.0
    n "You linger for a moment, watching as the festival winds down as the last of the crowd takes their photos with Fungie and An Phiast."

    n "You decide you've had your fill. You've seen enough of the town, the festival, and the mascots to know this is something far bigger than you."

    n "Some things can't be easily fixed. Some choices aren't yours to make."

    n "You turn away from the crowds and begin your walk to the bus station. The streets are quieter now, the town settling into the calm after the storm. The distant sound of the pier fills the silence, waves lapping against the walls."

    n "You take one last look back at the town of Dingle, the glow of the streets, the serenity of the waters… and then you step onto the bus, leaving it all behind."

    show sunset at bgspace
    with slow_fade

    n "Are you going to see any of them again? {w=0.5} who knows?"

    pause 3.0

    scene black_screen
    with very_slow_fade
    return
    














