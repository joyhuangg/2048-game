# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 11:08:55 2017

@author: joyhuangg
"""
import numpy as np
import random
from Tkinter import *
from copy import deepcopy

#color dictionaries for the colors of the number tiles
colors = {0: 'white', 2: 'lemon chiffon', 4: 'pink1', 8: 'lightBlue1', 16: 'thistle2', 32: 'plum1', 64: 'aquamarine2',
          128: 'PaleTurquoise1', 256: 'salmon1', 512:'LightSteelBlue1', 1024: 'peach puff', 2048:'DarkOrchid2', 4096:'tomato',
          8192: 'pale green', 16384: 'thistle', 32768:'RosyBrown1', 65536: 'SeaGreen1'}
          
###board object has a value which is the numpy 
###backbone of the visual of the board
class board(object):
    def __init__(self):
        self.value = newBoard()
    
    ###moves all numbers up while combining like numbers 
    ###ex.two 2's next to each other with a nonzero number
    ###next to them will turn into a 4
    def up(self):
        value = self.value
        #checks if there was a shift in any of the #s of the board
        movedE = False
        #up justifies all non zero values first
        for j in range(len(value[0])):
            for i in range(len(value)):
                #if the value at the coordinate is not a 0, want to swap
                #this value with coordinates above them until a nonzero
                #value is encountered
                if value[i][j] != 0 and i != 0:
                    c = i
                    #the upper coordinate
                    u = i -1
                    zero = True
                    while u >= 0 and zero == True:
                        if value[u][j] == 0:
                            zero == True
                            temp = value[u][j]
                            value[u][j] = value[c][j]
                            value[c][j] = temp
                            u -= 1
                            c -= 1
                            movedE = True
                        else:
                            zero = False
        #add numbers that are the same together and shift rest of the board up
        for j in range(len(value[0])):
            for i in range(len(value)):
                if value[i][j] != 0 and i != len(value)-1:
                    d = i + 1
                    #checks to see if number below is the same as the current number
                    #if it is it adds them together, turns the second number into a 0
                    #and moves this to the end of the board and moves all the other numbers up
                    if value[i][j] == value[d][j]:
                        movedE = True
                        value[i][j] *= 2
                        value[d][j] = 0 
                        while d < len(value)-1:
                            n = d + 1
                            temp = value[d][j]
                            value[d][j] = value [n][j]
                            value[n][j] = temp
                            d += 1
        
        #randomly place a 2 or 4 on the board if a move was made that effects the board
        if movedE == True:
            index = random.choice(np.argwhere(np.array(value) == 0))
            pos = [2,4]
            value[index[0]][index[1]] = np.random.choice(pos, p=[0.9, 0.10])
        self.value = value
        return self
        
    ###moves all numbers down while combining like numbers 
    ###ex.two 2's next to each other with a nonzero number
    ###next to them will turn into a 4    
    def down(self):
        value = self.value
        #checks if there was a shift in any of the #s of the board
        movedE = False
        #down justifies all non zero values
        for j in range(len(value[0])):
            for i in range(len(value)):
                #if the value at the coordinate is not a 0, want to swap
                #this value with coordinates below them until a nonzero
                #value is encountered
                #adjusts i value so it starts at the bottom of the board
                I = len(value) - i - 1
                if value[I][j] != 0 and I != len(value)-1:
                    c = I 
                    d = I +1
                    zero = True
                    while d < len(value) and zero == True:
                        if value[d][j] == 0:
                            zero == True
                            temp = value[d][j]
                            value[d][j] = value[c][j]
                            value[c][j] = temp
                            d += 1
                            c += 1
                            movedE = True
                        else:
                            zero = False
        
        #add numbers that are the same together and shift rest of the board down
        for j in range(len(value[0])):
            for i in range(len(value)):
                I = len(value) - i - 1
                if value[I][j] != 0 and I != 0:
                    u = I - 1
                    #checks to see if number above is the same as the current number
                    #if it is it adds them together, turns the second number into a 0
                    #and moves this to the end of the board and moves all the other numbers down
                    if value[I][j] == value[u][j]:
                        movedE = True
                        value[I][j] *= 2
                        value[u][j] = 0 
                        while u > 0:
                            n = u - 1
                            temp = value[u][j]
                            value[u][j] = value [n][j]
                            value[n][j] = temp
                            u -= 1
        #randomly place a 2 or 4 on the board if a valid move was mad
        if movedE == True:
            index = random.choice(np.argwhere(np.array(value) == 0))
            pos = [2,4]
            value[index[0]][index[1]] = np.random.choice(pos, p=[0.9, 0.10])
        self.value = value
        return self
        
    ###moves all numbers left while combining like numbers 
    ###ex.two 2's next to each other with a nonzero number
    ###next to them will turn into a 4      
    def left(self):
        value = self.value
        #checks if there was a shift in any of the #s of the board
        movedE = False
        #left justifies all non zero values
        for i in range(len(value)):
            for j in range(len(value[0])):
                #if the value at the coordinate is not a 0, want to swap
                #this value with coordinates left of them until a nonzero
                #value is encountered
                if value[i][j] != 0 and j != 0:
                    c = j
                    l = j -1
                    zero = True
                    while l >= 0 and zero == True:
                        if value[i][l] == 0:
                            zero == True
                            temp = value[i][l]
                            value[i][l] = value[i][c]
                            value[i][c] = temp
                            l -= 1
                            c -= 1
                            movedE = True
                        else:
                            zero = False
        #add numbers that are the same together and shift rest of the board to the left
        for i in range(len(value)):
            for j in range(len(value[0])):
                if value[i][j] != 0 and j != len(value[0])-1:
                    r = j + 1
                    #checks to see if number to the right is the same as the current number
                    #if it is it adds them together, turns the second number into a 0
                    #and moves this to the end of the board and moves all the other numbers left
                    if value[i][j] == value[i][r]:
                        movedE = True
                        value[i][j] *= 2
                        value[i][r] = 0 
                        while r < len(value)-1:
                            n = r + 1
                            temp = value[i][r]
                            value[i][r] = value [i][n]
                            value[i][n] = temp
                            r += 1
        
        #randomly place a 2 or 4 on the board if a valid move was made
        if movedE == True:
            index = random.choice(np.argwhere(np.array(value) == 0))
            pos = [2,4]
            value[index[0]][index[1]] = np.random.choice(pos, p=[0.9, 0.10])
        self.value = value
        return self
        
        
    ###moves all numbers right while combining like numbers 
    ###ex.two 2's next to each other with a nonzero number
    ###next to them will turn into a 4     
    def right(self):
        value = self.value
        movedE = False
        #right justifies all non zero values
        for i in range(len(value)):
            for j in range(len(value[0])):
                #if the value at the coordinate is not a 0, want to swap
                #this value with coordinates right of them until a nonzero
                #value is encountered
                #adjusts j value so it starts at the right of the board
                J = len(value) - j - 1
                if value[i][J] != 0 and J != len(value[0])-1:
                    c = J
                    r = J + 1
                    zero = True
                    while r < len(value[0]) and zero == True:
                        if value[i][r] == 0:
                            zero == True
                            temp = value[i][r]
                            value[i][r] = value[i][c]
                            value[i][c] = temp
                            r += 1
                            c += 1
                            movedE = True
                        else:
                            zero = False
        
        #add numbers that are the same together and shift the rest of the board to the right
        for i in range(len(value)):
            for j in range(len(value[0])):
                J = len(value) - j - 1
                if value[i][J] != 0 and J != 0:
                    l = J - 1
                    #checks to see if number to the left is the same as the current number
                    #if it is it adds them together, turns the second number into a 0
                    #and moves this to the end of the board and moves all the other numbers right
                    if value[i][J] == value[i][l]:
                        movedE = True
                        value[i][J] *= 2
                        value[i][l] = 0 
                        while l > 0:
                            n = l - 1
                            temp = value[i][l]
                            value[i][l] = value [i][n]
                            value[i][n] = temp
                            l -= 1
        
        #randomly place a 2 or 4 on the board if a valid was moved
        if movedE == True:
            index = random.choice(np.argwhere(np.array(value) == 0))
            pos = [2,4]
            value[index[0]][index[1]] = np.random.choice(pos, p=[0.9, 0.10])
        self.value = value
        return self

    
 
###creates the starting board's numpy array
###returns a 4x4 numpy array with 2 values of 2 or 4       
def newBoard():
    b = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
    b = np.array(b)
    x = random.randint(0,3)
    y = random.randint(0,3)
    #places a random 2 in a random coordinate of the board
    b[x][y] = 2
    secVal = False
    #until a second value of 2 or 4 is placed keeps trying to 
    #place a 2 or 4 in a random coordinate of the board
    while secVal == False:
        x2 = random.randint(0,3)
        y2 = random.randint(0,3)
        if x2 != x or y2 != y:
            #probability of placing a 4 is 1/10 and a 2 is 9/10
            p = random.randint(1,10)
            if p == 10:
                b[x2][y2] = 4
            else:
                b[x2][y2] = 2
            secVal = True
    return b
     
    
###Creates interactive window
###allows moves to be made based on arrow keys
###configures the board to a new board after the move is made
###checks to see if the game is won
###checks to see if the game is over
def move(event, value):
    
    if value == "r":
        brd.right()
    elif value == "l":
        brd.left()
    elif value == "d":
        brd.down()
    elif value == "u":
        brd.up()
    for i in range(len(brd.value)):
        for j in range(len(brd.value)):
            #if 0 is the number, creates an empty square
            if (brd.value)[i][j] == 0:
                w.itemconfig(text_grid[i][j], text = "", font =" Helvetica 32 bold")
            else:
                #uses the numpy array to create numbers on the board
                w.itemconfig(text_grid[i][j], text = str((brd.value)[i][j]), font =" Helvetica 32 bold")
            #consults the color dictionary to fill in the right color for the number
            w.itemconfig(grid[i][j], fill = colors[(brd.value)[i][j]])
    #if there is a 2048, that means the player won, allows them to continue playing
    if 2048 in brd.value:
        w.create_text(300,170, text = "Congratulations you reached 2048. Keep playing! ", font = " Helvetica 16 bold")
    over = False 
    #if there are no empty squares, and if making all moves on the board doesn't change the board
    #which is checked by making a deepcopy of the board, than there are no more available moves
    #and the game is over
    if 0 not in brd.value:
        brd2 = deepcopy(brd)
        brd2.right()
        if np.array_equal(brd2.value, brd.value):
            brd2 = deepcopy(brd)
            brd2.left()
            if np.array_equal(brd2.value, brd.value):
                brd2 = deepcopy(brd)
                brd2.up()
                if np.array_equal(brd2.value, brd.value):
                    brd2 = deepcopy(brd)
                    brd2.down()
                    if np.array_equal(brd2.value, brd.value):
                        over = True
    if over == True:
        w.create_text(450,100, text = "Game over!", font = " Helvetica 32 bold")   

        
###MAIN: initiates a new board, connects the GUI to tkinter
###creates a canvas in which to alter tiles in 
###creates a 4x4 grid and fills it with numbers based on the board object's numpy array
brd = board()
root = Tk()
root.title("2048")
w = Canvas(root, 
           width=600, 
           height=800)
w.pack(expand = YES, fill = BOTH)
#creates title of the game
header = w.create_rectangle(0,0,600,200,fill = "Royalblue1")
title = w.create_text(160,100, text = "2048", font =" Helvetica 80 bold", fill = "black")
#creates the grid with the numbers in it
grid = [[w.create_rectangle(150*i, 200+150*j, 150*(i+1), 200+150*(j+1), fill="white", width =3, outline = 'gray') for i in range(4)] for j in range(4)]
text_grid = [[w.create_text(150*i + 75, 275 + 150*j, text= "",  font =" Helvetica 32 bold") for i in range(4)] for j in range(4)]  
#populates the grid with board's numpy values
for i in range(4):
    for j in range(4):
        if (brd.value)[i][j] == 0:
            w.itemconfig(text_grid[i][j], text = "")
        else:
            w.itemconfig(text_grid[i][j], text = str((brd.value)[i][j]))
        w.itemconfig(grid[i][j], fill = colors[(brd.value)[i][j]])

#binds the keyboard to the moves you can make       
root.bind("<Right>",lambda event: move(event, value ="r"))
root.bind("<Left>",lambda event: move(event, value ="l"))
root.bind("<Up>",lambda event: move(event, value ="u"))
root.bind("<Down>",lambda event: move(event, value ="d"))
 
root.mainloop()