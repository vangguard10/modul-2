# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 08:36:11 2022

@author: alfarizqi wira anadyar
"""

#pembukaan
name=input('what is your name? ')
print('hai',name,'wellcome to this program')
print('this program function is to help you to calculate a distance between two places in the world surface.')
print("let's get started")
print()

#input
import math as m
lok1 = input('name of location 1: ')
lat1 = float(input('latitude of location 1[x]: '))
lon1 = float(input('longtitude of location 1[y]: '))
lok2 = input('name of location 2: ')
lat2 = float(input('latitude of location 2[x]: '))
lon2 = float(input('longtitude of location 2[y]: '))

#processing
jarak = m.dist([lat1,lon1], [lat2,lon2])
#output
print()
print('the distance between',lok1,'dan',lok2, 'is:',jarak)