#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:08:07 2020

@author: stephen
"""

from math import floor
import argparse

#Bread recipe calculator

if __name__ == '__main__':
    # Construct the argument parser
    ap = argparse.ArgumentParser()

    # Add the arguments to the parser
    ap.add_argument("-v", "--volume", required=False,
       help="Volume of your cooking pan(s) in litres.")
    ap.add_argument("-e", "--eggs", required=False,
       help="Desired number of eggs to use. \nOverrides the recipe based on container volume.")
    args = vars(ap.parse_args())
    
    OGVolume = 1.8*2
    
    if args['volume'] is not None:
        #Find nearest whole egg (round down).
        NewEggCount = floor((float(args['volume'])/OGVolume)*10)
        EggRatio = NewEggCount/10   
    
    if args['eggs'] is not None:
        NewEggCount = int(args['eggs'])
        EggRatio = NewEggCount/10

    s = '''\
        
    Tangzhong
    - {tflour} g flour mix
    - {water} g water
    
    Wet Mix
    - {eggs} large eggs
    - {oil} g oil
    - {milk} g 3.25% milk
    
    Dry Mix
    - {dflour} g flour mix
    - {sugar} g sugar
    - {salt} g salt
    - {yeast} g yeast\
    '''.format(
    tflour = floor(EggRatio*70),
    water = floor(EggRatio*250),
    eggs = floor(NewEggCount),
    oil = floor(EggRatio*130),
    milk = floor(EggRatio*250),
    dflour = floor(EggRatio*620),
    sugar = floor(EggRatio*30),
    salt = floor(EggRatio*16),
    yeast = floor(EggRatio*7)
    )
    
    print(s)

    


#TotalContainerVolume = 2.2*2

#OGVolume = 1.8*2

#Recipe
'''
Tangzhong 
- 70 g flour 
- 250 g water 

Wet 
- 10 eggs 
- 130 g oil
- 250 g milk 

Dry
- 620 g flour mix
- 30 g sugar
- 16 g salt
- 7 g yeast 
'''

#Find nearest whole egg (round down).

#NewEggCount = floor((TotalContainerVolume/OGVolume)*10)
#EggRatio = NewEggCount/10

# Egg count target override
# NewEggCount = 12
# EggRatio = NewEggCount/10
