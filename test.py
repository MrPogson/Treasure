print(" This is my Introduction \n Welcome to My game! \n It's a really good game!")

#Main function 
def main():

    play =input("\nDo you want to 'Play' or 'Quit'? \n").upper() #Ask if they want to play
    if play == "PLAY": #if they choose to play
        playgame()#go to function 'playgame'
        
    elif play == "QUIT":#if they choose quit
        game_over()#go to function 'Game over'

        
    else:#or they put anything else in
        print("Error - Please type 'Play' or 'Quit'\n")#tell them to try again
        main()#go back to top of function


def playgame():#THIS IS A FUNCTION
    print("this is where the code will go to play the game")

def game_over():
    print("this is where the code will go to end the game")

def set_up_grid_a():
    print("this is where we set up the shown grid")
    
def set_up_grid_b():
    print("this is where we set up the secret grid")
    
def move():
    print("this is where we move")
    
def score():
    print("this is where we check the score")
    

main()#TELLS IT TO GO TO FUNCTION, IT WON'T RUN WITHOUT THIS!
