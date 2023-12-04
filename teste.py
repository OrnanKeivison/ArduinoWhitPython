from pyfirmata import Arduino,SERVO
from time import sleep

class MyLed():
    def __init__(self, board, cor, porta):
        self.board = board
        self.cor = cor
        self.porta = porta

    def LightsON(self):
        self.board.digital[self.porta].write(1)
    
    def LightsOFF(self):
        self.board.digital[self.porta].write(0)

port = 'COM7'
board = Arduino(port)

yellow = MyLed(board, 'amarelo', 5)
red = MyLed(board, 'vermelho', 4)
green = MyLed(board, 'verde', 6)
blue = MyLed(board, 'azul', 7)

while True:
    red.LightsON()
    sleep(2)
    red.LightsOFF()

    yellow.LightsON()
    sleep(2)
    yellow.LightsOFF()

    green.LightsON()
    sleep(2)
    green.LightsOFF()

    blue.LightsON()
    sleep(2)
    blue.LightsOFF()