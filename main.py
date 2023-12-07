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

class IdentificarCores():
    def __init__(self):
        pass
    
    def vermelho(self, r, g, b):
        if r>g and r>b :
            return True
        else:
            return False
    
    def azul(self, r, g, b):
        if b>g and b>r :
            return True
        else:
            return False
    
    def verde(self, r, g, b):
        if g>b and g>r :
            return True
        else:
            return False
    
port = 'COM5'
board = Arduino(port)

red = MyLed(board, 'vermelho', 5)
green = MyLed(board, 'verde', 6)
blue = MyLed(board, 'azul', 7)

cap = cv2.VideoCapture(0)
i = IdentificarCores()

while True:
    _,img = cap.read()
    h,w,_ = img.shape
    offset = 100
    campo = img[offset:h-offset,offset:w-offset]
    cv2.rectangle(img,(offset,offset),(w-offset,h-offset),(255,0,0),3)
    corMediaLinha = np.average(campo,axis=0)
    corMedia = np.average(corMediaLinha,axis=0)
    r,g,b = int(corMedia[2]),int(corMedia[1]),int(corMedia[0])

    if i.azul(r, g, b):
        blue.LightsON()
        red.LightsOFF()
        green.LightsOFF()

    elif i.vermelho(r, g, b):
        red.LightsON()
        green.LightsOFF()
        blue.LightsOFF()

    elif i.verde(r, g, b):
        green.LightsON()
        red.LightsOFF()
        blue.LightsOFF()

    else:
        red.LightsOFF()
        green.LightsOFF()
        blue.LightsOFF()
    
    cv2.imshow('Img',img)
    cv2.waitKey(1)


    