from Piece import Piece
from Pawn import Pawn
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from King import King

class Board:
    board = {}
    inCheck = False
    turn = "white"
    whiteKing = King('a', '1', 'white')
    blackKing = King('a', '1', 'black')
    columns = []
    rows = []

    def __init__(self):
        self.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.rows = ['1', '2', '3', '4', '5', '6', '7', '8']

        for i in range(1, 9):
            index = str(i)
            for j in range (0, 8):        
            	if i == 2 :
            	    self.board[self.columns[j]+index] = Pawn(self.columns[j], index, "white")
            	elif i == 7:
            	    self.board[self.columns[j]+index] = Pawn(self.columns[j], index, "black")
            	elif i > 2 and i < 7:
            	    self.board[self.columns[j]+index] = Piece(self.columns[j], index, "blank", "  ")

        #Initialize white pieces
        self.board['a1'] = Rook('a', '1', "white")
        self.board['b1'] = Knight('b', '1', "white")
        self.board['c1'] = Bishop('c', '1', "white")
        self.board['d1'] = King('d', '1', "white")
        self.board['e1'] = Queen('e', '1', "white")
        self.board['f1'] = Bishop('f', '1', "white")
        self.board['g1'] = Knight('g', '1', "white")
        self.board['h1'] = Rook('h', '1', "white")

        #Initialize black pieces
        self.board['a8'] = Rook('a', '8', "black")
        self.board['b8'] = Knight('b', '8', "black")
        self.board['c8'] = Bishop('c', '8', "black")
        self.board['d8'] = King('d', '8', "black")
        self.board['e8'] = Queen('e', '8', "black")
        self.board['f8'] = Bishop('f', '8', "black")
        self.board['g8'] = Knight('g', '8', "black")
        self.board['h8'] = Rook('h', '8', "black")					

        #Initialize backup kings for check calculations
        self.whiteKing = King('d', '1', "white")
        self.blackKing = King('d', '8', "black")


    def printBoard(self):
        print("")
        for i in range(8, 0, -1):
            index = str(i)
            print(index + " ", end="")
            for j in range(0, 8):
                print("[" + self.board[self.columns[j]+index].shape + "]", end="")

            print("")

        print("   a   b   c   d   e   f   g   h\n")


    def movePiece(self, pieceToMove, destination):
        print("Moved " + self.turn + "'s piece")
        
        self.board[pieceToMove].moves += 1
        self.board[pieceToMove].position = self.board[destination].position
        self.board[destination] = self.board[pieceToMove]
        self.board[pieceToMove] = Piece(pieceToMove[0], pieceToMove[1], "blank", "  ")

        if self.board[destination].shape == 'wK':
            whiteKing = self.board[destination]
        elif self.board[destination].shape == 'bK':
            blackKing = self.board[destination]
            
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"


    def isValidMove(self, start, finish):
        if not self.validInput(finish):
            return False

        if not self.validInput(start):
            return False

        if self.board[start].colour != self.turn:
            return False
        elif self.board[start].validMove(start, finish, self.board[start], self.board[finish], self.board):
            if self.check():
                self.inCheck = True

                tempStart = self.board[start]
                tempFinish = self.board[finish]

                self.board[start].position = self.board[finish].position
                self.board[finish] = self.board[start]
                self.board[start] = Piece(start[0], start[1], "blank", "  ")

                if tempStart.shape == 'wK':
                    self.whiteKing = self.board[finish]
                elif tempStart.shape == 'bK':
                    self.blackKing = self.board[finish]
                    
                if self.check():
                    self.board[start] = tempStart
                    self.board[start].position = start
                    self.board[finish] = tempFinish
                    self.board[finish].position = finish
                    if tempStart.shape == 'wK':
                        self.whiteKing = tempStart
                        self.whiteKing.position = start
                    elif tempStart.shape == 'bK':
                        self.blackKing = tempStart
                        self.blackKing.position = start

                    return False
                else:
                    self.board[start] = tempStart
                    self.board[start].position = start
                    self.board[finish] = tempFinish
                    self.board[finish].position = finish
                    if tempStart.shape == 'wK':
                        self.whiteKing = tempStart
                        self.whiteKing.position = start
                    elif tempStart.shape == 'bK':
                        self.blackKing = tempStart
                        self.blackKing.position = start
                        
            return True
        else:
            return False


    def validInput(self, move):
        if move in self.board.keys():
            return True
        else:
            return False
        
        
    def check(self):
        king = King('a', '1', 'white')

        if self.turn == "white":
            king = self.whiteKing
        else:
            king = self.blackKing

        for cell in self.board.keys():
            if self.board[cell].validMove(cell, king.position, self.board[cell], king, self.board):
                return True

        return False                    


    def getValidMoves(self, piece):
        validMoves = []

        for cell in self.board.keys():
            if piece.validMove(piece.position, self.board[cell].position, piece, self.board[cell], self.board):
                validMoves.append(cell)

        return validMoves

    
    def checkMate(self):
        validMoves = []

        if self.check():
            for cell in self.board.keys():
                if self.board[cell].colour == self.turn:
                    validMoves = self.getValidMoves(self.board[cell])
                    for k in range(0, len(validMoves)):
                        finish = validMoves[k]
                        tempStart = self.board[cell]
                        tempFinish = self.board[finish]
                        
                        self.board[cell].position = self.board[finish].position
                        self.board[finish] = self.board[cell]
                        self.board[cell] = Piece(cell[0], cell[1], "blank", "  ")
                            
                        if tempStart.shape == 'wK':
                            self.whiteKing = self.board[finish]
                        elif tempStart.shape == 'bK':
                            self.blackKing = self.board[finish]
                                
                        if not self.check():
                            self.board[cell] = tempStart
                            self.board[cell].position = cell
                            self.board[finish] = tempFinish
                            self.board[finish].position = finish
                        
                            if tempStart.shape == 'wK':
                                self.whiteKing = tempStart
                                self.whiteKing.position = cell
                            elif tempStart.shape == 'bK':
                                self.blackKing = tempStart
                                self.blackKing.position = cell
                                
                            return False
                        else:
                            self.board[cell] = tempStart
                            self.board[cell].position = cell
                            self.board[finish] = tempFinish
                            self.board[finish].position = finish
                            
                            if tempStart.shape == 'wK':
                                self.whiteKing = tempStart
                                self.whiteKing.position = cell
                            elif tempStart.shape == 'bK':
                                self.blackKing = tempStart
                                self.blackKing.position = cell

            return True
        else:
            return False

    
    def gameloop(self):
        done = False

        while not done:
            self.printBoard()
                
            print(self.turn + "'s turn")
            start = input("Enter piece to move (cell): ")
            finish = input("Enter destination cell: ")
            while not self.isValidMove(start, finish):
                print("Invalid input. Please try again.")
                start = input("Enter piece to move (cell): ")
                finish = input("Enter destination cell: ") 

            self.movePiece(start, finish)

            if self.checkMate():
                done = True

        print("Checkmate!")
        if self.turn == 'black':
            print("White is the Winner!")
        else:
            print("Black is the Winner!")

        self.printBoard()
