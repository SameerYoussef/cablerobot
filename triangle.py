from turtle import *
import turtle
import math

class Triangle():
    def __init__(self, w, h, bl, tl, tr, br, dr):
        self.w = w
        self.h = h
        self.bl = bl
        self.tl = tl
        self.tr = tr
        self.br = br
        self.dr = dr

    def coordinate(self, angle, length, drop):
        def calc_cos(deg):
            return math.cos(math.radians(deg))

        def calc_sin(deg):
            return math.sin(math.radians(deg))

        w = self.w
        h = self.h
        
        dr = self.dr
        dr.up()
        dr.goto(-1*w/2 - 20, h/2)
        dr.right(90)
        dr.down()
        dr.forward(drop)

        bl = self.bl
        bl.up()
        bl.goto(-1*w/2, -1*h/2)
        bl.down()
        bl_angle_raw = angle
        bl_angle = 90 - bl_angle_raw
        bl.left(bl_angle_raw)
        bl_length = length
        bl.forward(bl_length)

        tl = self.tl
        tl.up()
        tl.goto(-1*w/2, h/2)
        tl.down()
        tl_length = ((bl_length ** 2) + (h ** 2) - (2 * bl_length * h * calc_cos(bl_angle))) ** (1/2)
        tl_angle_raw = math.degrees(math.asin(bl_length * calc_sin(bl_angle) / tl_length))
        tl_angle = 90 - tl_angle_raw
        tl.right(tl_angle)
        tl.forward(tl_length)

        tr = self.tr
        tr.up()
        tr.goto(w/2, h/2)
        tr.down()
        tr_length = ((tl_length ** 2) + (w ** 2) - (2 * tl_length * w * calc_cos(tl_angle))) ** (1/2)
        tr_angle_raw = math.degrees(math.asin(tl_length * calc_sin(tl_angle) / tr_length))
        tr_angle = 180 - tr_angle_raw
        tr.right(tr_angle)
        tr.forward(tr_length)

        br = self.br
        br.up()
        br.goto(w/2, -1*h/2)
        br.down()
        br_length = ((w ** 2) + (bl_length ** 2) - (2 * w * bl_length * calc_cos(bl_angle_raw))) ** (1/2)
        br_angle_raw = math.degrees(math.asin(bl_length * calc_sin(bl_angle_raw) / br_length))
        br_angle = 180 - br_angle_raw
        br.left(br_angle)
        br.forward(br_length)
        
        drop2 = drop ** 2
        return (bl_length ** 2 + drop2) ** (1/2), (tl_length ** 2 + drop2) ** (1/2), (tr_length ** 2 + drop2) ** (1/2), (br_length ** 2 + drop2) ** (1/2)
    
    def clear(self):
        for t in [self.bl, self.tl, self.tr, self.br, self.dr]:
            t.clear()
            t.reset()

def draw_outline(w, h, t):
    # drawing first side
    t.up()
    t.goto(-1*w/2, -1*h/2)
    t.down()
    t.forward(w) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
    
    # drawing second side
    t.forward(h) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
    
    # drawing third side
    t.forward(w) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
    
    # drawing fourth side
    t.forward(h) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree

if __name__ == "__main__":
    w = 435
    h = 225
    angle = 45
    length = 200
    height = 40
    screen = turtle.Screen()
    screen.tracer(0,0)
    screen.title("Coordinator")
    screen.bgcolor('sky blue')
    screen.screensize(400,300)
    draw_outline(w, h, turtle.Turtle())
    triangle = Triangle(w, h, turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle())
    triangle.coordinate(angle, length)
    screen.update()
    input("Press ENTER to end...")
    