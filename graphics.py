from tkinter import *
from game import TicTacToe
from algorithm import Algorithm


game = TicTacToe()
algorithm = Algorithm()
frames = [[None, None, None],
          [None, None, None],
          [None, None, None]]


class Cell(Frame):
    def __init__(self, cellNumber, buttonType, color):
        """
        cellNumber: '1 2' where 1 is row and 2 is column.
        """
        super().__init__(width=100, height=100)
        self._canvas = Canvas(self, width=100, height=100, bg=color)
        self._canvas.pack()
        self._canvas.bind(buttonType, self.drawO)
        
        self._cellNumber = cellNumber
        
        self._coordinatesRect1 = [15, 25, 25, 15, 95, 85, 85, 95]
        self._coordinatesRect2 = [85, 15, 95, 25, 25, 95, 15, 85]
        self._objects = []
        
        self.message = message
    
    def deleteObjects(self):
        for ob in self._objects:
            self._canvas.delete(ob)
    
    def drawX(self):
        rect1 = self._canvas.create_polygon(self._coordinatesRect1, fill='black')
        rect2 = self._canvas.create_polygon(self._coordinatesRect2, fill='black')
        self._objects.append(rect1)
        self._objects.append(rect2)
    
    def drawO(self, event):
        if game.gameOver():
            for x in range(3):
                for y in range(3):
                    frames[x][y].deleteObjects()
            game.setIndex(0)
            game.setTurn(1)
            return
        
        if not game.makeMove(self._cellNumber):
            self.message.set('Invalid move!')
            return
        
        oval = self._canvas.create_oval(10, 95, 95, 10, outline='black', width=10)
        self._objects.append(oval)
        self.message.set('AI is thinking')


if __name__ == '__main__':
    tk = Tk()
    
    message = StringVar()
    message.set('Welcome to TicTacToe!')
    label = Label(tk, textvariable=message)
    label.grid(row=0, column=0, columnspan=3, sticky=N)
    
    color = 'gray'
    for x in range(3):
        for y in range(3):
            newFrame = Cell((x, y), '<Button-1>', color)
            newFrame.grid(row=x+1, column=y)
            frames[x][y] = newFrame
            if color == 'gray':
                color = 'white'
            else:
                color = 'gray'
            newFrame.message = message
    
    while True:
        if game.whoseTurn() == -1:
            if not game.gameOver():
                move = algorithm.findBestMove(game.getGameState(), game.getIndex(), game.whoseTurn())
                game.makeMove(move)
                frames[move[0]][move[1]].drawX()
                message.set('Make your move!')
        if game.gameOver():
            if game.getWinner() == 1:
                message.set("You've won!")
            elif game.getWinner() == -1:
                message.set("You've lost!")
            else:
                message.set("Game tied!")
        
        tk.update()