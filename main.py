import cv2
import numpy as np
from pyfirmata import Arduino

class MyLed():
    def __init__(self, board, cor, porta):
        self.board = board
        self.cor = cor
        self.porta = porta

    def LightsON(self):
        self.board.digital[self.porta].write(1)
    
    def LightsOFF(self):
        self.board.digital[self.porta].write(0)

class Screen():
    def __init__(self, catch):
        self.catch = catch
        _,self.img = self.catch.read()
        h,w,_ = self.img.shape
        offset = 100
        campo = self.img[offset:h-offset,offset:w-offset]
        cv2.rectangle(self.img,(offset,offset),(w-offset,h-offset),(255,0,0),3)

        corMediaLinha = np.average(campo,axis=0)
        corMedia = np.average(corMediaLinha,axis=0)
        r,g,b = int(corMedia[2]),int(corMedia[1]),int(corMedia[0])

        return r, g, b
    
    def finalizar(self):
        cv2.imshow('Img',self.img)
        cv2.waitKey(1)


port = 'COM7'
board = Arduino(port)

red = MyLed(board, 'vermelho', 5)
green = MyLed(board, 'verde', 6)
blue = MyLed(board, 'azul', 7)

cap = cv2.VideoCapture(0)
janela = Screen(cap)
r = b = g = 0

while True:
    
    janela.configurar()

    if b>g and b>r:
        blue.LightsON()

    elif r>g and r>b:
        red.LightsON()

    elif g>b and g>r:
        green.LightsON()

    else:
        red.LightsOFF()
        green.LightsOFF()
        blue.LightsOFF()


    