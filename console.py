import game as Game
import algorithm as Algorithm


class Console:
    def __init__(self):
        pass
    
    def run(self):
        game = Game.TicTacToe()
        alg = Algorithm.Algorithm()
        
        print('Welcome to TicTacToe')
        while True:
            game.printGame()
            
            breaker = False
            while not breaker:
                moveStr = input('\nMake your move! ex) "1 3" where 1 is row and 3 is column.\n')
                move = (int(moveStr[0]), int(moveStr[2]))
                print('You chose ({0}, {1})!'.format(move[0], move[1]))
                if game.makeMove(move):
                    breaker = True
                else:
                    print('Invalid move!')
                game.printGame()
            
            if game.gameOver():
                break
            
            print('\nAI is thinking...')
            bestMove = alg.findBestMove(game.getGameState(), game.getIndex(), -1)
            print('AI chose ({0}, {1})!'.format(bestMove[0], bestMove[1]))
            game.makeMove(bestMove)
            
            if game.gameOver():
                break
        
        if game.getWinner() == 1:
            print("You've won!")
        elif game.getWinner() == -1:
            print("You've lost!")
        else:
            print('Game tied!')     


if __name__ == '__main__':
    Console().run()