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
        xpos 618
        ypos 670
        idle "map/house1_idle.png"
        hover "map/house1_hover.png"
        action Jump("house1_pressed")
        
    imagebutton:
        xpos 1596
        ypos 200
        idle "map/house2_idle.png"
        hover "map/house2_hover.png"
        action Jump("house2_pressed")

    imagebutton:
        xpos 596
        ypos 165
        idle "map/house2_idle.png"
        hover "map/house2_hover.png"
        action Jump("house3_pressed")

    imagebutton:
        xpos 1596
        ypos 865
        idle "map/house2_idle.png"
        hover "map/house2_hover.png"
        action Jump("house4_pressed")

    imagebutton:
        xpos 96
        ypos 65
        idle "map/house2_idle.png"
        hover "map/house2_hover.png"
        action Jump("house5_pressed")

        