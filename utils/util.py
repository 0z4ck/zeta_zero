import random


def createRandomBoard():
    pieces = ["p"]*18+["l"]*4+["n"]*4+["s"]*4+["g"]*4+["k","K"]+["r"]*2+["b"]*2
    freeplace = range(81)
    board = [["" for i in xrange(9)] for j in xrange(9)]
    for p in pieces:
        if p == "g":
            piece = random.choice([p.upper(),p])
        elif p=="k" or p=="K":
            piece = p
        else:
            piece = random.choice([p.upper(),p,"+"+p.upper(),"+"+p])
        
        pl = random.choice(freeplace)
        freeplace.remove(pl)
        filen = pl%9
        linen = pl/9
        board[linen][filen] = piece

    return board

def randTurn():
    return random.choice(["gote","sente"])


def prettifier(board):

    for bline in board:
        print(list(reversed(["  " if i==""  else i+" " if len(i)==1 else i for i in bline ])))

def rawtousi(p, x1, x2, y1, y2, sente=True):
    sfeny = ["a","b","c","d","e","f","g","h","i"]
    if sente:
        #print("p:{}, x1:{}, x2:{}, y1]{}, y2:{}".format(p, x1, x2, y1, y2))
        usimove = "{}{}{}{}".format(x1+1,sfeny[y1],x2+1,sfeny[y2])
    else:
        usimove = "{}{}{}{}".format(9-x1,sfeny[8-y1],9-x2,sfeny[8-y2]) 
    return usimove

def isCheck(board):
    turn = "gote" # temporary
    ischck = False
    if turn == "gote":
        for linen in range(9):
             if "K" in board[linen]:
                 kfilen = board[linen].index("K")
                 klinen = linen
                 break
        if klinen > 1 :
            #check knight's check
            if kfilen == 8:
                if board[klinen-2][kfilen-1] == "n":
                    ischck = True
                    print("knight is checking to sente")
            elif kfilen == 0:
                if board[klinen-2][kfilen+1] == "n":
                    ischck = True
                    print("knight is checking to sente")
            else:
                if board[klinen-2][kfilen-1] == "n" or board[klinen-2][kfilen+1] == "n":
                    ischck = True
                    print("knight is checking to sente")
        if klinen != 0 :
            #check king's front check
            if board[klinen-1][kfilen] in ["p","l","s","g","k","r","+p","+l","+n","+s","+b","+r"]:
                ischck = True
                print("{} is checking to sente from the front".format(board[klinen-1][kfilen]))
            if kfilen == 8:
                if board[klinen-1][kfilen-1] in ["s","g","k","b","+p","+l","+n","+s","+b","+r"]:
                    ischck = True
                    print("{} is checking to sente from the front right".format(board[klinen-1][kfilen-1]))
            elif kfilen == 0:
                if board[klinen-1][kfilen+1] in ["s","g","k","b","+p","+l","+n","+s","+b","+r"]:
                    ischck = True
                    print("{} is checking to sente from the front left".format(board[klinen-1][kfilen+1]))
            else:
                if board[klinen-1][kfilen-1] in ["s","g","k","b","+p","+l","+n","+s","+b","+r"]:
                    ischck = True
                    print("{} is checking to sente from the front right".format(board[klinen-1][kfilen-1]))
                if board[klinen-1][kfilen+1] in ["s","g","k","b","+p","+l","+n","+s","+b","+r"]:
                    ischck = True
                    print("{} is checking to sente from the front left".format(board[klinen-1][kfilen+1]))

        if kfilen != 0:
            #check king's right side
            if board[klinen][kfilen-1] in ["g","k","r","+p","+l","+n","+s","+b","+r"]:
                ischck = True
                print("{} is checking to sente from the right".format(board[klinen][kfilen-1]))
        if kfilen != 8:
            #check king's left side
            if board[klinen][kfilen+1] in ["g","k","r","+p","+l","+n","+s","+b","+r"]:
                ischck = True
                print("{} is checking to sente from the left".format(board[klinen][kfilen+1]))
        if klinen != 8:
            #check king's back
            if board[klinen+1][kfilen] in ["g","k","r","+p","+l","+n","+s","+b","+r"]:
                ischck = True
                print("{} is checking to sente from the back".format(board[klinen+1][kfilen]))
            if kfilen == 8:
                if board[klinen+1][kfilen-1] in ["s","k","b","+b","+r"]:
                    ischck = True
                    print("{} is checking to sente from the back right".format(board[klinen+1][kfilen-1]))
            elif kfilen == 0:
                if board[klinen+1][kfilen+1] in ["s","k","b","+b","+r"]:
                    ischck = True
                    print("{} is checking to sente from the back left".format(board[klinen+1][kfilen+1]))
            else:
                if board[klinen+1][kfilen-1] in ["s","k","b","+b","+r"]:
                    ischck = True
                    print("{} is checking to sente from the back right".format(board[klinen+1][kfilen-1]))
                if board[klinen+1][kfilen+1] in ["s","k","b","+b","+r"]:
                    ischck = True
                    print("{} is checking to sente from the back left".format(board[klinen+1][kfilen+1]))
        #check rook's check
        for piece in reversed(board[klinen][:kfilen]):
            if piece == "r" or piece == "+r":
                ischck = True
                print("rook is checking from the right")
                break
            elif piece != "":
                break
        for piece in board[klinen][kfilen+1:]:
            if piece == "r" or piece == "+r":
                ischck = True
                print("rook is checking from the left")
                break
            elif piece != "":
                break
        for piece in reversed([line[kfilen] for line in board][:klinen]):
            if piece == "r" or piece == "+r" or piece == "l":
                ischck = True
                print("rook or lance is checking from the front")
                break
            elif piece != "":
                break
        for piece in [line[kfilen] for line in board][klinen+1:]:
            if piece == "r" or piece == "+r":
                ischck = True
                print("rook is checking from the back")
                break
            elif piece != "":
                break
        #check bishop's check #the hardest part
        for i in range(1,9):
            if kfilen+i > 8 or klinen+i > 8:
                break
            if board[klinen+i][kfilen+i] == "b" or board[klinen+i][kfilen+i] == "+b":
                ischck = True
                print("bishop is checking from the back left")
                break
            elif board[klinen+i][kfilen+i] != "":
                break
        for i in range(1,9):
            if kfilen-i < 0 or klinen-i < 0:
                break
            if board[klinen-i][kfilen-i] == "b" or board[klinen-i][kfilen-i] == "+b":
                ischck = True
                print("bishop is checking from the front right")
                break
            elif board[klinen-i][kfilen-i] != "":
                break
        for i in range(1,9):
            if kfilen+i > 8 or klinen-i < 0:
                break
            if board[klinen-i][kfilen+i] == "b" or board[klinen-i][kfilen+i] == "+b":
                ischck = True
                print("bishop is checking from the front left")
                break
            elif board[klinen-i][kfilen+i] != "":
                break
        for i in range(1,9):
            if kfilen-i < 0 or klinen+i > 8:
                break
            if board[klinen+i][kfilen-i] == "b" or board[klinen+i][kfilen-i] == "+b":
                ischck = True
                print("bishop is checking from the back right")
                break
            elif board[klinen+i][kfilen-i] != "":
                break
    return ischck

def isThisMoveLegal(board,move):
    piece = move[0]
    x1 = move[1]
    x2 = move[2]
    y1 = move[3]
    y2 = move[4]
    board[y1][x1] = ""
    board[y2][x2] = piece
    legal = not isCheck(board)
    if not legal:
        print("{}{}{} is not legal".format(x2+1,y2+1,piece))

    return legal
