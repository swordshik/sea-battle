#SEA BATTLE

#importing libraries 
from os import system
import time
import random

# # == hitted
# x == not any ship
# o == not touched place

#VARIABLES
hitted = 0
list_of_hitted = []
moves = 0

#Functions
def check(row, column, list):
    if list[row][column] == 1:
        return 1
    else:
        return 0
    
def clear(x):
    time.sleep(x)
    system("cls")

def change_for_hit(row, column, list):
    list[row][column] = "#"
    return list

def change_for_hit_for_game(row, column, list):
    list[row][column] = 0
    return list

def change_for_not_hit(x, y, list):
    list[x][y] = "x"
    return list

def sunk(row, column, list): 
    #for inside
    if (row > 0 and row < 6) and (column > 0 and column < 6):
        list[row+1][column+1] = "x"
        list[row-1][column-1] = "x"
        list[row+1][column-1] = "x"
        list[row-1][column+1] = "x"
        list[row][column+1] = "x"
        list[row][column-1] = "x"
        list[row+1][column] = "x"
        list[row-1][column] = "x"
    
    #for corners
    if row == 0 and column == 0:
        list[row+1][column+1] = "x"
        list[row][column+1] = "x"
        list[row+1][column] = "x"
    if row == 0 and column == 6:
        list[row+1][column-1] = "x"
        list[row][column-1] = "x"
        list[row+1][column] = "x"
    if row == 6 and column == 0:
        list[row-1][column+1] = "x"
        list[row-1][column] = "x"
        list[row][column+1] = "x"
    if row == 6 and column == 6:
        list[row-1][column-1] = "x"
        list[row-1][column] = "x"
        list[row][column-1] = "x"
    
    #for sides
    if (row == 0 and (column > 0 and column < 6)):
        list[row+1][column-1] = "x"
        list[row+1][column+1] = "x"
        list[row][column+1] = "x"
        list[row][column-1] = "x"
        list[row+1][column] = "x"
    if (row == 6 and (column > 0 and column < 6)):
        list[row-1][column-1] = "x"
        list[row-1][column+1] = "x"
        list[row][column+1] = "x"
        list[row][column-1] = "x"
        list[row-1][column] = "x"
    if (column == 0 and (row > 0 and row < 6)):
        list[row+1][column+1] = "x"
        list[row-1][column+1] = "x"
        list[row+1][column] = "x"
        list[row-1][column] = "x"
        list[row][column+1] = "x"
    if (column == 6 and (row > 0 and row < 6)):
        list[row+1][column-1] = "x"
        list[row-1][column-1] = "x"
        list[row-1][column] = "x"
        list[row+1][column] = "x"
        list[row][column-1] = "x"
    return list


def not_sunk(row, column, list):
    #for inside
    if (row > 0 and row < 6) and (column > 0 and column < 6):
        list[row+1][column+1] = "x"
        list[row-1][column-1] = "x"
        list[row+1][column-1] = "x"
        list[row-1][column+1] = "x"   
    
    #for corners
    if row == 0 and column == 0:
        list[row+1][column+1] = "x"
    if row == 0 and column == 6:
        list[row+1][column-1] = "x"
    if row == 6 and column == 0:
        list[row-1][column+1] = "x"
    if row == 6 and column == 6:
        list[row-1][column-1] = "x"
    
    #for sides
    if (row == 0 and (column > 0 and column < 6)):
        list[row+1][column-1] = "x"
        list[row+1][column+1] = "x"
    if (row == 6 and (column > 0 and column < 6)):
        list[row-1][column-1] = "x"
        list[row-1][column+1] = "x"
    if (column == 0 and (row > 0 and row < 6)):
        list[row+1][column+1] = "x"
        list[row-1][column+1] = "x"
    if (column == 6 and (row > 0 and row < 6)):
        list[row+1][column-1] = "x"
        list[row-1][column-1] = "x"
    return list



def checknear(row, column, list):
    #for inside
    if (row > 0 and row < 6) and (column > 0 and column < 6):
        if list[row+1][column] == 1:
            return 1
        if list[row-1][column] == 1:
            return 1
        if list[row][column+1] == 1:
            return 1
        if list[row][column-1] == 1:
            return 1
        else:
            return 0
    
    #for corners
    if (row == 0 and column == 0):
        if list[row+1][column] == 1:
            return 1
        if list[row][column+1] == 1:
            return 1
        else:
            return 0
    if (row == 0 and column == 6):
        if list[row+1][column] == 1:
            return 1
        if list[row][column-1] == 1:
            return 1
        else:
            return 0
    if (row == 6 and column == 0):
        if list[row-1][column] == 1:
            return 1
        if list[row][column+1] == 1:
            return 1
        else:
            return 0
    if (row == 6 and column == 6):
        if list[row-1][column] == 1:
            return 1
        if list[row][column-1] == 1:
            return 1
        else:
            return 0

    #for sides
    if (row == 0 and (column > 0 and column < 6)):
        if list[row+1][column] == 1:
            return 1
        else:
            return 0
    if (row == 6 and (column > 0 and column < 6)):
        if list[row-1][column] == 1:
            return 1
        else:
            return 0
    if (column == 0 and (row > 0 and row < 6)):
        if list[row+1][column] == 1:
            return 1
        else:
            return 0
    if (column == 6 and (row > 0 and row < 6)):
        if list[row-1][column] == 1:
            return 1
        else:
            return 0
    
