
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like
image main_menu_background = "gui/menu/cover art.png"

image title_animated:
    "gui/menu/Title.png"
    linear 1.0 zoom 0.95 truecenter
    linear 1.0 zoom 1.05 truecenter
    repeat


image Start_animated:
    "gui/menu/Start.png"
    yzoom 1.0
    linear 0.5 yzoom 0.98
    linear 1.0 yzoom 1.02 
    linear 0.5 yzoom 1.0
    repeat

image Load_animated:
    "gui/menu/Load.png"
    yzoom 1.0
    linear 0.5 yzoom 0.98
    linear 1.0 yzoom 1.02 
    linear 0.5 yzoom 1.0
    repeat

image Settings_animated:
    "gui/menu/Settings.png"
    yzoom 1.0
    linear 0.5 yzoom 0.98
    linear 1.0 yzoom 1.02 
    linear 0.5 yzoom 1.0
    repeat

image About_animated:
    "gui/menu/About.png"
    yzoom 1.0
    linear 0.5 yzoom 0.98
    linear 1.0 yzoom 1.02 
    linear 0.5 yzoom 1.0
    repeat

image Help_animated:
    "gui/menu/Help.png"
    yzoom 1.0
    linear 0.5 yzoom 0.98
    linear 1.0 yzoom 1.02 
    linear 0.5 yzoom 1.0
    repeat

image Quit_animated:
    "gui/menu/Quit.png"
    yzoom 1.0
    linear 0.5 yzoom 0.98
    linear 1.0 yzoom 1.02 
    linear 0.5 yzoom 1.0
    repeat


screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "main_menu_background"
    add "title_animated"

    imagebutton  focus_mask True:
        

        idle "gui/menu/Start.png"
        hover "Start_animated"
      
        action Start()

    imagebutton  focus_mask True:

        idle "gui/menu/Load.png"
        hover "Load_animated"
        action ShowMenu("load")   
        
    imagebutton  focus_mask True:

        
        idle "gui/menu/Settings.png"
        hover "Settings_animated"
        action ShowMenu("preferences")



    imagebutton  focus_mask True:
    
        idle "gui/menu/About.png"
        hover "About_animated"
        action ShowMenu("about")

    
    imagebutton  focus_mask True:
  
        idle "gui/menu/Help.png"
        hover "Help_animated"
        action ShowMenu("help")


    if renpy.variant("pc"):
        ## The quit button is banned on iOS and unnecessary on Android and
        ## Web.
        imagebutton  focus_mask True:
  
            idle "gui/menu/Quit.png"
            hover "Quit_animated"
            action Quit(confirm=not main_menu)
        
    # vbox:
    #     xpos 60
    #     yalign 0.5
    #     spacing 6

    #     textbutton _("Start") action Start()

    #     textbutton _("Load") action ShowMenu("load")

    #     textbutton _("Preferences") action ShowMenu("preferences")

    #     textbutton _("About") action ShowMenu("about")

    #     if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

    #         ## Help isn't necessary or relevant to mobile devices.
    #         textbutton _("Help") action ShowMenu("help")

    #     if renpy.variant("pc"):

    #         ## The quit button is banned on iOS and unnecessary on Android and
    #         ## Web.
    #         textbutton _("Quit") action Quit(confirm=not main_menu)

