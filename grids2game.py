#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:12:45 2021

@author: alexander
"""


   

def grid_ss():
    x = int(input('Hello, I\'m here to make you a grid. How many columns would you like in your grid? '))
    y = int(input('Wonderful! Now, how many rows would you like? '))
    
    a = '+ - +'
    b = '\n|   |'
    c = '\n+ - +'

    aa = ' - +'
    bb = '   |'
    cc = ' - +'
 
    grid = a + aa*(x-1) + (b + bb*(x-1) + c + cc*(x-1))*y
    ## b + bb
    
    
    print(grid)
    
    # the game begins
    
    print('Now, let\'s have some fun!\n')
    if x and y < 3:
        print('''I\'m going to run the program again. This time make sure your grid 
has more than 3 columns and 3 rows.''')
        grid_ss()
        
    player = input('What is the first letter of your name? ')
    
    sqon = (4*x) + 4 #sqon = square one of grid
    
    def insert_initial():
        grl = list(grid) # separate string into a list
        grl[sqon] = player # changes empty space in 1st square to initial
        grida = "".join(grl) #joings the list to make the string with initial in 1st square
        print(grida)
    def insert_minitial():
        grl = list(grid) # separate string into a list
        grl[sqon] = player # changes empty space in 1st square to initial
        grida = "".join(grl) #joings the list to make the string with initial in 1st square
        
        grl = list(grida) # separate string into a list
        grl[sqon] = player # changes empty space in 1st square to initial
        grida = "".join(grl) #joings the list to make the string with initial in 1st square
        print(grida)
        
    
    insert_initial()
    
    
    horz = 'H'
    vert = 'V'
    
    timer = 1
    
    leftwll = []
    rightwll
    topwll = [((4*x) + 4), ()]
    botwll
    
    while timer < x*y:
        timer = timer + 1 #limit the times you can move to the amount of colomns
        if sqon == (4*x) + 4 or 
        mvmt = input('''Would you like to go horizontal or vertical? For 
horizontal enter capital H, for vertical enter capital V.''') #mvmt movement
        if mvmt == horz:
            grl = list(grid) # separate string into a list
            grl[sqon] = player # changes empty space in 1st square to initial
            grida = "".join(grl) #joings the list to make the string with initial in 1st square
            sqon = sqon + 4 
            grl = list(grida) # separate string into a list
            grl[sqon] = player # changes empty space in 1st square to initial
            grida = "".join(grl) #joings the list to make the string with initial in 1st square
            print(grida)
            grid = grida 
        if mvmt == vert:
            grl = list(grid) # separate string into a list
            grl[sqon] = player # changes empty space in 1st square to initial
            grida = "".join(grl) #joings the list to make the string with initial in 1st square
            sqon = sqon + ((4*x) + 2)*2#equation to move initial down two lines into square below
            grl = list(grida) # separate string into a list
            grl[sqon] = player # changes empty space in 1st square to initial
            grida = "".join(grl) #joings the list to make the string with initial in 1st square
            print(grida)
            grid = grida
    #elif mvmt == vert:
    
   
        
        
grid_ss()