from moves import Moves
import random
from utils import util
import time
import copy
from utils import evaluation

class Game:

    SFD = {'a': 0, 'c': 2, 'b': 1, 'e': 4, 'd': 3, 'g': 6, 'f': 5, 'i': 8, 'h': 7}

    def __init__(self,board=None):
        if board:
            self.board = board
        mv = Moves()

    def loadPosition(self, usimoves):
        
        self.okomadai = []
        self.komadai = []
        self.board = [ ["l","n","s","g","k","g","s","n","l"],
                      ["","b","","","","","","r",""],
                      ["p","p","p","p","p","p","p","p","p"],
                      ["","","","","","","","",""],
                      ["","","","","","","","",""],
                      ["","","","","","","","",""],
                      ["P","P","P","P","P","P","P","P","P"],
                      ["","R","","","","","","B",""],
                      ["L","N","S","G","K","G","S","N","L"] ]
        c = 0
        self.SFD = {'a': 0, 'c': 2, 'b': 1, 'e': 4, 'd': 3, 'g': 6, 'f': 5, 'i': 8, 'h': 7}

        for move in usimoves:
            if len(move)<4:
                pass
            elif move=="moves":
                pass
            else:
                c += 1 

        self.sente = c%2==0

        c = 0
        for move in usimoves:
            if len(move)<4:
                pass
            elif move=="moves":
                pass
            elif move[1]=="*":
                if (c%2==0 and self.sente) or (c%2!=0 and not self.sente):
                    piece = move[0]
                    self.komadai.remove(piece.lower())
                else:
                    piece = move[0].lower()
                    self.okomadai.remove(piece.lower())
                if self.sente:
                    self.board[self.SFD[move[3]]][int(move[2])-1] = piece
                else:
                    self.board[8-self.SFD[move[3]]][9-int(move[2])] = piece
                c += 1 
            else:
                if self.sente:
                    piece = self.board[self.SFD[move[1]]][int(move[0])-1]
                    if move[-1]=="+":
                        piece = "+"+piece
                    if self.board[self.SFD[move[3]]][int(move[2])-1].islower():
                        self.komadai.append(self.board[self.SFD[move[3]]][int(move[2])-1][-1].lower())
                    if self.board[self.SFD[move[3]]][int(move[2])-1].isupper():
                        self.okomadai.append(self.board[self.SFD[move[3]]][int(move[2])-1][-1].lower())
                    self.board[self.SFD[move[3]]][int(move[2])-1] = piece
                    self.board[self.SFD[move[1]]][int(move[0])-1] = ""
                else:
                    piece = self.board[8-self.SFD[move[1]]][9-int(move[0])]
                    if move[-1]=="+":
                        piece = "+"+piece
                    if self.board[8-self.SFD[move[3]]][9-int(move[2])].islower():
                        self.komadai.append(self.board[8-self.SFD[move[3]]][9-int(move[2])][-1].lower())
                    if self.board[8-self.SFD[move[3]]][9-int(move[2])].isupper():
                        self.okomadai.append(self.board[8-self.SFD[move[3]]][9-int(move[2])][-1].lower())
                    self.board[8-self.SFD[move[3]]][9-int(move[2])] = piece
                    self.board[8-self.SFD[move[1]]][9-int(move[0])] = ""
       
                c += 1 

        util.prettifier(self.board)

    def go(self):
        mv = Moves()
        movelist = []
        y = 0
        for line in self.board:
            x = 0
            for square in line:
                if square=="P":
                    mlist = mv.pawn(x,y)

                    mlist2 = filter(lambda xy: not self.board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            if y2 < 3:
                                usimove += "+"
                            #usimove = util.rawtousi(square.lower(),x,x2,y,y2)
                            movelist.append(usimove)
                            #print(usimove)
                            #print("pawn at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="L":
                    mlist = mv.lance(x,y)
                    mlist2 = []
                    for lx,ly in mlist:
                        if self.board[ly][lx]=="":
                            mlist2.append((lx,ly))
                        elif self.board[ly][lx].isupper():
                            break
                        else:
                            mlist2.append((lx,ly))
                            break
                        
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            if y2 < 3:
                                usimove += "+"
                            #usimove = util.rawtousi(square.lower(),x,x2,y,y2)
                            movelist.append(usimove)
                            #print(usimove)
                            #print("lance at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="N":
                    mlist = mv.knight(x,y)

                    mlist2 = filter(lambda xy: not self.board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            if y2 < 3:
                                usimove += "+"
                            #usimove = util.rawtousi(square.lower(),x,x2,y,y2)
                            movelist.append(usimove)
                            #print(usimove)
                            #print("knight at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="S":
                    mlist = mv.silver(x,y)

                    mlist2 = filter(lambda xy: not self.board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            if y2 < 3:
                                usimove += "+"
                            #usimove = util.rawtousi(square.lower(),x,x2,y,y2)
                            movelist.append(usimove)
                            #print(usimove)
                            #print("silver at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="G":
                    mlist = mv.gold(x,y)

                    mlist2 = filter(lambda xy: not self.board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            #usimove = util.rawtousi(square.lower(),x,x2,y,y2)
                            movelist.append(usimove)
                            #print(usimove)
                            #print("gold at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="K":
                    mlist = mv.king(x,y)
                    mlist2 = filter(lambda xy: not self.board[xy[1]][xy[0]].isupper(),mlist)

                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            #usimove = util.rawtousi(square.lower(),x,x2,y,y2)
                            movelist.append(usimove)
                            #print(usimove)
                            #print("king at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="R":
                    mlist = mv.rook(x,y)
                    mlist2 = []
                    print(mlist)
                    for mlpart in mlist[:4]:
                        for lx,ly in mlpart:
                            if self.board[ly][lx]=="":
                                mlist2.append((lx,ly))
                            elif self.board[ly][lx].isupper():
                                break
                            else:
                                mlist2.append((lx,ly))
                                break
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            if y2 < 3:
                                usimove += "+"
                            #usimove = util.rawtousi(square.lower(),x,x2,y,y2)
                            movelist.append(usimove)
                            #print(usimove)
                            #print("rook at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="B":
                    mlist = mv.bishop(x,y)
                    mlist2 = []
                    print(mlist)
                    for mlpart in mlist[:4]:
                        for lx,ly in mlpart:
                            if self.board[ly][lx]=="":
                                mlist2.append((lx,ly))
                            elif self.board[ly][lx].isupper():
                                break
                            else:
                                mlist2.append((lx,ly))
                                break

                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            if y2 < 3:
                                usimove += "+"
                            #usimove = util.rawtousi(square.lower(),x,x2,y,y2)
                            movelist.append(usimove)
                            #print(usimove)
                            #print("bishop at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="+P" or square=="+L" or square=="+N" or square=="+S":
                    mlist = mv.gold(x,y)

                    mlist2 = filter(lambda xy: not self.board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            #usimove = util.rawtousi(square.lower(),x,x2,y,y2)
                            movelist.append(usimove)
                            #print(usimove)
                            #print("narikin at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="+R":
                    mlist = mv.rook(x,y,dragon=True)
                    mlist2 = []
                    for mlpart in mlist[:4]:
                        for lx,ly in mlpart:
                            if self.board[ly][lx]=="":
                                mlist2.append((lx,ly))
                            elif self.board[ly][lx].isupper():
                                break
                            else:
                                mlist2.append((lx,ly))
                                break
                    for lx,ly in mlist[4]:
                            mlist2.append((lx,ly))
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            #usimove = util.rawtousi(square.lower(),x,x2,y,y2)
                            movelist.append(usimove)
                            #print(usimove)
                            #print("dragon at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="+B":
                    mlist = mv.bishop(x,y,horse=True)
                    mlist2 = []
                    for mlpart in mlist[:4]:
                        for lx,ly in mlpart:
                            if self.board[ly][lx]=="":
                                mlist2.append((lx,ly))
                            elif self.board[ly][lx].isupper():
                                break
                            else:
                                mlist2.append((lx,ly))
                                break
                    for lx,ly in mlist[4]:
                            mlist2.append((lx,ly))

                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            #usimove = util.rawtousi(square.lower(),x,x2,y,y2)
                            movelist.append(usimove)
                            #print(usimove)
                            #print("horse at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                x += 1
            y += 1
        sfeny = ["a","b","c","d","e","f","g","h","i"]
        for koma in self.komadai:
            for tempy in range(9):
                for tempx in range(9):
                    if self.board[tempy][tempx]=="":
                        if self.sente:
                            usimove = "{}*{}{}".format(koma.upper(),tempx+1,sfeny[tempy])
                        else:
                            usimove = "{}*{}{}".format(koma.upper(),9-tempx,sfeny[8-tempy])
                        if util.isThisDropLegal(copy.deepcopy(self.board),(koma.upper(),tempx,tempy)):
                            movelist.append(usimove)

        print(movelist)
        #time.sleep(5)
        if util.isCheck(self.board,"opponent"):
            ismate = util.isMate(copy.deepcopy(self.board),movelist,self.sente)
            if ismate[0]:
                print("bestmove {}".format("resign"))
                return
            else:
                movelist = ismate[1]

        scoredmovelist=[]
        for usimove in movelist:
            calcboard = copy.deepcopy(self.board)
            calckmd = copy.deepcopy(self.komadai)
            if usimove[1]=="*":
                piece = usimove[0]
                calckmd.remove(piece.lower())
                if self.sente:
                    calcboard[self.SFD[usimove[3]]][int(usimove[2])-1] = piece
                else:
                    calcboard[8-self.SFD[usimove[3]]][9-int(usimove[2])] = piece
            else:
                if self.sente:
                    piece = calcboard[self.SFD[usimove[1]]][int(usimove[0])-1]
                    if usimove[-1]=="+":
                        piece = "+"+piece
                    if calcboard[self.SFD[usimove[3]]][int(usimove[2])-1].islower():
                        calckmd.append(calcboard[self.SFD[usimove[3]]][int(usimove[2])-1][-1].lower())
                    calcboard[self.SFD[usimove[3]]][int(usimove[2])-1] = piece
                    calcboard[self.SFD[usimove[1]]][int(usimove[0])-1] = ""
                else:
                    piece = calcboard[8-self.SFD[usimove[1]]][9-int(usimove[0])]
                    if usimove[-1]=="+":
                        piece = "+"+piece
                    if calcboard[8-self.SFD[usimove[3]]][9-int(usimove[2])].islower():
                        calckmd.append(calcboard[8-self.SFD[usimove[3]]][9-int(usimove[2])][-1].lower())
                    calcboard[8-self.SFD[usimove[3]]][9-int(usimove[2])] = piece
                    calcboard[8-self.SFD[usimove[1]]][9-int(usimove[0])] = ""
            #okomadai = evaluation.getokomadai(calcboard,calckmd) 
            score = evaluation.evaluation(calcboard,calckmd,self.okomadai,mv,turn="opponent")
            scoredmovelist.append((usimove,score))

        print(scoredmovelist)
        bm = max(scoredmovelist,key=lambda x:x[1])
        bms = [usimv for usimv,sco in scoredmovelist if sco == bm[1]]
        print(bms)
        bm = random.choice(bms)
        print("bestmove {}".format(bm))
        #print("bestmove {}".format("resign"))
