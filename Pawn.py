from Piece import Piece

class Pawn(Piece):
    def __init__(self, column, row, colour):
        self.position = column + row
        self.colour = colour
        self.shape = colour[0] + "p"


    def validMove(self, start, finish, player, destination, board):
        si = self.columns.index(start[0])
        fi = self.columns.index(finish[0])
        sr = self.rows.index(start[1]) + 1
        fr = self.rows.index(finish[1]) + 1
            
        if player.colour != destination.colour:
            if (fi == si + 1) or (fi == si - 1): #one space diagonal
                if player.colour == "white" and destination.colour == "black":
                    if fr == sr + 1: #valid white attack
                        return True
                elif player.colour == "black" and destination.colour == "white":
                    if fr == sr - 1: #valid black attack
                        return True
            elif fi == si: #same column
                if destination.colour != "blank":
                    return False

                if player.colour == "white":
                    if fr == sr + 2:
                        if sr == 2 and self.moves == 0: #valid white 2 space move
                            if board[self.columns[si]+'3'].colour == "blank":
                                return True
                    elif fr == sr + 1: #valid white 1 space move
                        return True
                elif player.colour == "black":
                    if fr == sr - 2:
                        if sr == 7 and self.moves == 0: #valid black 2 space move
                            if board[self.columns[si]+'6'].colour == "blank":
                                return True
                    elif fr == sr - 1: #valid black 1 space move
                        return True

        return False
