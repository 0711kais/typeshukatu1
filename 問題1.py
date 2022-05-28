# -*- coding: utf-8 -*-
"""
Created on Sun May 29 02:06:55 2022

@author: syuny
"""

for num in range(1, 101):
    string = ''

    # ここから記述
    string = num    #stringに1から100までの値を代入
    
    if num % 3 ==0:
        string ='Fizz' #3の倍数の時、Fizzを出力
        
    if num % 5 ==0:
        string ='Buzz' #5の倍数の時、Fizzを出力
        
    if num % 15 ==0:
        string ='FizzBuzz'  #15の倍数の時、Fizzを出力
    
    # ここまで記述

    print(string)