SIZE = 3


class Board:
    def __init__(self):
        self._cells = []
        for x in range(SIZE):
            self._cells.append([])
            for y in range(SIZE):
                self._cells[x].append(0)
    
    def getRow(self, n):
        """
        Returns nth row.
        """
        return self._cells[n]
    
    def getCol(self, n):
        """
        Returns nth column.
        """
        toReturn = []
        for i in range(SIZE):
            toReturn.append(self._cells[i][n])
        return toReturn
    
    def getDiags(self):
        """
        Returns diagonals.
        """
        toReturn = [[], []]
        for i in range(SIZE):
            toReturn[0].append(self._cells[i][i])
            toReturn[1].append(self._cells[i][2 - i])
        return toReturn
    
    def makeMove(self, player, move):
        self._cells[move[0]][move[1]] = player
    
    def copy(self):
        newBoard = Board()
        for x in range(SIZE):
            for y in range(SIZE):
                newBoard._cells[x][y] = self._cells[x][y]
        return newBoard
    
    def getNeutrals(self):
        toReturn = []
        for x in range(SIZE):
            for y in range(SIZE):
                if self._cells[x][y] == 0:
                    toReturn.append((x, y))
        return toReturn

class GameState:
    def __init__(self):
        """
        Each state is a board.
        """
        newBoard = Board()
        self._states = [newBoard]
    
    def makeMove(self, n, player, move):
        """
        move is to be made at nth board.
        """
        newBoard = self._states[n].copy()
        newBoard.makeMove(player, move)
        if len(self._states) == n + 1:
            self._states.append(newBoard)
        else:
            self._states[n + 1] = newBoard
    
    def getAvailableMoves(self, n):
        return self._states[n].getNeutrals()
    
    def getBoard(self, n):
        return self._states[n]
    
    def _evaluateLine(self, line):
        players = [0, 0]
        for i in range(SIZE):
            if line[i] == 1:
                players[1] += 1
            elif line[i] == -1:
                players[0] += 1
        if players[0] == SIZE:
            return -300
        elif players[1] == SIZE:
            return 300
        if players[0] == 0:
            return players[1] * 1
        elif players[1] == 0:
            return players[0] * -1
        return 0
    
    def evaluateState(self, n):
        """
        Returns evaluation of nth state.
        """
        evaluations = 0
        for i in range(SIZE):
            evaluations += self._evaluateLine(self._states[n].getRow(i))
        for i in range(SIZE):
            evaluations += self._evaluateLine(self._states[n].getCol(i))
        diags = self._states[n].getDiags()
        evaluations += self._evaluateLine(diags[0])
        evaluations += self._evaluateLine(diags[1])
        return evaluations
    
    def gameOver(self, n):
        for i in range(SIZE):
            if sum(self._states[n].getRow(i)) == SIZE or sum(self._states[n].getRow(i)) == -SIZE:
                return True
            if sum(self._states[n].getCol(i)) == SIZE or sum(self._states[n].getCol(i)) == -SIZE:
                return True
        diags = self._states[n].getDiags()
        if sum(diags[0]) == SIZE or sum(diags[0]) == -SIZE:
            return True
        if sum(diags[1]) == SIZE or sum(diags[1]) == -SIZE:
            return True
        return n == SIZE * SIZE
    
    def getWinner(self, n):
        for i in range(SIZE):
            if sum(self._states[n].getRow(i)) == SIZE:
                return 1
            if sum(self._states[n].getRow(i)) == -SIZE:
                return -1
            if sum(self._states[n].getCol(i)) == SIZE:
                return 1
            if sum(self._states[n].getCol(i)) == -SIZE:
                return -1
        diags = self._states[n].getDiags()
        if sum(diags[0]) == SIZE:
            return 1
        if sum(diags[0]) == -SIZE:
            return -1
        if sum(diags[1]) == SIZE:
            return 1
        if sum(diags[1]) == -SIZE:
            return -1  
        return 0

class TicTacToe:
    def __init__(self):
        self._gameState = GameState()
        # Indicates index of current state.
        self._index = 0
        # Players are represented as 1 or -1 where 1 is user and -1 is AI.
        self._turn = 1
    
    def getGameState(self):
        return self._gameState
    
    def makeMove(self, move):
        if move not in self._gameState.getAvailableMoves(self._index):
            return False
        
        self._gameState.makeMove(self._index, self._turn, move)
        self._index += 1
        if self._turn == 1:
            self._turn = -1
        else:
            self._turn = 1
        return True
    
    def whoseTurn(self):
        return self._turn
    
    def printGame(self):
        currentBoard = self._gameState.getBoard(self._index)
        for i in range(SIZE):
            print(currentBoard.getRow(i))
    
    def gameOver(self):
        return self._gameState.gameOver(self._index)
    
    def getWinner(self):
        return self._gameState.getWinner(self._index)
    
    def getIndex(self):
        return self._index
    
    def setIndex(self, index):
        self._index = index
    
    def setTurn(self, player):
        self._turn = player