from Piece import Piece

class King(Piece):
    def __init__(self, column, row, colour):
        self.position = column + row
        self.colour = colour
        self.shape = colour[0] + "K"


    def validMove(self, start, finish, player, destination, board):
        si = self.columns.index(start[0])
        fi = self.columns.index(finish[0])
        sr = self.rows.index(start[1]) + 1
        fr = self.rows.index(finish[1]) + 1

        if player.colour != destination.colour:
            if fr == sr + 1:
                if fi == si:
                    return True
                elif fi == si + 1:
                    return True
                elif fi == si - 1:
                    return True
            elif fr == sr - 1:
                if fi == si:
                    return True
                elif fi == si + 1:
                    return True
                elif fi == si - 1:
                    return True
            elif fr == sr:
                if fi == si + 1:
                    return True
                elif fi == si - 1:
                    return True

        return False


    def getMoves(self, board):
        col = self.columns.index(position[0])
        row = self.rows.index(position[1])
        moves = []

        cell = self.columns[col+1] + self.rows[row+1]
        if cell in board.keys():
            moves.append(cell)

        cell = self.columns[col+1] + self.rows[row]
        if cell in board.keys():
            moves.append(cell)

        cell = self.columns[col+1] + self.rows[row-1]
        if cell in board.keys():
            moves.append(cell)

        cell = self.columns[col] + self.rows[row+1]
        if cell in board.keys():
            moves.append(cell)

        cell = self.columns[col] + self.rows[row-1]
        if cell in board.keys():
            moves.append(cell)

        cell = self.columns[col-1] + self.rows[row+1]
        if cell in board.keys():
            moves.append(cell)

        cell = self.columns[col-1] + self.rows[row-1]
        if cell in board.keys():
            moves.append(cell)

        cell = self.columns[col-1] + self.rows[row]
        if cell in board.keys():
            moves.append(cell)

        return moves
        
