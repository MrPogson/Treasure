#import libraries
import random
import time

#Define global variables
global Pos
global grid
global grid2
global score

#set score to 0
score = 0
#set starting position to 30
Pos=30

#Main function 
def main():
    global grid #make the variable 'grid' available
    global grid2#make the variable 'grid2' available
    play =input("\nDo you want to 'Play' or 'Quit'? ").upper() #Ask if they want to play
    if play == "PLAY": #if they choose to play
        grid =["W","W","W","W","O","O","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]#set up the grid 
        random.shuffle(grid)#randomise the positions
        grid2=["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X",]#set up the blank grid
        grid2.insert(Pos,"P")#put a P in the bottom left corner
        movement()#go to function 'movement'
        
    elif play == "QUIT":#if they choose quit
        game_over()#go to function
    else:#of they put anything else in
        print("Error - Please choose 'Play' or 'Quit'")#tell them to try again
        main()#go to function

def print_grid_2():#grid with game elements, hidden by default
    global grid
    print("\n")
    matrix=[grid [i:i+6]for i in range (0,len(grid),6)]
    for a,b,c,d,e,f in matrix:
        print (a,b,c,d,e,f)    

def print_grid():# - grid of X's
    global grid2
    print("\n")
    matrix2=[grid2 [j:j+6]for j in range (0,len(grid2),6)]
    for a,b,c,d,e,f in matrix2:
        print (a,b,c,d,e,f)

def movement():
    global grid
    global grid2
    global Pos

    print_grid()
    #print_grid_2()  #uncomment to show position of game elements
                     
    move=input("\nDo you want to go 'Up', 'Down', 'Left' or 'Right'?\n")
    move=move.upper()
                     
    if move == ("UP"):
        qty = int(input("\nHow far up?\n")) 
        old_p=Pos
        Pos=Pos+((qty)*-6)
        if qty == 0:
            print("\nPlease choose a number between 1-6!")
            Pos=old_p
            movement()
        if Pos <0:
            print ("\nThat's too far up! You've gone off the board!\nTry again!")
            Pos=old_p
            movement()
        print("\n#####################\nnew Position =",Pos)
        check_score()
        grid2[Pos] = "P"
        grid2[old_p]="-"

    elif move == ("DOWN"):
        qty = int(input("\nHow far down?\n"))
        old_p=Pos
        Pos=Pos+((qty)*6)
        if qty == 0:
            print("\nPlease choose a number between 1-6!")
            Pos=old_p
            movement()
        if Pos >35:
            print ("\nThat's too far up! You've gone off the board!\nTry again!")
            Pos=old_p
            movement()
        print("\nnew Position =",Pos)
        check_score()
        grid2[Pos] = "P"
        grid2[old_p]="-"

    elif move == ("RIGHT"):
        qty = int(input("\nHow far right?\n"))
        old_p=Pos
        Pos=Pos+(qty)
        if qty == 0:
            print("\nPlease choose a number between 1-6!")
            Pos=old_p
            movement()
        print("\n#########################\nnew Position =",Pos)
        check_score()
        grid2[Pos] = "P"
        grid2[old_p]="-"

    elif move == ("LEFT"):
        qty = int(input("\nHow far left?\n"))
        old_p=Pos
        Pos=Pos-(qty)
        if qty == 0:
            print("\nPlease choose a number between 1-6!")
            Pos=old_p
            movement()
        print("\n########################\nnew Position =",Pos)
        check_score()
        grid2[Pos] = "P"
        grid2[old_p]="-"

    else:
        print ("choose 'Up', 'Down', 'Left' or 'Right'")
        
    movement()
    
def check_score():
    global Pos
    global score
    global grid
    
    if (grid[Pos])not in ["W","O"]:
        print("\nMiss!\n")
        print ("Score = ",score,"\n####################")

    elif (grid[Pos])=="W":
        print("\nYou found A Wally!! 100 points!\n")
        score=score+100
        print ("Score = ",score,"\n################################")
        grid[Pos]="X"

    if (grid[Pos])=="O":
        print("\nYou hit Oddlaw! You lose!\n")
        score=0
        print ("Score = ",score,"\n################################")

def game_over():
    print ("##############\nGame Over!\nThank you for playing!\n#############\n")
    time.sleep(5)
    exit()
print ("Welcome!")
main()
