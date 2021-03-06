
def evaluation(board,mykomadai,okomadai,mv,turn=""):
    pawn = 100
    lance = 300
    knight = 300
    silver = 400
    gold = 500
    rook = 800
    bishop = 700
    king = 9999
    score_cp = 0;
    y = 0;
    for bline in board:
        x = 0;
        for square in bline:
            if square=="K":
                score_cp += king
            if square=="k":
                score_cp -= king
            if square=="P":
                score_cp += pawn
            if square=="p":
                score_cp -= pawn
            if square=="L":
                score_cp += lance
            if square=="l":
                score_cp -= lance
            if square=="N":
                score_cp += knight
            if square=="n":
                score_cp -= knight
            if square=="S":
                score_cp += silver
            if square=="s":
                score_cp -= silver
            if square=="G" or square=="+L" or square=="+N" or square=="+P" or square=="+S" :
                score_cp += gold
            if square=="g" or square=="+l" or square=="+n" or square=="+p" or square=="+s":
                score_cp -= gold
            if square=="R":
                score_cp += rook
                c = 0
                for ix in reversed(range(x)):
                    #print("y: {}, len(board): {}, ix: {}, x: {}".format(y,len(board),ix,x))
                    if board[y][ix]=="":
                        c += 1
                    elif board[y][ix].isupper():
                        break
                    else:
                        c += 1
                        break
                for ix in range(x+1,9):
                    if board[y][ix]=="":
                        c += 1
                    elif board[y][ix].isupper():
                        break
                    else:
                        c += 1
                        break
                for iy in reversed(range(y)):
                    if board[iy][x]=="":
                        c += 1
                    elif board[iy][x].isupper():
                        break
                    else:
                        c += 1
                        break
                for iy in range(y+1,9):
                    if board[iy][x]=="":
                        c += 1
                    elif board[iy][x].isupper():
                        break
                    else:
                        c += 1
                        break
                score_cp += c*9

            if square=="r":
                score_cp -= rook
            if square=="B":
                score_cp += bishop
            if square=="b":
                score_cp -= bishop
            if square=="+R":
                score_cp += rook + silver
                c = 0
                for ix in reversed(range(x)):
                    if board[y][ix]=="":
                        c += 1
                    elif board[y][ix].isupper():
                        break
                    else:
                        c += 1
                        break
                for ix in range(x+1,9):
                    if board[y][ix]=="":
                        c += 1
                    elif board[y][ix].isupper():
                        break
                    else:
                        c += 1
                        break
                for iy in reversed(range(y)):
                    if board[iy][x]=="":
                        c += 1
                    elif board[iy][x].isupper():
                        break
                    else:
                        c += 1
                        break
                for iy in range(y+1,9):
                    if board[iy][x]=="":
                        c += 1
                    elif board[iy][x].isupper():
                        break
                    else:
                        c += 1
                        break
                score_cp += c*9
            if square=="+r":
                score_cp -= rook + silver
            if square=="+B":
                score_cp += bishop + gold
            if square=="+b":
                score_cp -= bishop + gold
            x += 1
        y += 1

    for p in mykomadai:
            if square=="k":
                score_cp += king
            if square=="p":
                score_cp += pawn
            if square=="l":
                score_cp += lance
            if square=="n":
                score_cp += knight
            if square=="s":
                score_cp += silver
            if square=="g" or square=="+l" or square=="+n" or square=="+p" or square=="+s":
                score_cp += gold
            if square=="r":
                score_cp += rook
            if square=="b":
                score_cp += bishop
    for p in okomadai:
            if square=="k":
                score_cp -= king
            if square=="p":
                score_cp -= pawn
            if square=="l":
                score_cp -= lance
            if square=="n":
                score_cp -= knight
            if square=="s":
                score_cp -= silver
            if square=="g" or square=="+l" or square=="+n" or square=="+p" or square=="+s":
                score_cp -= gold
            if square=="r":
                score_cp -= rook
            if square=="b":
                score_cp -= bishop
        
    if turn == "opponent":
        score_cp -= 50
    elif turn == "me":
        score_cp += 50

    return score_cp

def getokomadai(board,mykomadai):
    klist = ["p"]*18+["l"]*4+["n"]*4+["s"]*4+["g"]*4+["k","K"]+["r"]*2+["b"]*2
    for bline in board:
        for sq in bline:
          if sq!="":
            klist.remove(sq[-1])
    for p in mykomadai:
        klist.remove(p)

    return klist

