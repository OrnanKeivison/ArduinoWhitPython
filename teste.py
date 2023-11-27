from pyfirmata import Arduino,SERVO
from time import sleep
from Leds import MyLed

port = 'COM6'
board = Arduino(port)

yellow = MyLed(board, 'amarelo', 6)
red = MyLed(board, 'vermelho', 7)
green = MyLed(board, 'verde', 8)

red.LightsON
sleep(2)
red.LightsOFF

yellow.LightsON
sleep(2)
yellow.LightsOFF

green.LightsON
sleep(2)
green.LightsOFF