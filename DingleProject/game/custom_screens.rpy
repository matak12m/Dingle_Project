﻿## Screen with Stats Button
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        # auto "UI/map_%s.png"
        # action Jump ("call_mapUI")
        # You may also use the code below depending on your needs.
        # action ShowMenu("mapUI")
        # This was the same code used in the vlog.

# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.
# label call_mapUI:
#     call screen MapUI



#  this defines the map and its buttons. 
# action == function

# 38 477, 511 380, 621 167, 741 290, 1553 559

screen MapUI:
    

    imagebutton:
        xpos 50
        ypos 445
        idle "gui/map/bay button.png"
        hover "gui/map/bay button hover.png"
      
        action Jump("bay_pressed")

    
        
    imagebutton:
        xpos 576
        ypos 130
        
        idle "gui/map/church button.png"
        hover "gui/map/church button hover.png"
        action Jump("church_pressed")

    imagebutton:
        xpos 680
        ypos 255

        idle "gui/map/town button.png"
        hover "gui/map/town button hover.png"
        action Jump("town_pressed")

    imagebutton:
        xpos 470
        ypos 358
        

        idle "gui/map/tourist button.png"
        hover "gui/map/tourist button hover.png"
        action Jump("tourist_pressed")

    if (TimeProgress > 3):
        imagebutton:
            xpos 1490
            ypos 515
            idle "gui/map/hotel button.png"
            hover "gui/map/hotel button hover.png"
            action Jump("hotel_pressed_ontime")
    else:
        imagebutton:
            xpos 1490
            ypos 515
            idle "gui/map/hotel button.png"
            hover "gui/map/hotel button hover.png"
            action Jump("hotel_pressed_early")
        