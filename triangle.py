
# x, y, z at top center
start = [0, 0, 0]


# draw square in Python Turtle
import turtle
import math
  
t = turtle.Turtle()
 
w = 435
h = 225

# drawing first side
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

def calc_cos(deg):
    return math.cos(math.radians(deg))

def calc_sin(deg):
    return math.sin(math.radians(deg))

def calc_asin(deg):
    return math.asin(deg)

bl = turtle.Turtle()
bl_angle_raw = 70
bl_angle = 90 - bl_angle_raw
bl.left(bl_angle_raw)
bl_length = 200
bl.forward(bl_length)

tl = turtle.Turtle()
tl.goto(0, h)
tl_length = ((bl_length ** 2) + (h ** 2) - (2 * bl_length * h * calc_cos(bl_angle))) ** (1/2)
print(f"TOP LEFT LEN: {tl_length}") # 169.72
tl_angle_raw = math.degrees(math.asin(bl_length * calc_sin(bl_angle) / tl_length))
tl_angle = 90 - tl_angle_raw
print(f"TOP LEFT ANGLE: {tl_angle}") # 24.62
tl.right(tl_angle)
tl.forward(tl_length)

tr = turtle.Turtle()
tr.up()
tr.goto(w, h)
tr.down()
tr_length = ((tl_length ** 2) + (w ** 2) - (2 * tl_length * w * calc_cos(tl_angle))) ** (1/2)
tr_angle_raw = math.degrees(math.asin(tl_length * calc_sin(tl_angle) / tr_length))
tr_angle = 180 - tr_angle_raw
tr.right(tr_angle)
tr.forward(tr_length)
print(f"TOP RIGHT LEN: {tr_length}") # 300.44
print(f"TOP RIGHT ANGLE: {tr_angle}") # 13.75


br = turtle.Turtle()
br.up()
br.goto(w, 0)
br.down()
br_length = ((w ** 2) + (bl_length ** 2) - (2 * w * bl_length * calc_cos(bl_angle_raw))) ** (1/2)
br_angle_raw = math.degrees(math.asin(bl_length * calc_sin(bl_angle_raw) / br_length))
br_angle = 180 - br_angle_raw
br.left(br_angle)
br.forward(br_length)
print(f"BOTTOM RIGHT LEN: {br_length}")
print(f"BOTTOM RIGHT ANGLE: {br_angle}")

