## Screen with Stats Button
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

screen MapUI:
    

    imagebutton:
        xpos 130
        ypos 575
        idle "map/house1_idle.png"
        hover "map/bay overlay.png"
        action Jump("bay_pressed")
        
    imagebutton:
        xpos 980
        ypos 368
        idle "map/house2_idle.png"
        hover "map/church overlay.png"
        action Jump("church_pressed")

    imagebutton:
        xpos 1085
        ypos 360
        
        idle "map/house2_idle.png"
        hover "map/town overlay.png"
        action Jump("town_pressed")

    imagebutton:
        xpos 778
        ypos 587
        

        idle "map/house2_idle.png"
        hover "map/tourist office overlay.png"
        action Jump("tourist_pressed")

    if (TimeProgress > 3):
        imagebutton:
            xpos 96
            ypos 65
            idle "map/house1_idle.png"
            hover "map/house1_hover.png"
            action Jump("house5_pressed")

        