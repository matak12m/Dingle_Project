# ending script


#max AP points you can gain: 7
#max F points you can gain: 5
#currently you start with 1 in each.


label epilogue:



    n "The day flies by, filled with exciting talks, breathtaking short films, and addictive games."

    n "There's so many people..."

    n "And the whole event is plastered with the visage or An Phiast, with stickers of him everywhere."

    n "It's an amazing experience, all in his honour."

    n "As you reluctantly leave the electric buzz of the busy hotel, you see An Phiast and Fungie on opposite sides of the hotel yard, each surrounded by their own crowd of fans."

    n "Cameras flash as they pose for photos, their smiles polished, their presence commanding. Two legendary mascots of Dingle, both larger than life, yet separated by something unspoken."

    n "Your bus leaves soon. Who do you want to say goodbye to?"




    menu:
        "An Phiast":
            jump choice_epilogue_anphiast
        "Fugnie":
            jump choice_epilogue_fungie
        "Make both of them talk together":
            jump choice_epilogue_both
        "Go on the bus":
            jump choice_epilogue_bus







label choice_epilogue_anphiast:
    play music "audio/EmotionalPianoMusic" fadeout 1.0

    if (APRelationship > 4):

        n "You make your way towards An Phiast, making your way through the group of fans now heading back to the hotel."

        a "You stuck around?"

        player "Of course! I had a really good time."

        a "Good!"

        n "An Phiast beams with happiness, knowing you enjoyed his festival."

        a "That's what it's all about, isn't it? Something to bring people together. I hope it was worth your long trip."

        player "It was."

        n "You nod, thinking of all the great memories you've made here in Dingle. Memories within the festival, with the townspeople…"

        n "…and with An Phiast."

        n "There's an understanding silence between you as you admire the bustling hotel from afar, people from all over the world admiring An Phiast's legacy."

        a "Before you go… *Pause* I just want to say thank you - for sticking by me. It means a lot to me, and I'll never forget it."

        n "His voice is steady, assured, with a new confidence to him."

        n "You smile, remembering the shy little green mascot he used to be."

        n "Looking at him now, he's a completely changed person. He stands taller, no longer afraid to stand out."

        n "He smiles excitedly as more fans emerge from the hotel, calling his name."

        a "I should go… Have a safe journey home."

        n "He smiles softly as he begins to walk away. Before he's out of earshot, he stops and turns around."

        a "You'll come back next year, won't you?"

        n "You laugh" 

        player "Of course!"

        n "With that, you part ways. He returns to his adoring fans as you make your way back into Dingle to catch the bus."

        n "You meant every word you said, and you can't wait to come back."

        show sunset an phiast at bgspace

        n "Dingle is going to be great next year..."
        scene black_screen
        with very_slow_fade
        return
    else:

        n "You make your way towards An Phiast, making your way through the group of fans excitedly asking for photos."

        n "You fail to catch his eye as he poses for silly selfies. As a last resort, you give him a light tap on the arm."

        a "Oh, Can I help you?"

        n "His smile to you is forced, for the sake of the public eye."

        player "Oh sorry, I uh… I just wanted to say goodbye."

        a "You're leaving?"

        n "He continues to pose for pictures with fans, speaking in between each photo."

        player "Yeah…"

        a "Well, I hope you enjoyed Animation Dingle. We hope to see you again next year!"

        n "His response is recited, almost robotic. He avoids your eyes as he speaks."

        player "Thanks…"

        n "He turns away for more photos with fans, leaving his back turned to you."

        n "With nothing left to do, you take one last look at the beach."

        show sunset at bgspace

        n "While you had a fantastic time, you wish you had gotten to know An Phiast a little better."

        n "There's always next year..."
        
        n "...right?"
        scene black_screen
        with very_slow_fade
        return
label choice_epilogue_fungie:
    play music "audio/EmotionalPianoMusic" fadeout 1.0
    if (FRelationship > 3):

        n "You make your way towards Fungie, making your way through the group of fans who have just bombarded him with selfies."

        f "Well, well. Look who it is!"

        n "He beams with happiness as you roll your eyes with a smirk."

        f "Did you enjoy your time at Dingle?"

        player "I had a great time."

        f "You're very welcome for that."

        n "He teases, but you can't help but laugh."

        f "Really, though, I'm glad. And uh.. *Pause* Thank you."

        player "For what?"

        f "For seeing past all that noise."

        player "What do you mean?"

        f "Oh, you know… *He gestures vaguely* For seeing past all that arrogant, golden boy act."

        f "It's nice to be reminded that there's… well, that there's more to me than that."

        player "There always was."

        f "*He smiles softly with a chuckle* Don't go making me soft now."

        f "Get home safe, won't you?"

        n "You smile"

        player " I will."
            
        n "With that, he reluctantly walks away, re-joining his group of fans by the hotel entrance, eager to take photos."

        n "You make your way back to your bus, with only one thought on your mind:"

        show sunset fungie at bgspace

        n "Dingle is going to be great next year..."
        scene black_screen
        with very_slow_fade
        return
    else:

        n "You make your way towards Fungie, making your way through the group of photographers and eager fans taking photos."

        player "Fungie?"

        n "You call out to him amidst the bright flashes of cameras, people asking him to pose, and people with microphones asking questions."

        n "You call out once again, waving your arms to catch his attention."

        n "His eyes meet yours, and a wave of annoyance washes over his face."
        f "Can't you see I'm busy?"

        n "He speaks through a small gap in his mouth, not willing to break the smile for the cameras."

        player "I just want to say goodbye..."

        n "His sharp eyes meet yours yet again. He rolls his eyes before resuming his poses and answering questions for fans."

        n "Defeated, you leave him alone and make your way to the bus station."

        n "You're positive that there's more to Fungie than his arrogant façade.  Maybe if you had gotten to know him better, things would be different…"

        n "At least there's always next year."

        show sunset

        n "...right?"
        scene black_screen
        with very_slow_fade
        return

