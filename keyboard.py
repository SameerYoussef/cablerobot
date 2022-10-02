from getch import getche
import turtle
import time
import triangle

w = 435
h = 225

angle = 45
length = 200
height = 40

screen = turtle.Screen()
screen.title('Keyboard coordinator')
screen.bgcolor('sky blue')
screen.setup(w + 200, h + 200, 1000)
#screen.setworldcoordinates(-200,-200,200,200)
screen.tracer(0,0)



def read_input(text_t, coordinator):
    global angle
    global length
    global height
    
    while True:
        char = getche() #read the pressed key
        coordinator.clear()
        
        if char == chr(27):
            break
        elif(char==chr(49)):
            angle -= 1            
            print(f"reducing angle to {angle}")
        elif(char==chr(55)):
            angle += 1
            print(f"increasing angle to {angle}")
        elif(char==chr(50)):
            length -= 5
            print(f"reducing length to {length}")
        elif(char==chr(56)):
            length += 5
            print(f"increasing length to {length}")
        elif(char==chr(51)):
            height -= 1
            print(f"reducing height to {height}")
        elif(char==chr(57)):
            height += 1
            print(f"increasing height to {height}")
        
        coordinator.coordinate(angle, length)
        text_t.clear()
        text_t.write(f"{angle}/{length}/{height}", font=("Arial", 16, "normal"))
        screen.update()
    
if __name__ == "__main__":
    triangle.draw_outline(w, h, turtle.Turtle())
    coordinator = triangle.Triangle(w, h, turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle())
    coordinator.coordinate(angle, length)
    screen.update()
    read_input(turtle.Turtle(), coordinator)
    input("Press ENTER to end...")
