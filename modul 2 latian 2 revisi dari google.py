# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:47:31 2022

source: https://www.w3resource.com/python-exercises/math/python-math-exercise-27.php
modified by: alfarizqi wira anadyar-065002200034
"""

from math import radians, sin, cos, acos
print('this program will calculate the distance between to point of location')
loc1=input('the first location name: ')
loc2=input('the second location name: ')
print('==================================')

print("Input coordinates of two points of locations:")
x1 = radians(float(input("latitude location 1: ")))
y1 = radians(float(input("longtitude location 1: ")))
print('==================================')
x2 = radians(float(input("latitude location 2: ")))
y2 = radians(float(input("longtitude location 2: ")))

if (x1 == x2) and (y1 == y2):
    dist = 0
else :
    dist = 6371.01 * acos(sin(x1)*sin(x2) + cos(x1)*cos(x2)*cos(y1 - y2))

print('==================================')
print("The distance between",loc1,'and',loc2,"is %.2f km." % dist)
print('Alfarizqi Wira Anadyar - 065002200034 - @alfarizqiwira')