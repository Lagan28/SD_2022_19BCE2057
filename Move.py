class Move:

    def __init__(self, piece, newPos):
        self.notation = None
        self.piece = piece
        self.oldPos = piece.position
        self.newPos = newPos
        self.passant = False

    def __str__(self):
        displayString = 'Old pos : ' + str(self.oldPos) + ' -- New pos : ' + str(self.newPos)
        if self.notation:
            displayString += ' Notation : ' + self.notation
        if self.passant:
            displayString = 'Old pos : ' + str(self.oldPos) + ' -- New pos : ' + str(self.newPos) + ' -- Pawn taken : ' + str(self.specialMovePiece)
            displayString += ' PASSANT'
        return displayString
    def __hash__(self):
        return hash((self.oldPos, self.newPos))

    def reverse(self):
        return Move(self.piece, self.piece.position)