
class MyLed():
    def __init__(self, board, cor, porta):
        self.board = board
        self.cor = cor
        self.porta = porta

    def LightsON(self):
        self.board.digital[self.porta].write(1)
    
    def LightsOFF(self):
        self.board.digital[self.porta].write(1)