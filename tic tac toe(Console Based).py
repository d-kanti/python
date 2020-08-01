
            #----------------------------------------defining functions-----------------------------------------

#s---------------------show board--------87------>
def disp(board):
    #clear the previous output----
    print("\n"*10)
    
    
    i = 1
    for _ in range(3):
        for j in range(2):
            print(" ",board[i+j],"  | ",end="")
        print(" ",board[i+2])
        if i<6:
            print("="*22)
        i+=3


#--------------------------------initial function to assign 'x' or 'o' to player 1-------------
def initial():
    while True:
        try:
            temp_inp = input("Player 1 would like to choose (X or O): ") 
            if temp_inp.lower() == "x" or temp_inp.lower() == "o":
                break
            else:
                print("invalid input!! Try again.......")
        except:
            print("invalid input!! Try again.........")
    if temp_inp.lower() == "x":
        return ("X","O")
    else:
        return ("O","X")

#--------------check if won----------------
def check_win(pw, board):
    win = False
    for i in [1,4,7]:
        if board[i]==board[i+1]==board[i+2]:
            win = board[i]
    for i in [1,2,3]:
        if board[i]==board[i+3]==board[i+6]:
            win = board[i]
    if board[1]==board[5]==board[9] or board[3]==board[5]==board[7]:
        win = board[5]
    
    if win:
        print("\n"*2)
        print("========================== Game Over ===================")
        print("{} won the game...".format(pw[win]))
        print("\n"*4)
        
    return win






# initializing the board
board  = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}


(a,b) = initial()
players = {'Player 1' : a, 'Player 2' : b}
pw = {a:'Player 1',b:'Player 2'}

won = False
disp(board)
count = 0
while not won:
    for i in players:
        
        place = int(input("turn for {} (1~9): ".format(i)))
        board[place] = players[i]
        disp(board)
        count += 1
        won = check_win(pw,board)
        if won:
            break
        elif count == 9:
            won = True
            print("========================== Game Draw ===================")
            print("\n"*4)
            break
        else:
            continue
