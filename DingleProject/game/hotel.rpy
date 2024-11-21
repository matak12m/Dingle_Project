# town center script


label house5_pressed:
    scene dingle town at bgspace
    "Dingle Hotel pressed! this is where the animation dingle takes place."



    if APRelationship >= 1 and FRelationship >= 1:
        "both An Phiast and Fungie seem to like you."
    elif APRelationship >= 1 :
        "An Phiast seems to like you."

    elif FRelationship >= 1 :
        "Fungie seems to like you!"

    if APRelationship > 1 or FRelationship > 1:
        "bug report."

    "This is a test button. back to the map you go!"
    jump map_screen



