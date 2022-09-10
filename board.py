import Piece

alphabet = ["A", "B", "C", "D", "E"]

class Board:
    """
        A class to represent a chess board.
    """
    def __init__(self):
        self.board = []

        for i in range(5):
            self.board.append([None] * 5)

        # Player 1
        for i in range(5):
            self.board[4][0] = Piece.Pawn(True)
            self.board[4][1] = Piece.Hero(True)
            self.board[4][2] = Piece.Hero(True)
            self.board[4][3] = Piece.Hero(True)
            self.board[4][4] = Piece.Pawn(True)

        # Player 2
        for i in range(5):
            self.board[0][0] = Piece.Pawn(False)
            self.board[0][1] = Piece.Hero(False)
            self.board[0][2] = Piece.Hero(False)
            self.board[0][3] = Piece.Pawn(False)
            self.board[0][4] = Piece.Hero(False)

    def print_board(self):
        print('    ' + '   '.join(map(str, alphabet)))
        for i in range(len(self.board)):
            tmp_str = str(len(self.board)-i) + " |"
            for j in self.board[i]:
                if j is None or j.name == 'GP':
                    tmp_str += "   |"
                elif len(j.name) == 2:
                    tmp_str += (" " + str(j) + "|")
                else:
                    tmp_str += (" " + str(j) + " |")
            print(tmp_str)