#it will be hard to make for each game different location for ships
#so i define 6 map, and for every game there will be randompicked map

#LIBRARY OF MAPS
#first map
linesmap00 = [0]
linesmap00 = linesmap00*7
linesmap01 = [0]
linesmap01 = linesmap01*7
linesmap02 = [0]
linesmap02 = linesmap02*7
linesmap03 = [0]
linesmap03 = linesmap03*7
linesmap04 = [0]
linesmap04 = linesmap04*7
linesmap05 = [0]
linesmap05 = linesmap05*7
linesmap06 = [0]
linesmap06 = linesmap06*7
map0 = [linesmap00, linesmap01, linesmap02, linesmap03, linesmap04, linesmap05, linesmap06]
map0[0][0] = 1
map0[0][6] = 1
map0[1][2] = 1
map0[1][4] = 1
map0[2][2] = 1
map0[2][4] = 1
map0[4][2] = 1
map0[4][3] = 1
map0[4][4] = 1
map0[6][0] = 1
map0[6][6] = 1

#second map
linesmap10 = [0]
linesmap10 = linesmap10*7
linesmap11 = [0]
linesmap11 = linesmap11*7
linesmap12 = [0]
linesmap12 = linesmap12*7
linesmap13 = [0]
linesmap13 = linesmap13*7
linesmap14 = [0]
linesmap14 = linesmap14*7
linesmap15 = [0]
linesmap15 = linesmap15*7
linesmap16 = [0]
linesmap16 = linesmap16*7
map1 = [linesmap10, linesmap11, linesmap12, linesmap13, linesmap14, linesmap15, linesmap16]
map1[0][1] = 1
map1[0][5] = 1
map1[1][1] = 1
map1[1][5] = 1
map1[3][0] = 1
map1[3][2] = 1
map1[3][4] = 1
map1[3][6] = 1
map1[6][2] = 1
map1[6][3] = 1
map1[6][4] = 1

#third map
linesmap20 = [0]
linesmap20 = linesmap20*7
linesmap21 = [0]
linesmap21 = linesmap21*7
linesmap22 = [0]
linesmap22 = linesmap22*7
linesmap23 = [0]
linesmap23 = linesmap23*7
linesmap24 = [0]
linesmap24 = linesmap24*7
linesmap25 = [0]
linesmap25 = linesmap25*7
linesmap26 = [0]
linesmap26 = linesmap26*7
map2 = [linesmap20, linesmap21, linesmap22, linesmap23, linesmap24, linesmap25, linesmap26]
map2[0][0] = 1
map2[1][4] = 1
map2[2][4] = 1
map2[2][0] = 1
map2[3][0] = 1
map2[2][2] = 1
map2[4][4] = 1
map2[5][0] = 1
map2[5][1] = 1
map2[5][2] = 1
map2[6][6] = 1

#fourth map
linesmap30 = [0]
linesmap30 = linesmap30*7
linesmap31 = [0]
linesmap31 = linesmap31*7
linesmap32 = [0]
linesmap32 = linesmap32*7
linesmap33 = [0]
linesmap33 = linesmap33*7
linesmap34 = [0]
linesmap34 = linesmap34*7
linesmap35 = [0]
linesmap35 = linesmap35*7
linesmap36 = [0]
linesmap36 = linesmap36*7
map3 = [linesmap30, linesmap31, linesmap32, linesmap33, linesmap34, linesmap35, linesmap36]
map3[0][6] = 1
map3[1][1] = 1
map3[2][1] = 1
map3[2][4] = 1
map3[2][6] = 1
map3[3][6] = 1
map3[4][2] = 1
map3[5][4] = 1
map3[5][5] = 1
map3[5][6] = 1
map3[6][0] = 1

