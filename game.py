class Board:
    def __init__(self):
        self._cells = [[0, 0, 0], 
                       [0, 0, 0], 
                       [0, 0, 0]]
    
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
        for i in range(3):
            toReturn.append(self._cells[i][n])
        return toReturn
    
    def getDiags(self):
        """
        Returns diagonals.
        """
        toReturn = [[], []]
        for i in range(3):
            toReturn[0].append(self._cells[i][i])
            toReturn[1].append(self._cells[i][2 - i])
        return toReturn
    
    def makeMove(self, player, move):
        self._cells[move[0]][move[1]] = player
    
    def copy(self):
        newBoard = Board()
        for x in range(3):
            for y in range(3):
                newBoard._cells[x][y] = self._cells[x][y]
        return newBoard
    
    def getNeutrals(self):
        toReturn = []
        for x in range(3):
            for y in range(3):
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
        for i in range(3):
            if line[i] == 1:
                players[1] += 1
            elif line[i] == -1:
                players[0] += 1
        if players[0] == 3:
            return -300
        elif players[1] == 3:
            return 300
        if players[0] == 0:
            return players[1] * 1
        elif players[1] == 0:
            return players[0] * -1
        return 0
    
    def evaluateState(self, n):
        evaluations = 0
        for i in range(3):
            evaluations += self._evaluateLine(self._states[n].getRow(i))
        for i in range(3):
            evaluations += self._evaluateLine(self._states[n].getCol(i))
        diags = self._states[n].getDiags()
        evaluations += self._evaluateLine(diags[0])
        evaluations += self._evaluateLine(diags[1])
        return evaluations
    
    def gameOver(self, n):
        for i in range(3):
            if sum(self._states[n].getRow(i)) == 3 or sum(self._states[n].getRow(i)) == -3:
                return True
            if sum(self._states[n].getCol(i)) == 3 or sum(self._states[n].getCol(i)) == -3:
                return True
        diags = self._states[n].getDiags()
        if sum(diags[0]) == 3 or sum(diags[0]) == -3:
            return True
        if sum(diags[1]) == 3 or sum(diags[1]) == -3:
            return True
        return n == 9
    
    def getWinner(self, n):
        for i in range(3):
            if sum(self._states[n].getRow(i)) == 3:
                return 1
            if sum(self._states[n].getRow(i)) == -3:
                return -1
            if sum(self._states[n].getCol(i)) == 3:
                return 1
            if sum(self._states[n].getCol(i)) == -3:
                return -1
        diags = self._states[n].getDiags()
        if sum(diags[0]) == 3:
            return 1
        if sum(diags[0]) == -3:
            return -1
        if sum(diags[1]) == 3:
            return 1
        if sum(diags[1]) == -3:
            return -1  
        return 0

class TicTacToe:
    def __init__(self):
        self._gameState = GameState()
        self._index = 0
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
        for i in range(3):
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