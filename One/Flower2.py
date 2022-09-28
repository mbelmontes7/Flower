import turtle
wn = turtle.Screen()
wn.bgcolor("#A45C40")

#1
tur1 = turtle.Turtle()
tur1.hideturtle()
tur1.fillcolor("#E4B7A0")
tur1.begin_fill()
tur1.pensize(3)
tur1.speed(900)
tur1.end_fill()

#2
tur2 = turtle.Turtle()
tur2.penup()
tur2.goto(200,200)
tur2.color("#C38370")
tur2.pensize(3)
tur2.speed(900) 
tur2.pendown()
tur1.hideturtle()


#3 
tur3 = turtle.Turtle()  
tur3.penup()
tur3.goto(-200, -200)
tur3.color("#F6EEE0")
tur3.pendown()
tur3.pensize(3)
tur3.speed(900)



# # tur4 = turtle.turtle ()




# # tur5 = turtle.turtle ()


#for range
for i in range(150):
 tur1.forward(i)
 tur1.right(75)
 tur2.forward(i)
 tur2.left(100)
 tur2.left(90)
 tur3.backward(i)
 tur3.right(100)
 tur3.left(50)




# turtle.done() 
wn.exitonclick()