#fifth map
linesmap40 = [0]
linesmap40 = linesmap40*7
linesmap41 = [0]
linesmap41 = linesmap41*7
linesmap42 = [0]
linesmap42 = linesmap42*7
linesmap43 = [0]
linesmap43 = linesmap43*7
linesmap44 = [0]
linesmap44 = linesmap44*7
linesmap45 = [0]
linesmap45 = linesmap45*7
linesmap46 = [0]
linesmap46 = linesmap46*7
map4 = [linesmap40, linesmap41, linesmap42, linesmap43, linesmap44, linesmap45, linesmap46]
map4[2][2] = 1
map4[2][4] = 1
map4[4][2] = 1
map4[4][4] = 1
map4[5][0] = 1
map4[6][0] = 1
map4[5][6] = 1
map4[6][6] = 1
map4[6][2] = 1
map4[6][3] = 1
map4[6][4] = 1

#sixth map
linesmap50 = [0]
linesmap50 = linesmap50*7
linesmap51 = [0]
linesmap51 = linesmap51*7
linesmap52 = [0]
linesmap52 = linesmap52*7
linesmap53 = [0]
linesmap53 = linesmap53*7
linesmap54 = [0]
linesmap54 = linesmap54*7
linesmap55 = [0]
linesmap55 = linesmap55*7
linesmap56 = [0]
linesmap56 = linesmap56*7
map5 = [linesmap50, linesmap51, linesmap52, linesmap53, linesmap54, linesmap55, linesmap56]
map5[0][0] = 1
map5[0][6] = 1
map5[1][2] = 1
map5[1][4] = 1
map5[3][1] = 1
map5[3][2] = 1
map5[3][4] = 1
map5[3][5] = 1
map5[5][2] = 1
map5[5][3] = 1
map5[5][4] = 1

#field to communicate with player
linesplayer0 = ["o"]
linesplayer0 = linesplayer0*7
linesplayer1 = ["o"]
linesplayer1 = linesplayer1*7
linesplayer2 = ["o"]
linesplayer2 = linesplayer2*7
linesplayer3 = ["o"]
linesplayer3 = linesplayer3*7
linesplayer4 = ["o"]
linesplayer4 = linesplayer4*7
linesplayer5 = ["o"]
linesplayer5 = linesplayer5*7
linesplayer6 = ["o"]
linesplayer6 = linesplayer6*7
fieldplayer = [linesplayer0, linesplayer1, linesplayer2, linesplayer3, linesplayer4, linesplayer5, linesplayer6]

#choosing map
linesfield0 = [0]
linesfield0 = linesfield0*7
linesfield1 = [0]
linesfield1 = linesfield1*7
linesfield2 = [0]
linesfield2 = linesfield2*7
linesfield3 = [0]
linesfield3 = linesfield3*7
linesfield4 = [0]
linesfield4 = linesfield4*7
linesfield5 = [0]
linesfield5 = linesfield5*7
linesfield6 = [0]
linesfield6 = linesfield6*7
field = [linesfield0, linesfield1, linesfield2, linesfield3, linesfield4, linesfield5, linesfield6]
rand = random.randrange(0, 7)
if rand == 0:
    field = map0(field)
if rand == 1:
    field = map1(field)
if rand == 2:
    field = map2(field)
if rand == 3:
    field = map3(field)
if rand == 4:
    field = map4(field)
if rand == 5:
    field = map5(field)
clear(0)

name = input("Enter your name:\n")
clear(5)

#game
while hitted != 11:
    for i in range(7):
        print(*fieldplayer[i])

    column = int(input("Enter the column\n"))
    column -= 1

    row = input("Enter the row\n")
    row = ord(row) - 97
    moves += 1
    small_list_of_hitted = [row, column]
    clear(0)

    if (small_list_of_hitted in list_of_hitted):
        print("You've already shooted here.")
    
    elif row>6 or column>6:
        print("You shooted out of map.")

    else:
        list_of_hitted.append(small_list_of_hitted)

        #when player did not hit
        if check(row, column, field) == 0:
            clear(0)
        
            print("You did not hit")
            clear(3)

            fieldplayer = change_for_not_hit(row, column, fieldplayer)
    
        #when player hitted
        if check(row, column, field) == 1:
        
            hitted += 1
            field = change_for_hit_for_game(row, column, field)

            fieldplayer = change_for_hit(row, column, fieldplayer)


            #for sunk
            if checknear(row, column, field) == 0:
                clear(0)
            
                print("Hit and sunk")
                clear(3)

                fieldplayer = sunk(row, column, fieldplayer)

        
            #for not sunk
            if checknear(row, column, field) == 1:
                clear(0)
            
                print("Hitted")
                clear(3)

                fieldplayer = not_sunk(row, column, fieldplayer)

print("Congratulations, you won the game!")
print("Player:", name, "\nMoves:", moves)
