# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration----
shape = "circle"
size= .5
colour= "palegreen"
score= 0

font_setup = ("Times New Roman", 20, "italic")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
neb = trtl.Turtle(shape=shape)
neb.turtlesize(size)
neb.fillcolor(colour)
neb.pencolor(colour)
neb.speed(0)

keeper = trtl.Turtle(shape="circle")
keeper.ht()
keeper.penup()
keeper.goto(-350, 250)
keeper.pendown()
keeper.pencolor("limegreen")
font = ("Times New Roman", 30, "bold")

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(290, -350)
counter.pendown()
counter.pencolor("aquamarine")

#-----game functions--------
def turtle_clicked (x,y):
    move_neb()
    score_keeper()
def move_neb ():
    neb.penup()
    neb.ht()
    new_xpos= random.randint(-400, 400)
    new_ypos= random.randint(-300, 300)
    neb.goto(new_xpos, new_ypos)
    neb.showturtle()     
def score_keeper ():
    global score
    score+=1
    keeper.clear()
    keeper.write (score, font=font)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    game_over()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
def game_over ():
    neb.penup()
    neb.goto(500 , 500)
    wn.bgcolor("midnightblue")

#-----events----------------
neb.onclick(turtle_clicked)


wn = trtl.Screen()
wn.bgcolor("dimgrey") # customization - changed background colour
wn.ontimer(countdown, counter_interval)
wn.mainloop()