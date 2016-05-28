from Piece import Piece

class Bishop(Piece):
    def __init__(self, column, row, colour):
        self.position = column + row
        self.colour = colour
        self.shape = colour[0] + "b"

        
    def validMove(self, start, finish, player, destination, board):
        si = self.columns.index(start[0])
        fi = self.columns.index(finish[0])
        sr = self.rows.index(start[1])
        fr = self.rows.index(finish[1])

        if player.colour != destination.colour:
            if (fi - si) == (fr - sr):
                if fi - si > 0:
                    i = si + 1
                    for j in range(sr+1, fr):
                        cell = self.columns[i] + self.rows[j]

                        if board[cell].colour != "blank":
                            return False
                        else:
                            i += 1
                else:
                    i = si - 1
                    for j in range(sr-1, fr, -1):
                        cell = self.columns[i] + self.rows[j]
                        
                        if board[cell].colour != "blank":
                            return False
                        else:
                            i -= 1
                    
                return True
            elif (-1 * (fi - si)) == (fr - sr):
                if fi - si > 0:
                    i = si + 1
                    for j in range(sr-1, fr, -1):
                        cell = self.columns[i] + self.rows[j]

                        if board[cell].colour != "blank":
                            return False
                        else:
                            i += 1

                else:
                    i = si - 1
                    for j in range(sr+1, fr):
                        cell = self.columns[i] + self.rows[j]
                            
                        if board[cell].colour != "blank":
                            return False
                        else:
                            i -= 1
                    
                return True

        return False