label choice_epilogue_both:
    play music "audio/EmotionalPianoMusic" fadeout 1.0
    if (APRelationship > 4 and FRelationship > 4):

        n "You manage to catch the eyes of both Fungie and An Phiast, who tower over the crowd below them."

        n "You wave them over. As they approach you, their excited smiles quickly fade as they realise the other is also heading for you."

        f "Did you need something?"

        n "Fungie turns his nose at An Phiast, who is sheepishly looking away."

        player "I wanted to speak to you both. Together."

        n "You watch as they shift uncomfortably, looking for a way out."

        player "Aren't you both tired of this?"

        a "Of what?"

        n "This whole… rivalry thing. You both clearly care about this town, but you act like there's not enough space for the both of you."

        n "An Phiast and Fungie stand in stunned silence, mouths agape like a fish out of water."

        player "Well?"

        n "You stand your ground, arms crossed as you wait for a response."

        n "Fungie, now oddly sheepish, rubs the back of his neck before speaking to An Phiast."

        f "I mean… I guess… I don't know… this whole festival… it's all about you, you know?"

        n "He mumbles, barely a whisper."

        a "What?"

        f "You heard me. I guess I was just… jealous? *Sighs* I hated seeing your name on everything. A whole festival about you? While I get a statue here, a mention there?"

        n "Fungie looks away, refusing to meet An Phiast's eyes."

        a "Jealous of me? I was jealous of you!"

        n "An Phiast exclaims in utter shock."

        a "You don't need a festival to be remembered. This town adores you every single day! No matter what I do, how many events are held with my name on it… It's your name they always come back to."

        n "The weight of An Phiast's words hangs in the air. Heavy, but honest."

        f "We were good at this, you know."

        a "At what?"

        f "Working together."

        a "Yeah… we were."

        n "There's a long pause before Fungie exhales with a small chuckle."

        f "What do you say? One last time - for old time's sake?"

        a "*Chuckles* You always were persistent."

        n "A small smile tugs at the corners of An Phiast's mouth before he finally nods. There's no grand handshake, no dramatic reconciliation - just an understanding. A quiet truce."

        n "And for now, that's enough."

        show sunset both at bgspace

        n "Who knows what all three of you will be up to next year?"
        scene black_screen
        with very_slow_fade
        return

    else:

        n "You stand outside the hotel, waiting to catch the eyes of both An Phiast and Fungie."
        n "A few minutes go by without success, so you resort to jumping and waving your hands in the air. People are staring but you don't care."

        n "Your plan has worked successfully, as An Phiast and Fungie stare at you in shock."

        n "You wave them over and they reluctantly come. Even more reluctantly when they see the other making their way to you as well."

        player "Guys… you need to talk this out!"

        f "What?"

        n "This whole... rivalry thing. You're both mascots of Dingle! Why are you fighting like this?"

        n "There's an awkward silence as they refuse to speak."

        player "Well?"

        a "It's not that simple."

        player "Yes it is! Just talk!"

        f "And how would you know? You've been here what… a day? And you think you know us?"

        n "You look to An Phiast for some backup, but he looks away."

        player "Seriously?"

        a "He's right... You don't know the whole story."

        player "But can't you just talk about why you avoid each other like the plague?"

        f "I have nothing to say to him."

        a "Likewise."

        n "This is not going well."

        n "The situation is tense - both An Phiast and Fungie have a stern look on their face, arms crossed and avoiding eye contact with the other."

        f "Is that all you wanted to say?"

        n "Fungie is impatient, wanting to return to his waiting fans."

        player "Can't you guys just… I don't know, go for coffee together or something? Talk it out?"

        a "I don't like coffee."

        f "Well, I don't like you."

        n "Fungie huffs at An Phiast in anger, a slight spray of water emerging from his blowhole."

        a "I'm going to leave now."

        f "That's right, coward. Walk away like you always do."

        n "An Phiast returns to his group of fans, a forced smile plastered on his face for photos."

        player "Did you really need to do all that?"

        f "I'm doing this for the good of the town. Someone needs to keep the monster away."

        n "With another huff, Fungie turns and walks away, his perfected, polished smile returning for the cameras."

        n "You walk away in complete utter defeat, back towards the bus station."

        n "You're convinced that you can repair their friendship. If only you had gotten to know them both better…"

        n "Maybe you could have another chance"

        n "There's always next year..."

        show sunset at bgspace
        n "...right?"
        scene black_screen
        with very_slow_fade
        return

label choice_epilogue_bus:
    play music "audio/EmotionalPianoMusic" fadeout 1.0
    n "You linger for a moment, watching as the festival winds down as the last of the crowd takes their photos with Fungie and An Phiast."

    n "You decide you've had your fill. You've seen enough of the town, the festival, and the mascots to know this is something far bigger than you."

    n "Some things can't be easily fixed. Some choices aren't yours to make."

    n "You turn away from the crowds and begin your walk to the bus station. The streets are quieter now, the town settling into the calm after the storm. The distant sound of the pier fills the silence, waves lapping against the walls."

    n "You take one last look back at the town of Dingle, the glow of the streets, the serenity of the waters… and then you step onto the bus, leaving it all behind."

    show sunset at bgspace

    n "Are you going to see any of them again? who knows?"

    n "There's always next year..."

    scene black_screen
    with very_slow_fade
    return
    














