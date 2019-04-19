import copy
import numpy as np

ROWS = 6
COLUMNS = 7

p_infinity = float("inf")
n_infinity = float("-inf")

class Game:

    def __init__(self):
        
        self.turn = 0
        self.board = self.create_board()

        self.game_over = False

        self.playerX = 21
        self.playerO = 21

    def create_board(self):
        board = np.zeros((ROWS,COLUMNS))
        return board
    
    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece
    
    def is_valid_position(self, col):
        for row in reversed(range(ROWS)):
            if self.board[row][col] == 0:
                return row
        return -1
    
    def winning_move(self, piece):
        #horizontal
        for c in range(COLUMNS-3):
            for r in range(ROWS):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True
        #vertical
        for c in range(COLUMNS):
            for r in range(ROWS-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True
        #diagonal positivo
        for c in range(COLUMNS-3):
            for r in range(ROWS-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True
        #diagonal negativo
        for c in range(COLUMNS-3):
            for r in range(3, ROWS):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True

#INICIO: alínea c)

    def nlinhas4(self, piece):

        linhas = 0

        for c in range(COLUMNS-3):
            for r in range(ROWS):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    linhas += 1
        #vertical
        for c in range(COLUMNS):
            for r in range(ROWS-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    linhas += 1
        #diagonal positivo
        for c in range(COLUMNS-3):
            for r in range(ROWS-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    linhas += 1
        #diagonal negativo
        for c in range(COLUMNS-3):
            for r in range(3, ROWS):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    linhas += 1

        return linhas

    def nlinhas3(self, piece):

        linhas = 0

        for c in range(COLUMNS-3):
            for r in range(ROWS):
                if (self.board[r][c] == 0 and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece) or (self.board[r][c] == piece and self.board[r][c+1] == 0 and self.board[r][c+2] == piece and self.board[r][c+3] == piece) or (self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == 0 and self.board[r][c+3] == piece) or (self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == 0):
                    linhas += 1
        #vertical
        for c in range(COLUMNS):
            for r in range(ROWS-3):
                if (self.board[r][c] == 0 and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece) or (self.board[r][c] == piece and self.board[r+1][c] == 0 and self.board[r+2][c] == piece and self.board[r+3][c] == piece) or (self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == 0 and self.board[r+3][c] == piece) or (self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == 0):
                    linhas += 1
        #diagonal positivo
        for c in range(COLUMNS-3):
            for r in range(ROWS-3):
                if (self.board[r][c] == 0 and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece) or (self.board[r][c] == piece and self.board[r+1][c+1] == 0 and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece) or (self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == 0 and self.board[r+3][c+3] == piece) or (self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == 0):
                    linhas += 1
        #diagonal negativo
        for c in range(COLUMNS-3):
            for r in range(3, ROWS):
                if (self.board[r][c] == 0 and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece) or (self.board[r][c] == piece and self.board[r-1][c+1] == 0 and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece) or (self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == 0 and self.board[r-3][c+3] == piece) or (self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == 0):
                    linhas += 1

        return linhas

    def central(self, piece):
        
        points = 0

        for count in range(ROWS):
            if self.board[count][3] == piece:
                points += 2
            if self.board[count][2] == piece:
                points += 1
            if self.board[count][4] == piece:
                points += 1

        return points

#FIM: alínea c)

    def get_valid_locations(self):
        valid_locations = []
        for col in range(COLUMNS):
            if self.is_valid_position(col) != -1:
                valid_locations.append(col)
        return valid_locations

    def children(self, piece):

        gameChilds = []

        for c in range(COLUMNS):
            row = self.is_valid_position(c)
            if row != -1:
                temporaryGame = copy.deepcopy(self)
                temporaryGame.drop_piece(row, c, piece)
                gameChilds.append([temporaryGame,row, c])

        return gameChilds  