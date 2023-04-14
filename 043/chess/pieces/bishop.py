from pieces import Piece
import board

class Bishop(Piece):
    def __init__(self, color, type):
        Piece.__init__(self, color, type)

    def __str__(self):
        return "B" if (self.color == "W") else "b"

    def scan(self):
        availMoves = []
        optionCounter = 1
        pieceFound = False
        running = True
        edgeFound = False

        # reset rowCount and colCount
        rowCount = self.row
        colCount = self.col

        # scan up
        if self.row > 0:
            if self.col > 0:
                # scan up and left
                while (rowCount > 0 or colCount > 0) and running and not edgeFound:
                    rowCount -= 1
                    colCount -= 1
                    if colCount == -1 or rowCount == -1:
                        edgeFound = True

                    elif (board.Grid(rowCount, colCount).piece.color != self.color):
                        board.Grid(rowCount, colCount).des = True
                        board.Grid(rowCount, colCount).option = optionCounter
                        optionCounter += 1
                        availMoves.append(board.Grid(rowCount, colCount))
                        if board.Grid(rowCount, colCount).pieceStatus:
                            pieceFound = True

                    else:
                        rowCount = 0
                        colCount = 0
                        running = False

                    if pieceFound:
                        rowCount = 0
                        colCount = 0
                        running = False

            # reset rowCount and colCount
            rowCount = self.row
            colCount = self.col
            edgeFound = False
            running = True
            pieceFound = False

            if self.col < 7:
                # scan up and right
                while (rowCount > 0 or colCount < 7) and running and not edgeFound:
                    rowCount -= 1
                    colCount += 1
                    if colCount == 7 or rowCount == 0:
                        edgeFound = True
                    if (board.Grid(rowCount, colCount).piece.color != self.color):
                        board.Grid(rowCount, colCount).des = True
                        board.Grid(rowCount, colCount).option = optionCounter
                        optionCounter += 1
                        availMoves.append(board.Grid(rowCount, colCount))
                        if board.Grid(rowCount, colCount).pieceStatus:
                            pieceFound = True

                    else:
                        rowCount = 0
                        colCount = 7
                        running = False

                    if pieceFound:
                        rowCount = 0
                        colCount = 7
                        running = False

        #scan down
        if self.row < 7:
            # reset rowCount and colCount
            rowCount = self.row
            colCount = self.col
            edgeFound = False
            running = True
            pieceFound = False

            # scan down and left
            if self.col > 0:
                while (rowCount < 7 or colCount > 0) and running and not edgeFound:
                    rowCount += 1
                    colCount -= 1
                    if colCount == -1 or rowCount == 8:
                        edgeFound = True
                    elif (board.Grid(rowCount, colCount).piece.color != self.color):
                        board.Grid(rowCount, colCount).des = True
                        board.Grid(rowCount, colCount).option = optionCounter
                        optionCounter += 1
                        availMoves.append(board.Grid(rowCount, colCount))
                        if board.Grid(rowCount, colCount).pieceStatus:
                            pieceFound = True

                    else:
                        rowCount = 7
                        colCount = 0
                        running = False

                    if pieceFound:
                        rowCount = 7
                        colCount = 0
                        running = False

            # reset rowCount and colCount
            rowCount = self.row
            colCount = self.col
            edgeFound = False
            running = True
            pieceFound = False

            # scan down and right
            if self.col < 7:
                while (rowCount < 7 or colCount < 7) and running and not edgeFound:
                    rowCount += 1
                    colCount += 1
                    if colCount == 8 or rowCount == 8:
                        edgeFound = True
                    elif (board.Grid(rowCount, colCount).piece.color != self.color):
                        board.Grid(rowCount, colCount).des = True
                        board.Grid(rowCount, colCount).option = optionCounter
                        optionCounter += 1
                        availMoves.append(board.Grid(rowCount, colCount))
                        if board.Grid(rowCount, colCount).pieceStatus:
                            pieceFound = True

                    else:
                        rowCount = 7
                        colCount = 7
                        running = False

                    if pieceFound:
                        rowCount = 7
                        colCount = 7
                        running = False

        return availMoves
