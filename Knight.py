from Piece import Piece

class Knight(Piece):
    def __init__(self, column, row, colour):
        self.position = column + row
        self.colour = colour
        self.shape = colour[0] + "n"


    def validMove(self, start, finish, player, destination, board):
        si = self.columns.index(start[0]) #start position column index
        fi = self.columns.index(finish[0]) #end position column index
        sr = self.rows.index(start[1]) + 1 #start position row index
        fr = self.rows.index(finish[1]) + 1 #end position row index

        if player.colour != destination.colour:
            if fr == sr + 2:
                if fi == si + 1:
                    return True
                elif fi == si - 1:
                    return True
            elif fr == sr - 2:
                if fi == si + 1:
                    return True
                elif fi == si - 1:
                    return True
            elif fr == sr + 1:
                if fi == si + 2:
                    return True
                elif fi == si - 2:
                    return True
            elif fr == sr - 1:
                if fi == si + 2:
                    return True
                elif fi == si - 2:
                    return True

        return False
