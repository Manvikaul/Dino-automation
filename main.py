# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:00:22 2020

@author: DELL
"""

import pyautogui
from PIL import Image, ImageGrab
import time
#from numpy import asarray

def hit(key):
    pyautogui.press(key)
    return
    
def collision(data):
    
    #rectangle for birds
    #for i in range(190,240):
    #    for j in range(250,370):
    #        if data[i,j]<100:
    #             hit('down')
    #             return 
    #rectangle for cactus
    for i in range(275,295):
            for j in range(370,450):
                if data[i,j]<100:
                    hit('up')
                    return             
    return 
 
if __name__=="__main__":
    print("Game starting in 5 seconds")
    time.sleep(5)
    #hit('up')
    while True:
        image=ImageGrab.grab().convert('L') #L to change to  grayscale
        data=image.load()
        collision(data)
            
        #print(asarray(image))
'''        
        #rectangle for birds
        #for i in range(190,240):
        #    for j in range(250,370):
        #        data[i,j]=180
      
        #rectangle for cactus
        for i in range(180,210):
            for j in range(370,450):
                data[i,j]=0
                

                
        image.show()
        break
'''        