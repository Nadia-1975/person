# ---------1) черепаха-------
from turtle import *

def star(length):
    for step in 1,2,3:
        forward(120)
        left(360/3)
    print("Это треугольник.")
    star(length)



