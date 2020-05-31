# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:00:22 2020

@author: DELL
"""

import pyautogui
from PIL import ImageGrab
import time
#from numpy import asarray

def hit(key):
    pyautogui.press(key)
    return                
    
def collision(data):
    for i in range(380,400):
            for j in range(370,450):
                if data[i,j]<100 and data[180,120]==255:
                    hit('up')
                    return   
                elif (data[i,j]>100 and data[180,120]==0):
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
'''      
        #TESTING
  
        #data[180,120]=255
        #print(data[200,500])
            
        #print(asarray(image))
        
        #rectangle for birds
        #for i in range(190,240):
        #    for j in range(250,370):
        #        data[i,j]=180
      
        #rectangle for cactus
        for i in range(50,150):
            for j in range(370,450):
                print(data[i,j])
                

                
        image.show()
        break        
'''       