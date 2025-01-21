# town center script


label tourist_pressed:
    scene dingle town at bgspace
    "Tourist Center Pressed! There's a statue of Fungie here."

    # FUNGIE ONLY DIALOGUE

    player "You make your way to the tourist centre, where you come across a large statue of a very
    familiar dolphin."
    player "The statue is in pristine condition, and is almost lifelike. You reach out to touch it's smooth
    surface..."
    f "Did you need something?"
    player " *You jump back in shock as the statue comes to life* No, I'm sorry! I thought you were a
    statue…"
    f " *He chuckles* They did a good job, didn't they? But don't mistake me for some cold block
    of stone - I'm the real deal."
    player " *You look him up and down* …The resemblance is uncanny. Is that not weird to see
    yourself in stone every day?"
    f "Not at all, in fact - I'm grateful for the honour. It's a big responsibility being the face of this
    town; people come from all over just to catch a glimpse of me!"
    player "Well… people seem to talk about An Phiast more than you… He's a mascot like you,
    right?"
    f "An Phiast? *Pause* I'm not surprised. He has a way of… lurking in people's heads, even
    when he doesn't belong there."
    # ***************************************************************************
    # *******
    # Option 1. player "What do you mean by that? Is he dangerous?"
    # f "Let's just say… I had to work hard to make this town what it is today – a place people love
    # to visit. But not everyone shared that vision."
    # player "But-"
    # f " *Interrupts* Just… keep your distance. Trust me on this – this town needs me more than
    # it needs him.
    # Option 2. player "I've met him. He seemed… kind. Are you sure he's as bad as
    # you say?"
    # f " *Flicker of anger* Kind? Sure – that's how he wants you to see him. It's all an act, nothing
    # more."
    # player "No, he's not like that! He genuinely cares for the people in this town, just like you."
    # f "Forget it. Believe what you want, but don't say I didn't warn you."
    # Option 3. player "People seem to have strong options on him. Why is that?"
    # f "*Pause* He's… complicated. People don't know what to make of him. Some see a
    # monster, others see him as misunderstood.
    # player "And what do you see?"
    # f "I see someone who doesn't belong here. Someone who never has. But I don't expect you
    # to understand."
    # ***************************************************************************
    # *******
    # player "Wait but-"
    # u "Mammy, look! It's Fungie!"
    # player "Your conversation is interrupted by a child pointing excitedly at Fungie. His demeanor
    # snaps back into his polished, public self upon hearing his name."
    # f "Well hello there, little one!"
    # player "As Fungie begins to walk away to join the mother and child for pictures, he pauses."
    # f "Look… Dingle has a lot to offer and explore but just… keep to what's safe. Some things are
    # better left alone."
    # player "With that, Fungie walks away."


    
    jump after_house_choice