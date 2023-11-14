#SEA BATTLE

#importing libraries 
from os import system
import time
import random
import sys

# # == hitted
# x == not any ship
# o == not touched place

#VARIABLES
list_of_hitted = []
stat = []

#Functions
def clear(x):
    time.sleep(x)
    system("cls")

def exit():
    sys.exit()

def info():
    clear(0)
    print("# == hitted\nx == not any ship\no == not touched place")
    print("Columns given in numbers.\nRows given in letters.\n")
    print("Enter '0' to get back to menu")
    if int(input()) == 0:
        menu()

def check(row, column, list):
    if list[row][column] == 1:
        return 1
    else:
        return 0
    
def statistics():
    clear(0)
    for i in range(len(stat)):
        print(stat[i][0], "     ", print(stat[i][1]))
    print("\nEnter '0' to get back to menu")
    if int(input()) == 0:
        menu()

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
def map0(map0):
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
    return map0
#second map
def map1(map1):
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
    return map1
#third map
def map2(map2):
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
    return map2
#fourth map
def map3(map3):
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
    return map3
#fifth map
def map4(map4):
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
    return map4
#sixth map
def map5(map5):
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
    return map5

#menu
def menu():
    clear(0)
    wh = input("1: Play\n2: Info\n3: Statistics\n4: Exit\n")
    if wh == "1":
        game()
    elif wh == "2":
        info()
    elif wh == "3":
        statistics()
    elif wh == "4":
        sys.exit()
    else:
        menu()

#game
def game():
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
    hitted = 0 
    moves = 0
    clear(0)
    
    name = input("Enter your name:\n")
    clear(3)

    while hitted != 11:
        print("Enter '0' to get back to menu")
        for i in range(7):
            print(*fieldplayer[i])
        #choosing column
        column = int(input("Enter the column\n"))
        column -= 1
        
        if column == -1:
            menu()
        
        #choosing row
        row = input("Enter the row\n")
        
        if row == "0":
            menu()
        
        # turning row into integer
        row = ord(row) - 97

        #add 1 to moves
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
    l = [name, moves]
    stat.append(l)
    print("Enter '0' to get back to menu")
    if int(input()) == 0:
        menu()

menu()
