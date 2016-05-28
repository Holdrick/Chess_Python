class Piece:
    alive = True
    moves = 0
    position = ""
    colour = ""
    shape = ""
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rows = ['1', '2', '3', '4', '5', '6', '7', '8']

    def __init__(self, column, row, colour, shape):
        self.position = column + row
        self.colour = colour
        self.shape = shape

    def validMove(self, start, finish, pieceToMove, destination, board):
        return False
