import random
ladders = { 
    3:38,
    24:33,
    42:93,
    72: 84
    }
snakes = { 
    17:7,
    54:34,
    62:19,
    98:79
    }

final_score = 100

class Player:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
    
name_temp = input("Enter the name of the Player 1 :  ")
p1 = Player(name_temp, 0)
name_temp = input("Enter the name of the Player 2 :  ")
p2 = Player(name_temp, 0)

mode = ""
while(not mode):
    temp = input("Please enter the Mode of the Game: ")
    if temp == 'auto' or temp == 'manual':
        mode = temp
    else:
        print("Invalid Input !!")
        continue

def turn_p2(mode, ladders, snakes,final_score):
    global p2
    global p1_win
    global p2_win
    global status
    if mode == 'auto':
        user_input = input("Player 2:")
        if user_input == 'roll':
            dice = random.randint(1,6)
            status = 0
            if p2.pos+dice > final_score:
                print("input not allowed")
            else:
                p2.pos += dice            
            if p2.pos in ladders:
                print(" Climbed a ladder  |+|+|+|+|+|+|")
                p2.pos = ladders[p2.pos]
            elif p2.pos in snakes:
                print(" Encountered a snake  >:~`~`~`~`~`~")
                p2.pos = snakes[p2.pos]
            print(" {} 's final position is {}".format(p2.name,p2.pos))
            if p2.pos == final_score:
                p2_win = True            
        elif user_input == 'quit':
            print("player 2 quited")
            p1_win = True       
        else:
            print("Invalid input !!  Try again....")        
    elif mode == 'manual':
        user_input = input("Player 2:")
        try:
            dice = int(user_input)
            if dice>0 and dice<21:
                status = 0
                if p2.pos+dice > final_score:
                    print("input not allowed")
                else:
                    p2.pos += dice
                if p2.pos in ladders:
                    print(" Climbed a ladder  |+|+|+|+|+|+|")
                    p2.pos = ladders[p2.pos]
                elif p2.pos in snakes:
                    print(" Encountered a snake  >:~`~`~`~`~`~")
                    p2.pos = snakes[p2.pos]
                print(" {} 's final position is {}".format(p2.name,p2.pos))
                if p2.pos == final_score:
                    p2_win = True                
            else:
                print("Input invalid")
                        
        except:
            if user_input == 'quit':
                print("player 1 quited")
                p1_win = True        
            else:
                print("Invalid input !!  Try again....")
    else:
        print("something went wrong !!")

def turn_p1(mode, ladders, snakes,final_score):
    global p1
    global p2_win
    global p1_win
    global status
    if mode == 'auto':
        user_input = input("Player 1:")
        if user_input == 'roll':
            dice = random.randint(1,6)
            status = 1
            if p1.pos+dice > final_score:
                print("input not allowed")
            else:
                p1.pos += dice            
            if p1.pos in ladders:
                print(" Climbed a ladder  |+|+|+|+|+|+|")
                p1.pos = ladders[p1.pos]
            elif p1.pos in snakes:
                print(" Encountered a snake  >:~`~`~`~`~`~")
                p1.pos = snakes[p1.pos]
            print(" {} 's final position is {}".format(p1.name,p1.pos))                    
            if p1.pos == final_score:
               p1_win = True            
        elif user_input == 'quit':
            print("player 1 quited")
            p2_win = True        
        else:
            print("Invalid input !!  Try again....")        
    elif mode == 'manual':
        user_input = input("Player 1:")
        try:
            dice = int(user_input)
            if dice>0 and dice<21:
                status = 1
                if p1.pos+dice > final_score:
                    print("input not allowed")
                else:
                    p1.pos += dice

                if p1.pos in ladders:
                    print(" Climbed a ladder  |+|+|+|+|+|+|")
                    p1.pos = ladders[p1.pos]
                elif p1.pos in snakes:
                    print(" Encountered a snake  >:~`~`~`~`~`~")
                    p1.pos = snakes[p1.pos]
                print(" {} 's final position is {}".format(p1.name,p1.pos))
                if p1.pos == final_score:
                    p1_win =  True                
            else:
                print("Input invalid")            
        except:
            if user_input == 'quit':
                print("player 1 quited")
                p2_win = True        
            else:
                print("Invalid input !!  Try again....")       
    else:
        print("something went wrong !!")

##############################################
print("############start##########")
status = 0
p1_win = False
p2_win = False
while not p1_win and not p2_win:
    if status == 0:
        turn_p1(mode,ladders,snakes,final_score)
        if p1_win :
            print("Congratulations {}!! You win the game!".format(p1.name))
            break
        elif p2_win :
            print("Congratulations {}!! You win the game!".format(p2.name))
            break
        else:
            continue
    elif status == 1:
        turn_p2(mode,ladders,snakes,final_score)
        if p1_win :
            print("Congratulations {}!! You win the game!".format(p1.name))
            break
        elif p2_win :
            print("Congratulations {}!! You win the game!".format(p2.name))
            break
        else:
            continue