import src.board_info as snl
import src.player_turn as pt







def play(p1,p2,mode):
    print("############start##########")
    status = 0
    p1_win = False
    p2_win = False
    while not p1_win and not p2_win:
        if status == 0:
            (p1,p2_win,p1_win,status) = pt.turn_p1(mode,snl,p1,p2_win,p1_win,status)
            if p1_win :
                p1.congrat()
                break
            elif p2_win :
                p2.congrat()
                break
            else:
                continue
        elif status == 1:
            (p2,p1_win,p2_win,status) = pt.turn_p2(mode,snl,p2,p1_win,p2_win,status)
            if p1_win :
                p1.congrat()
                break
            elif p2_win :
                p2.congrat()
                break
            else:
                continue