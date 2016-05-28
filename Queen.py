from Piece import Piece
from Bishop import Bishop
from Rook import Rook

class Queen(Piece):
    bishop = Bishop('a', '1', 'white')
    rook = Rook('a', '1', 'black')
    
    def __init__(self, column, row, colour):
        self.position = column + row
        self.colour = colour
        self.shape = colour[0] + "Q"

    def validMove(self, start, finish, player, destination, board):
        si = self.columns.index(start[0])
        fi = self.columns.index(finish[0])
        sr = self.rows.index(start[1]) + 1
        fr = self.rows.index(finish[1]) + 1

        if player.colour != destination.colour:
            if self.bishop.validMove(start, finish, player, destination, board):
                return True
            if self.rook.validMove(start, finish, player, destination, board):
                return True

        return False
