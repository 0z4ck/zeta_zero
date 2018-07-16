
class Moves:

    def __init__(self):
        pass

    def pawn(self, x, y, me=True):
        if me:
            return [(x,y-1)]
        else:
            return [(x,y+1)]

    def lance(self, x, y, me=True):
        move_list = []
        if me:
            for i in reversed(range(y)):
                move_list.append((x,i))
            return move_list
        else:
            for i in reversed(range(y+1,9)):
                move_list.append((x,i))
            return move_list
            
    def knight(self, x, y, me=True):
        if me:
            if x == 0:
                return [(x+1,y-2)]
            elif x == 8:
                return [(x-1,y-2)]
            else:
                return [(x-1,y-2),(x+1,y-2)]
        else:
            if x == 0:
                return [(x+1,y+2)]
            elif x == 8:
                return [(x-1,y+2)]
            else:
                return [(x-1,y+2),(x+1,y+2)]

    def silver(self, x, y, me=True):
        if me:
            move_list = [(x,y-1),(x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1)]
            if x == 0:
                for im in ((x-1,y-1),(x-1,y+1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if x == 8:
                for im in ((x+1,y-1),(x+1,y+1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if y == 0:
                for im in ((x,y-1),(x-1,y-1),(x+1,y-1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if y == 8:
                for im in ((x-1,y+1),(x+1,y+1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass

            return move_list
        else:
            move_list = [(x,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1)]
            if x == 0:
                for im in ((x-1,y-1),(x-1,y+1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if x == 8:
                for im in ((x+1,y-1),(x+1,y+1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if y == 0:
                for im in ((x-1,y-1),(x+1,y-1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if y == 8:
                for im in ((x,y+1),(x-1,y+1),(x+1,y+1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            return move_list


    def gold(self, x, y, me=True):
        if me:
            move_list = [(x,y-1),(x-1,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x,y+1)]
            if x == 0:
                for im in ((x-1,y-1),(x-1,y)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if x == 8:
                for im in ((x+1,y-1),(x+1,y)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if y == 0:
                for im in ((x,y-1),(x-1,y-1),(x+1,y-1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if y == 8:
                for im in ((x,y+1),):
                  try:
                    move_list.remove(im)
                  except:
                    pass

            return move_list
        else:
            move_list = [(x,y+1),(x-1,y),(x+1,y),(x-1,y+1),(x+1,y+1),(x,y-1)]
            if x == 0:
                for im in ((x-1,y),(x-1,y+1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if x == 8:
                for im in ((x+1,y),(x+1,y+1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if y == 0:
                for im in ((x,y-1),):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if y == 8:
                for im in ((x,y+1),(x-1,y+1),(x+1,y+1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            return move_list

    def king(self, x, y):
            move_list = [(x,y-1),(x-1,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x,y+1),(x-1,y+1),(x+1,y+1)]
            if x == 0:
                for im in ((x-1,y-1),(x-1,y),(x-1,y+1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if x == 8:
                for im in ((x+1,y-1),(x+1,y),(x+1,y+1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if y == 0:
                for im in ((x,y-1),(x-1,y-1),(x+1,y-1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            if y == 8:
                for im in ((x,y+1),(x-1,y+1),(x+1,y+1)):
                  try:
                    move_list.remove(im)
                  except:
                    pass
            return move_list

    def rook(self, x, y, dragon=False):
            move_list = []
            movefront = []
            moveback = []
            moveleft = []
            moveright = []
            for i in reversed(range(y)):
                movefront.append((x,i))
            move_list.append(movefront)
            for i in range(y+1,9):
                moveback.append((x,i))
            move_list.append(moveback)
            for i in reversed(range(x)):
                moveright.append((i,y))
            move_list.append(moveright)
            for i in range(x+1,9):
                moveleft.append((i,y))
            move_list.append(moveleft)

            if dragon:
                im = [(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)]
                if x==8:
                    for i in ((x+1,y+1),(x+1,y-1)):
                        try:
                            im.remove(i)
                        except:
                            pass
                if y==8:
                    for i in ((x+1,y+1),(x-1,y+1)):
                        try:
                            im.remove(i)
                        except:
                            pass
                if x==0:
                    for i in ((x-1,y-1),(x-1,y+1)):
                        try:
                            im.remove(i)
                        except:
                            pass
                if y==0:
                    for i in (((x-1,y-1)),(x+1,y-1)):
                        try:
                            im.remove(i)
                        except:
                            pass
                move_list.append(im)
            return move_list

    def bishop(self, x, y, horse=False):
            move_list = []
            leftback = []
            rightback = []
            leftfront = []
            rightfront = []
            for i in range(1,9):
                if x+i < 9 and y+i < 9:
                    leftback.append((x+i,y+i))
                if x-i >= 0 and y+i < 9:
                    rightback.append((x-i,y+i))
                if x+i < 9 and y-i >= 0:
                    leftfront.append((x+i,y-i))
                if x-i >= 0 and y-i >= 0:
                    rightfront.append((x-i,y-i))
            for movepart in [leftback,rightback,leftfront,rightfront]:
                move_list.append(movepart)

            if horse:
                im = [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]
                if x==8:
                    for i in ((x+1,y),):
                        try:
                            im.remove(i)
                        except:
                            pass
                if y==8:
                    for i in ((x,y+1),):
                        try:
                            im.remove(i)
                        except:
                            pass
                if x==0:
                    for i in ((x-1,y),):
                        try:
                            im.remove(i)
                        except:
                            pass
                if y==0:
                    for i in (((x,y-1)),):
                        try:
                            im.remove(i)
                        except:
                            pass
                move_list.append(im)
            return move_list

