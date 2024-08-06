import turtle
wn = turtle.Screen() # creates a graphics window
wn.setup(540,508) # set window dimension

alex = turtle.Turtle() # create a turtle named alex
alex.shape("turtle") # alex looks like a turtle
alex.color("blue") # alex has a color


destination=input("enter direction") #user types the required destination in a dialogue box and that is assigned to the variable 'destination'

if(destination=="north"):

alex.left(90)
alex.forward(254)
elif(destination=="south"):
alex.left(270)
alex.forward(254)
elif(destination=="east"):
alex.right(360)
alex.forward(270)
elif(destination=="west"):
alex.right(180)
alex.forward(270)
else:
alex.penup() #alex will move without drawing (as the pen is lifted up)
alex.goto(-260,230) #alex goes to the respective position
alex.forward(10)
alex.fillcolor((45,137,203)) #alex writes in this color
alex.pencolor((0,0,255)) #outline of alex is in this color
alex.write(" Looks like", font=('Aerial',07,'normal'))+alex.write(" you have typed a wrong destination", font=('Aerial',07,'italic')) #alex writes the given statement within quotes in normal and italic font styles