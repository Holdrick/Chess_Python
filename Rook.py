from Piece import Piece

class Rook(Piece):
    def __init__(self, column, row, colour):
        self.position = column + row
        self.colour = colour
        self.shape = colour[0] + "r"


    def validMove(self, start, finish, player, destination, board):
        si = self.columns.index(start[0])
        fi = self.columns.index(finish[0])
        sRow = self.rows.index(start[1]) + 1
        fRow = self.rows.index(finish[1]) + 1
        
        if player.colour != destination.colour:
            sIndex = 0
            fIndex = 0

            if si == fi: #same column
                c = self.columns[si]
                
                if sRow <= fRow:
                    sIndex = sRow
                    fIndex = fRow
                else:
                    sIndex = fRow
                    fIndex = sRow

                for i in range(sIndex, fIndex-1):
                    r = self.rows[i]
                    if board[c + r].colour != "blank":
                        return False
                    
                return True
            
            elif sRow == fRow: #same row
                r = self.rows[sRow-1]
                if si <= fi:
                    sIndex = si
                    fIndex = fi
                else:
                    sIndex = fi
                    fIndex = si

                for i in range(sIndex+1, fIndex):
                    c = self.columns[i]
                    
                    if board[c + r].colour != "blank":
                        return False
                    
                return True

        return False
