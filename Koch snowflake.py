import turtle

MyTurtle = turtle.Turtle()
MyTurtle.shape("circle")
MyTurtle.shapesize(0.25)
MyTurtle.speed("fastest")
MyTurtle.up()
MyTurtle.setx(-300)
MyTurtle.sety(180)
MyTurtle.down()

def GetPattern(degree):

    if (degree == 1):
        return "FRRFRRF"
    else:
        return (GetPattern(degree-1).replace("F","FLFRRFLF"))

def TriangleFractal(degree):

    distance = 600/(3**(degree - 1))
    pattern = GetPattern(degree)
    
    for a in range(0,len(pattern)):
        if(pattern[a]== "F"):
            MyTurtle.forward(distance)
        elif(pattern[a]== "L"):
            MyTurtle.left(60)
        elif(pattern[a]== "R"):
            MyTurtle.right(60)

    MyTurtle.right(120)

fractalDegree = input("What degree would you like\nthe fractal to be rendered to?")
fractalDegree = int(fractalDegree)

for i in range(1,(fractalDegree + 1)):
    TriangleFractal(i)
    
MyTurtle.up()
MyTurtle.hideturtle()
MyTurtle.left(30)
MyTurtle.forward(10)
MyTurtle.left(90)

while(True):
    MyTurtle.forward(100)
    MyTurtle.left(180)