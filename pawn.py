from Piece import Piece
from Coordinate import Coordinate as C
from Move import Move

WHITE = True
BLACK = False

class Pawn(Piece):
    value=1

    def __init__(self, board, side, position, movesMade=0):
        super(Pawn, self).__init__(board, side, position)
        self.movesMade = movesMade

    def getPossibleMoves(self):
        currentPosition = self.position

        # Pawn moves one up
        movement = C(0, 1) if self.side == WHITE else C(0, -1)
        advanceOnePosition = currentPosition + movement
        if self.board.isValidPos(advanceOnePosition):
            # Promotion moves
            if self.board.pieceAtPosition(advanceOnePosition) is None:
                col = advanceOnePosition[1]
                yield Move(self, advanceOnePosition)

        movements = [C(1, 1), C(-1, 1)] \
            if self.side == WHITE else [C(1, -1), C(-1, -1)]

        for movement in movements:
            newPosition = self.position + movement
            if self.board.isValidPos(newPosition):
                pieceToTake = self.board.pieceAtPosition(newPosition)
                if pieceToTake and pieceToTake.side != self.side:
                    col = newPosition[1]
                    yield Move(self, newPosition)

