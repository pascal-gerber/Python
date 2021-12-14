import turtle
#turtle is a simple draw program
#it doesnt need specific downloads

#the shape is the starter objects shape
#can be ==> triangle, square, circle, arrow, or classic.
turtle.shape("classic")

#these 2 commands are like pen up and pen down
#turtle up will still be able to move but doesn't
#leave any trace

turtle.up()
turtle.down()

#turtle down will start drawing again


#now for the 4 different movement ways
"forward and backward" #other color comment

#######################
#Movement always require a number as movement
#distance
turtle.forward(10)
turtle.backward(20)
#######################

#the 2 other movements are
"left and right"

#######################
#the left and right take an angle number.
turtle.left(90)
turtle.right(180)
#######################


#||||||||||||||||||||||||||||||||||||||||||
turtle.color('red', 'yellow')
turtle.begin_fill()
#those 2 commands will once ended fill, fill up every
#shape it drawn that is closed.
#the borders be red and the inside is yellow

#### should make a cube
def cube():
    for i in range(4):
        turtle.left(90)
        turtle.forward(20)
        

cube()
turtle.end_fill()
#after the end fill, the colors will be applied
#||||||||||||||||||||||||||||||||||||||||||

#moves away and places a red dot.
turtle.forward(30)
#it creates a round dot with a size and color
turtle.dot(10, "Red")
        

#ends turtle
turtle.done()



#Turtle is a gigantic module, it has a very hight amount of content
#there will be more content about turtle



