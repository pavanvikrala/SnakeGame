from turtle import Turtle
POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVEMENT = 20
# Creating constants
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_part(pos)


    def add_part(self, pos):
        chitti = Turtle(shape='square')
        chitti.penup()
        chitti.color('green')
        chitti.goto(pos)
        self.parts.append(chitti)

    def extend(self):
        self.add_part(self.parts[-1].position())
    def move(self):
        for part in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[part - 1].xcor()
            new_y = self.parts[part - 1].ycor()
            self.parts[part].goto(new_x, new_y)

        self.parts[0].fd(MOVEMENT)

    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


