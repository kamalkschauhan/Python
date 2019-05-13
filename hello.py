# print("Hello world")
# (1 + 4) * 2
# 239 + 588
# 827 * 827
# (239 + 588) * (239 + 588)
# (239 + 588) ** 2
import turtle

# turtle.left(90)
# turtle.forward(8)
# turtle.left(20)

#turtle.shape("turtle") # this converts its shape to actual turtle
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.reset()
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)

for name in "John", "Sam", "Jill":
    print("Hello " + name)

a = 3.0
b = 2008
c = 2
d = 2.7
x = "mid-2010"
print ("Python %.1f was released in %d. \
The final %d.x version %.1f release came out in %s."
% (a,b,c,d,x))
# Python 3.0 was released in 2008. The final 2.x version 2.7 release came out in mid-2010.

for i in range(10):
    print(i)

print("\n")

total = 0
for i in 5, 7, 11, 13:
    print(i)
    total = total + i
print(total)

print("\n")

# for _ in range(10):
#     print("Hello!")

def line_without_moving():
	for i in range(20):
		turtle.forward(i)
		turtle.penup()
		turtle.forward(5)
		turtle.pendown()

# line_without_moving()
# turtle.exitonclick()

def tilted_square():
  turtle.left(20)     # now we can change the angle only here
  for _ in range(4):
      turtle.forward(50)
      turtle.left(90)

def tilted_square():
  turtle.left(40)
  square()

#from turtle import *
#circle(100)

def square():
  for _ in range(4):
      turtle.forward(100)
      turtle.left(90)


def hexa():
  for _ in range(6):
      turtle.forward(50)
      turtle.left(60)


# tilted_square()
# tilted_square()
# tilted_square()
# hexa()


# square()

# start : experiment
# for _ in range (6):
#     hexa()
#     turtle.forward(50)
#     turtle.right(60)
# end   : experiment

# start : experiment
# from turtle import *
# for i in range(100): # this "for" loop will repeat these functions 500 times
#     forward(i)
#     left(91)
# end   : experiment

# start : experiment
# from turtle import *
# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
# for x in range(360):
#     pencolor(colors[x % 6])
#     width(x / 100 + 1)
#     forward(x)
#     left(59)
# end   : experiment



# start : experiment
# from turtle import *
# import random
#
# for n in range(60):
#     penup()
#     goto(random.randint(-400, 400), random.randint(-400, 400))
#     pendown()
#
#     red_amount   = random.randint( 0,  30) / 100.0
#     blue_amount  = random.randint(50, 100) / 100.0
#     green_amount = random.randint( 0,  30) / 100.0
#     pencolor((red_amount, green_amount, blue_amount))
#
#     circle_size = random.randint(10, 40)
#     pensize(random.randint(1, 5))
#
#     for i in range(6):
#         circle(circle_size)
#         left(60)
# end   : experiment


# A module is a single file (or files) that are imported under one import and used. e.g.
# import my_module
#
# A package is a collection of modules in directories that give a package hierarchy.
# from my_package.timing.danger.internets import function_of_love
# pip install matplotlib
# python -m matplotlib

greeting = 'Hello'
print (greeting[1])
print (greeting[1:])
print (len(greeting))
print (greeting + 'World')

greeting[1:]

squares_list = [0,1,4,7,12,17,16]

print (squares_list)

# direction = -30
# if direction > 0 :
#     turtle.forward(direction)
# else:
#     turtle.left(180)
#     turtle.forward(-direction)


my_variable = "       I Am Capitalised"
print(my_variable)
my_stripped = my_variable.strip()
print(my_stripped)
my_lower = my_variable.lower()
print(my_lower)

def move():
    direction = input("Go left or right? ")
    if direction == "left":
        turtle.left(60)
        turtle.forward(50)
    if direction == "right":
        turtle.right(60)
        turtle.forward(50)

# move()

import pandas as pd
print("\n")
print("\n")
print("Panda Series")

x = pd.Series([6,3,4,6])

print (x)

import numpy as np
print("\n")
print("\n")
print("Panda DataFrame")

df = pd.DataFrame(np.random.randn(4,3))

print (df)

import matplotlib as mpl

turtle.exitonclick()

# import gc
# found = []
# for obj in gc.get_objects():
# 	if type(obj) == type(tilted_square):
# 		if obj.__name__ == tilted_square.__name__:
# 			found.append(obj)

# print(found)

# bonus: you could have a separate function for drawing a square,
# which might be useful later:
