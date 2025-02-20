
screen frameBox(image):
    frame:
        background Frame("paperframe.png", 16, 16)
        pos(0.2, 0.2)
        anchor (0.0,0.0)
        xysize(700,500)
        add Image(image):
            pos(9,9)
            xysize(700-32,500-32)