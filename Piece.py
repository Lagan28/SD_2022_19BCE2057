blocked_path = "There's a piece in the path."
incorrect_path = "This piece does not move in this pattern."


class Piece:
    """
    A class to represent a piece in chess
    Attributes:
    --------
    Pawn->P

    Methods:
    --------
    is_valid_move(board, start, to) -> bool
        Returns True if moving the piece at `start` to `to` is a legal
        move on board `board`
        Precondition: [start] and [to] are valid coordinates on the board.board
    is_white() -> bool
        Return True if piece is white

    """

    def __init__(self, color):
        self.name = ""
        self.color = color

    def is_valid_move(self, board, start, to):
        return False

    def is_white(self):
        return self.color

    def __str__(self):
        if self.color:
            return self.name
        else:
            return '\033[94m' + self.name + '\033[0m'


class GhostPawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "GP"

    def is_valid_move(self, board, start, to):
        return False


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "P"
        self.first_move = True

    def is_valid_move(self, board, start, to):
        if self.color:
            # diagonal move
            if start[0] == to[0] + 1 and (start[1] == to[1] + 1 or start[1] == to[1] - 1):
                # if board.board[to[0]][to[1]] is not None:
                #     self.first_move = False
                #     return True
                print("Cannot move diagonally.\n")
                return False

            # vertical move
            if start[1] == to[1]:
                if start[0] - to[0] == 1:
                    for i in range(start[0] - 1, to[0] - 1, -1):
                        if board.board[i][start[1]] is not None:
                            print(blocked_path)
                            return False
                    # insert a GhostPawn
                    if start[0] - to[0] == 1:
                        board.board[start[0]][start[1]] = GhostPawn(self.color)
                        board.white_ghost_piece = (start[0], start[1])
                    self.first_move = False
                    return True
                print("Invalid move")
                return False
            print(incorrect_path)
            return False

        else:
            if start[0] == to[0] - 1 and (start[1] == to[1] - 1 or start[1] == to[1] + 1):
                if board.board[to[0]][to[1]] is not None:
                    self.first_move = False
                    return True
                print(blocked_path)
                return False
            if start[1] == to[1]:
                if to[0] - start[0] == 1:
                    for i in range(start[0] + 1, to[0] + 1):
                        if board.board[i][start[1]] is not None:
                            print(blocked_path)
                            return False
                    # insert a GhostPawn
                    if to[0] - start[0] == 2:
                        board.board[start[0]][start[1]] = GhostPawn(self.color)
                        board.black_ghost_piece = (start[0], start[1])
                    self.first_move = False
                    return True
                print("Invalid move")
                return False
            print(incorrect_path)
            return False


class Hero(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "H"
        self.first_move = True

    def is_valid_move(self, board, start, to):
        if self.color:
            # diagonal move
            if start[0] == to[0] + 1 and (start[1] == to[1] + 1 or start[1] == to[1] - 1):
                if board.board[to[0]][to[1]] is not None:
                    self.first_move = False
                    return True
                print("Cannot move diagonally unless taking.\n")
                return False

            # vertical move
            if start[1] == to[1]:
                if (start[0] - to[0] == 2 and self.first_move) or (start[0] - to[0] == 1):
                    for i in range(start[0] - 1, to[0] - 1, -1):
                        if board.board[i][start[1]] is not None:
                            print(blocked_path)
                            return False
                    # insert a GhostPawn
                    if start[0] - to[0] == 2:
                        board.board[start[0] - 1][start[1]] = GhostPawn(self.color)
                        board.white_ghost_piece = (start[0] - 1, start[1])
                    self.first_move = False
                    return True
                print("Invalid move" + " or " + "Cannot move forward twice if not first move.\n")
                return False
            print(incorrect_path)
            return False

        else:
            if start[0] == to[0] - 1 and (start[1] == to[1] - 1 or start[1] == to[1] + 1):
                if board.board[to[0]][to[1]] is not None:
                    self.first_move = False
                    return True
                print(blocked_path)
                return False
            if start[1] == to[1]:
                if (to[0] - start[0] == 2 and self.first_move) or (to[0] - start[0] == 1):
                    for i in range(start[0] + 1, to[0] + 1):
                        if board.board[i][start[1]] is not None:
                            print(blocked_path)
                            return False
                    # insert a GhostPawn
                    if to[0] - start[0] == 2:
                        board.board[start[0] + 1][start[1]] = GhostPawn(self.color)
                        board.black_ghost_piece = (start[0] + 1, start[1])
                    self.first_move = False
                    return True
                print("Invalid move" + " or " + "Cannot move forward twice if not first move.\n")
                return False
            print(incorrect_path)
            return False