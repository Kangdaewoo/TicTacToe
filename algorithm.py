class Algorithm:
    def __init__(self):
        pass
    
    def findBestMove(self, gameState, index, player):
        return self.minimaxSearch(gameState, index, player)[0]
    
    def minimaxSearch(self, gameState, index, player):
        """
        Recursively find a best move that gives the most evaluation.
        """
        if gameState.gameOver(index):
            # (11 - index) gives more points on the evaluation of early finished games.
            return (None, gameState.evaluateState(index) * (11 - index))
        
        nextPlayer = 0
        if player == 1:
            nextPlayer = -1
        else:
            nextPlayer = 1
        
        bestMove = None
        bestEvaluation = 0
        if player == 1:
            bestEvaluation = float('-inf')
        else:
            bestEvaluation = float('inf')
        
        for move in gameState.getAvailableMoves(index):
            gameState.makeMove(index, player, move)
            temp, evaluation = self.minimaxSearch(gameState, index + 1, nextPlayer)
            if (player == 1 and evaluation >= bestEvaluation) or (player == -1 and evaluation <= bestEvaluation):
                bestMove = move
                bestEvaluation = evaluation
        
        if bestMove == None:
            if player == 1:
                bestEvaluation = float('inf')
            else:
                bestEvaluation = float('-inf')
        return (bestMove, bestEvaluation)