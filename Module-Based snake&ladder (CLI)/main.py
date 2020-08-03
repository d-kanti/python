import src.extra_func as x
import src.app as app

class Player():
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
    
    def congrat(self):
         print(f"Congratulations {self.name}!! You win the game!")
   
p1 = Player(x.nam("Player 1"), 0)
p2 = Player(x.nam("Player 2"), 0)
mode = x.mode_select() 

app.play(p1,p2,mode)