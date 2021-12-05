##Elijah Stroot
## CS101 Lab
## December 1, 2021
## Assignment 12

####Algorithm:
'''
1. Create the Main mother class called Point that contains an x, a y, and a color
2. Create methods inside the class
3. Create a class called Box with extra x y cordinates
4. Create methods inside the box class
5. Create methods a class called Boxfilled
6. Create a class called Circle with a radius as well in addition to the x,y cordinate
7. Create a class called Circle fill that will fill the circle with a fill color. 
'''
import turtle
class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    def draw_action(self):
        turtle.dot()
class Box(Point):
    def __init__(self, x, y, color, x1, x2):
        self.x1 = x1
        self.x2 = x2
        super().__init__(x, y, color)

    def draw_action(self):
        "draws a box"
class BoxFilled(Box):
    def __init__(self, x, y, color):
        super().__init__(x,y,color)

class Circle(Point):
    def __init__(self, x,y, color, radius):
        self.radius = radius 
        super().__init__(x,y, color)
    
class CircleFilled(Circle):
    def __init__(self, x, y, radius, color, fill_color):
        self.fill_color = fill_color
        super().__init__(x, y, radius, color)
    def draw_action(self):
        "draws a circle"

