#turn for player 1 -------------------
import random
def turn_p1(mode,snl,p1,p2_win,p1_win,status):

    if mode == 'auto':
        user_input = input("Player 1:")
        if user_input == 'roll':
            dice = random.randint(1,6)
            status = 1
            if p1.pos+dice > snl.final_score:
                print("input not allowed")
            else:
                p1.pos += dice            
            if p1.pos in snl.ladders:
                print(" Climbed a ladder  |+|+|+|+|+|+|")
                p1.pos = snl.ladders[p1.pos]
            elif p1.pos in snl.snakes:
                print(" Encountered a snake  >:~`~`~`~`~`~")
                p1.pos = snl.snakes[p1.pos]
            print(" {} 's final position is {}".format(p1.name,p1.pos))                    
            if p1.pos == snl.final_score:
               p1_win = True            
        elif user_input == 'quit':
            print("player 1 quited")
            p2_win = True        
        else:
            print("Invalid input !!  Try again....")        
    elif mode == 'manual':
        user_input = input("Player 1 (1~20):")
        try:
            dice = int(user_input)
            if dice>0 and dice<21:
                status = 1
                if p1.pos+dice > snl.final_score:
                    print("input not allowed")
                else:
                    p1.pos += dice
 
                if p1.pos in snl.ladders:
                    print(" Climbed a ladder  |+|+|+|+|+|+|")
                    p1.pos = snl.ladders[p1.pos]
                elif p1.pos in snl.snakes:
                    print(" Encountered a snake  >:~`~`~`~`~`~")
                    p1.pos = snl.snakes[p1.pos]
                print(" {} 's final position is {}".format(p1.name,p1.pos))
                if p1.pos == snl.final_score:
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
    return (p1,p2_win,p1_win,status)







#turn for player 2----------------------
def turn_p2(mode, snl,p2,p1_win,p2_win,status):

    if mode == 'auto':
        user_input = input("Player 2:")
        if user_input == 'roll':
            dice = random.randint(1,6)
            status = 0
            if p2.pos+dice > snl.final_score:
                print("input not allowed")
            else:
                p2.pos += dice            
            if p2.pos in snl.ladders:
                print(" Climbed a ladder  |+|+|+|+|+|+|")
                p2.pos = snl.ladders[p2.pos]
            elif p2.pos in snl.snakes:
                print(" Encountered a snake  >:~`~`~`~`~`~")
                p2.pos = snl.snakes[p2.pos]
            print(" {} 's final position is {}".format(p2.name,p2.pos))
            if p2.pos == snl.final_score:
                p2_win = True            
        elif user_input == 'quit':
            print("player 2 quited")
            p1_win = True       
        else:
            print("Invalid input !!  Try again....")        
    elif mode == 'manual':
        user_input = input("Player 2 (1~20):")
        try:
            dice = int(user_input)
            if dice>0 and dice<21:
                status = 0
                if p2.pos+dice > snl.final_score:
                    print("input not allowed")
                else:
                    p2.pos += dice
                if p2.pos in snl.ladders:
                    print(" Climbed a ladder  |+|+|+|+|+|+|")
                    p2.pos = snl.ladders[p2.pos]
                elif p2.pos in snl.snakes:
                    print(" Encountered a snake  >:~`~`~`~`~`~")
                    p2.pos = snl.snakes[p2.pos]
                print(" {} 's final position is {}".format(p2.name,p2.pos))
                if p2.pos == snl.final_score:
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

    return (p2,p1_win,p2_win,status)