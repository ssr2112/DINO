# from email.mime import image
# from socket import if_indextoname
import pyautogui
from PIL import Image, ImageGrab
import time
# from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)
    
def isCollide(data):
    #image is in the form of a 2D array
    #at given location if black pixel(<100) will come, up key will be fired
    for i in range(310,415):
            for j in range(600,660):
                if data[i,j]<100:
                    return True     #up is used for pressing up key in pyautogui
    return False

if __name__=='__main__':
    print("Hey Dino game is about to start in 3 sec... Press up key to play")
    time.sleep(3)
    hit('up')
    while True:
        # .convert('L') to take blace & white image(grey scale image) as processing it is easier than clour image
        image= ImageGrab.grab().convert('L')
        data= image.load()
        if isCollide(data):
            hit('up')

        # print(asarray(image))
        for i in range(500,650):
            for j in range(550,720):
                data[i,j]=0

        # image.show()
        # break
