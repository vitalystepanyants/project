# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:28:30 2020

@author: dasha
"""
import RPi.GPIO as GPIO # Импортируем нужный модуль
import time

mode = GPIO.getmode() # Проверяем метод нумерации
GPIO.setmode(GPIO.BOARD) # Устанавливаем метод BOARD, если не установлен ранее

chan_list_left = (11,13,15,16) # Управляющие пины для левой руки
chan_list_right = (18,22,29,31) # Управляющие пины для правой руки                                   

GPIO.output(chan_list_left, GPIO.LOW) # на левую руку на всё подается LOW
GPIO.output(chan_list_right, GPIO.LOW) # на правую руку на всё подается LOW

muxChannel=[[0,0,0,0], # channel 0 
            [1,0,0,0], # channel 1 
            [0,1,0,0], # channel 2 
            [1,1,0,0], # channel 3 
            [0,0,1,0], # channel 4 
            [1,0,1,0], # channel 5 
            [0,1,1,0], # channel 6 
            [1,1,1,0], # channel 7 
            [0,0,0,1], # channel 8 
            [1,0,0,1], # channel 9 
            [0,1,0,1], # channel 10 
            [1,1,0,1], # channel 11 
            [0,0,1,1], # channel 12 
            [1,0,1,1], # channel 13 
            [0,1,1,1], # channel 14 
            [1,1,1,1]] # channel 15 
 
for i in range(16):
    GPIO.output(chan_list_left, muxChannel(i))
    GPIO.output(chan_list_right, muxChannel(i))
    time.sleep(1)    
    
GPIO.cleanup() # Очистка 