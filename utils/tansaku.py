from utils import util, evaluation
import copy

def minimax(board,kmd,okmd,mv,depth,c_depth,sente):
    if depth==0:
        return evaluation.evaluation(board,kmd,okmd,mv)
    movelist = []
    y = 0
    if c_depth%2==0 :
        for line in board:
            x = 0
            for square in line:
                if square=="P":
                    mlist = mv.pawn(x,y)
    
                    mlist2 = filter(lambda xy: not board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            if y2 < 3:
                                usimove += "+"
                            movelist.append(usimove)
                elif square=="L":
                    mlist = mv.lance(x,y)
                    mlist2 = []
                    for lx,ly in mlist:
                        if board[ly][lx]=="":
                            mlist2.append((lx,ly))
                        elif board[ly][lx].isupper():
                            break
                        else:
                            mlist2.append((lx,ly))
                            break
                        
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            if y2 < 3:
                                usimove += "+"
                            movelist.append(usimove)
                elif square=="N":
                    mlist = mv.knight(x,y)
    
                    mlist2 = filter(lambda xy: not board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            if y2 < 3:
                                usimove += "+"
                            movelist.append(usimove)
                elif square=="S":
                    mlist = mv.silver(x,y)
    
                    mlist2 = filter(lambda xy: not board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            if y2 < 3:
                                usimove += "+"
                            movelist.append(usimove)
                elif square=="G":
                    mlist = mv.gold(x,y)
    
                    mlist2 = filter(lambda xy: not board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            movelist.append(usimove)
                elif square=="K":
                    mlist = mv.king(x,y)
                    mlist2 = filter(lambda xy: not board[xy[1]][xy[0]].isupper(),mlist)
    
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            movelist.append(usimove)
                elif square=="R":
                    mlist = mv.rook(x,y)
                    mlist2 = []
                    #print(mlist)
                    for mlpart in mlist[:4]:
                        for lx,ly in mlpart:
                            if board[ly][lx]=="":
                                mlist2.append((lx,ly))
                            elif board[ly][lx].isupper():
                                break
                            else:
                                mlist2.append((lx,ly))
                                break
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            if y2 < 3:
                                usimove += "+"
                            movelist.append(usimove)
                elif square=="B":
                    mlist = mv.bishop(x,y)
                    mlist2 = []
                    #print(mlist)
                    for mlpart in mlist[:4]:
                        for lx,ly in mlpart:
                            if board[ly][lx]=="":
                                mlist2.append((lx,ly))
                            elif board[ly][lx].isupper():
                                break
                            else:
                                mlist2.append((lx,ly))
                                break
    
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            if y2 < 3:
                                usimove += "+"
                            movelist.append(usimove)
                elif square=="+P" or square=="+L" or square=="+N" or square=="+S":
                    mlist = mv.gold(x,y)
    
                    mlist2 = filter(lambda xy: not board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            movelist.append(usimove)
                elif square=="+R":
                    mlist = mv.rook(x,y,dragon=True)
                    mlist2 = []
                    for mlpart in mlist[:4]:
                        for lx,ly in mlpart:
                            if board[ly][lx]=="":
                                mlist2.append((lx,ly))
                            elif board[ly][lx].isupper():
                                break
                            else:
                                mlist2.append((lx,ly))
                                break
                    for lx,ly in mlist[4]:
                            mlist2.append((lx,ly))
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            movelist.append(usimove)
                elif square=="+B":
                    mlist = mv.bishop(x,y,horse=True)
                    mlist2 = []
                    for mlpart in mlist[:4]:
                        for lx,ly in mlpart:
                            if board[ly][lx]=="":
                                mlist2.append((lx,ly))
                            elif board[ly][lx].isupper():
                                break
                            else:
                                mlist2.append((lx,ly))
                                break
                    for lx,ly in mlist[4]:
                            mlist2.append((lx,ly))
    
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            movelist.append(usimove)
                x += 1
            y += 1
        sfeny = ["a","b","c","d","e","f","g","h","i"]
        for koma in kmd:
            for tempy in range(9):
                for tempx in range(9):
                    if board[tempy][tempx]=="":
                        if sente:
                            usimove = "{}*{}{}".format(koma.upper(),tempx+1,sfeny[tempy])
                        else:
                            usimove = "{}*{}{}".format(koma.upper(),9-tempx,sfeny[8-tempy])
                        if util.isThisDropLegal(copy.deepcopy(board),(koma.upper(),tempx,tempy)):
                            movelist.append(usimove)
    else:
        for line in board:
            x = 0
            for square in line:
                if square=="p":
                    mlist = mv.pawn(x,y,me=False)
    
                    mlist2 = filter(lambda xy: not board[xy[1]][xy[0]].islower(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            if y2 < 3:
                                usimove += "+"
                            movelist.append(usimove)
                elif square=="l":
                    mlist = mv.lance(x,y,me=False)
                    mlist2 = []
                    for lx,ly in mlist:
                        if board[ly][lx]=="":
                            mlist2.append((lx,ly))
                        elif board[ly][lx].islower():
                            break
                        else:
                            mlist2.append((lx,ly))
                            break
                        
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            if y2 < 3:
                                usimove += "+"
                            movelist.append(usimove)
                elif square=="n":
                    mlist = mv.knight(x,y,me=False)
    
                    mlist2 = filter(lambda xy: not board[xy[1]][xy[0]].islower(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            if y2 < 3:
                                usimove += "+"
                            movelist.append(usimove)
                elif square=="s":
                    mlist = mv.silver(x,y,me=False)
    
                    mlist2 = filter(lambda xy: not board[xy[1]][xy[0]].islower(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            if y2 < 3:
                                usimove += "+"
                            movelist.append(usimove)
                elif square=="g":
                    mlist = mv.gold(x,y,me=False)
    
                    mlist2 = filter(lambda xy: not board[xy[1]][xy[0]].islower(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            movelist.append(usimove)
                elif square=="k":
                    mlist = mv.king(x,y)
                    mlist2 = filter(lambda xy: not board[xy[1]][xy[0]].islower(),mlist)
    
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            movelist.append(usimove)
                elif square=="r":
                    mlist = mv.rook(x,y)
                    mlist2 = []
                    #print(mlist)
                    for mlpart in mlist[:4]:
                        for lx,ly in mlpart:
                            if board[ly][lx]=="":
                                mlist2.append((lx,ly))
                            elif board[ly][lx].islower():
                                break
                            else:
                                mlist2.append((lx,ly))
                                break
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            if y2 < 3:
                                usimove += "+"
                            movelist.append(usimove)
                elif square=="b":
                    mlist = mv.bishop(x,y)
                    mlist2 = []
                    #print(mlist)
                    for mlpart in mlist[:4]:
                        for lx,ly in mlpart:
                            if board[ly][lx]=="":
                                mlist2.append((lx,ly))
                            elif board[ly][lx].islower():
                                break
                            else:
                                mlist2.append((lx,ly))
                                break
    
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            if y2 < 3:
                                usimove += "+"
                            movelist.append(usimove)
                elif square=="+p" or square=="+l" or square=="+n" or square=="+s":
                    mlist = mv.gold(x,y,me=False)
    
                    mlist2 = filter(lambda xy: not board[xy[1]][xy[0]].islower(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            movelist.append(usimove)
                elif square=="+r":
                    mlist = mv.rook(x,y,dragon=True)
                    mlist2 = []
                    for mlpart in mlist[:4]:
                        for lx,ly in mlpart:
                            if board[ly][lx]=="":
                                mlist2.append((lx,ly))
                            elif board[ly][lx].islower():
                                break
                            else:
                                mlist2.append((lx,ly))
                                break
                    for lx,ly in mlist[4]:
                            mlist2.append((lx,ly))
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            movelist.append(usimove)
                elif square=="+b":
                    mlist = mv.bishop(x,y,horse=True)
                    mlist2 = []
                    for mlpart in mlist[:4]:
                        for lx,ly in mlpart:
                            if board[ly][lx]=="":
                                mlist2.append((lx,ly))
                            elif board[ly][lx].islower():
                                break
                            else:
                                mlist2.append((lx,ly))
                                break
                    for lx,ly in mlist[4]:
                            mlist2.append((lx,ly))
    
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,sente)
                            movelist.append(usimove)
                x += 1
            y += 1
        sfeny = ["a","b","c","d","e","f","g","h","i"]
        for koma in okmd:
            for tempy in range(9):
                for tempx in range(9):
                    if board[tempy][tempx]=="":
                        if sente:
                            usimove = "{}*{}{}".format(koma.upper(),tempx+1,sfeny[tempy])
                        else:
                            usimove = "{}*{}{}".format(koma.upper(),9-tempx,sfeny[8-tempy])
                        if util.isThisDropLegal(copy.deepcopy(board),(koma.upper(),tempx,tempy)):
                            movelist.append(usimove)


    w = len(movelist)


    if w == 0:
        return evaluation.evaluation(board,kmd,okmd,mv,turn="opponent")
    
    if c_depth%2==0:
        maxs = float("-inf")
        for i in range(w):
            usim = movelist[i]
            rawm = util.usitoraw(board,usim,sente)
            cboard = copy.deepcopy(board)
            legal = util.isThisMoveLegal(cboard,rawm,me=True)
            if not legal:
                continue
            cboard2 = copy.deepcopy(board)
            piece = rawm[0]
            x1 = rawm[1]
            x2 = rawm[2]
            y1 = rawm[3]
            y2 = rawm[4]
            if x1 and y1:
                cboard2[y1][x1] = ""
            cboard2[y2][x2] = piece
            score = minimax(cboard,kmd,okmd,mv,depth-1,c_depth+1,sente)
            if score>maxs:
                maxs = score
        return maxs
    else:
        mins = float("inf")
        for i in range(w):
            usim = movelist[i]
            rawm = util.usitoraw(board,usim,sente)
            cboard = copy.deepcopy(board)
            legal = util.isThisMoveLegal(cboard,rawm,me=False)
            if not legal:
                continue
            cboard2 = copy.deepcopy(board)
            piece = rawm[0]
            x1 = rawm[1]
            x2 = rawm[2]
            y1 = rawm[3]
            y2 = rawm[4]
            if x1 and y1:
                cboard2[y1][x1] = ""
            cboard2[y2][x2] = piece
            score = minimax(cboard,kmd,okmd,mv,depth-1,c_depth+1,sente)
            if score<mins:
                mins = score
        return mins


