# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:47:31 2022

@author: alfarizqi wira anadyar
"""

import math as m
print('this program will calculate the distance between to point of location')
loc1=input('the first location name: ')
loc2=input('the second location name: ')
print('==================================')

print("Input coordinates of two points of locations:")
x1 = m.radians(float(input("latitude location 1: ")))
y1 = m.radians(float(input("longtitude location 1: ")))
print('==================================')
x2 = m.radians(float(input("latitude location 2: ")))
y2 = m.radians(float(input("longtitude location 2: ")))

if (x1 == x2) and (y1 == y2):
    dist = 0
else :
    dist = 6371.01 * m.acos(m.sin(x1)*m.sin(x2) + m.cos(x1)*m.cos(x2)*m.cos(y1 - y2))

print('==================================')
print("The distance between",loc1,'and',loc2,"is %.2f km." % dist)
print('Alfarizqi Wira Anadyar - 065002200034 - @alfarizqiwira')
