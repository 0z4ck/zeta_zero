from moves import Moves
import random
from utils import util
import time
import copy

class Game:

    def __init__(self,board=None):
        if board:
            self.board = board
        mv = Moves()

    def loadPosition(self, usimoves):
        
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
        sfd = {'a': 0, 'c': 2, 'b': 1, 'e': 4, 'd': 3, 'g': 6, 'f': 5, 'i': 8, 'h': 7}

        for move in usimoves:
            if len(move)<4:
                pass
            elif move=="moves":
                pass
            elif move[1]=="*":
                if c%2==0:
                    piece = move[0]
                else:
                    piece = move[0].lower()
                self.board[sfd[move[3]]][int(move[2])-1] = piece
                c += 1 
            else:
                piece = self.board[sfd[move[1]]][int(move[0])-1]
                if move[-1]=="+":
                    piece = "+"+piece
                self.board[sfd[move[3]]][int(move[2])-1] = piece
                self.board[sfd[move[1]]][int(move[0])-1] = ""
                c += 1 
        self.sente = c%2==0
        util.prettifier(self.board)

    def go(self):
        mv = Moves()
        movelist = []
        y = 0
        if util.isCheck(self.board):
            print("bestmove {}".format("resign"))
            return
        for line in self.board:
            x = 0
            for square in line:
                #print("{}{}".format(x,y))
                if square=="P":
                    mlist = mv.pawn(x,y)

                    mlist2 = filter(lambda xy: not self.board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            movelist.append(usimove)
                            print(usimove)
                            print("pawn at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
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
                            movelist.append(usimove)
                            print(usimove)
                            print("lance at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="N":
                    mlist = mv.knight(x,y)

                    mlist2 = filter(lambda xy: not self.board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            movelist.append(usimove)
                            print(usimove)
                            print("knight at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="S":
                    mlist = mv.silver(x,y)

                    mlist2 = filter(lambda xy: not self.board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            movelist.append(usimove)
                            print(usimove)
                            print("silver at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="G":
                    mlist = mv.gold(x,y)

                    mlist2 = filter(lambda xy: not self.board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            movelist.append(usimove)
                            print(usimove)
                            print("gold at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="K":
                    mlist = mv.king(x,y)
                    mlist2 = filter(lambda xy: not self.board[xy[1]][xy[0]].isupper(),mlist)

                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            movelist.append(usimove)
                            print(usimove)
                            print("king at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
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
                            movelist.append(usimove)
                            print(usimove)
                            print("rook at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
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
                            movelist.append(usimove)
                            print(usimove)
                            print("bishop at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                elif square=="+P" or square=="+L" or square=="+N" or square=="+S":
                    mlist = mv.gold(x,y)

                    mlist2 = filter(lambda xy: not self.board[xy[1]][xy[0]].isupper(),mlist)
                    for x2, y2 in mlist2:
                        if util.isThisMoveLegal(copy.deepcopy(self.board),(square.upper(),x,x2,y,y2)):
                            usimove = util.rawtousi(square.lower(),x,x2,y,y2,self.sente)
                            movelist.append(usimove)
                            print(usimove)
                            print("narikin at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
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
                            movelist.append(usimove)
                            print(usimove)
                            print("dragon at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
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
                            movelist.append(usimove)
                            print(usimove)
                            print("horse at {}{} can move to {}{}".format(x+1,y+1,x2+1,y2+1))
                x += 1
            y += 1
        print(movelist)
        bm = random.choice(movelist)
        #time.sleep(5)
        print("bestmove {}".format(bm))
        #print("bestmove {}".format("resign"))
