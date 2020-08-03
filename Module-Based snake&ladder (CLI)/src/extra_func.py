def nam(s):
    return input(f"Enter the name of the {s} :  ")

# defining a mode of the game, 
# 'auto' mode means randomly
# a number of moves will be made. 
# 'manual' mode means the input will be provided 
# by the player (<=20)

def mode_select():
    mode = ""

    while(not mode):
        temp = input("Please enter the Mode of the Game (manual or auto): ").lower()
        if temp == 'auto' or temp == 'manual':
            mode = temp
        else:
            print("Invalid Input !!")
            continue
    
    return mode