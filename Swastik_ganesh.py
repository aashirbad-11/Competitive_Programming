# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 00:54:11 2020

@author: aashirbad JAY
"""

x = int(input('Enter the length : '))
print('*', end='')
for i in range((x-3)//2):
    print(' ', end='')
for i in range((x+1)//2):
    print('*', end ='')
print()

for x_ in range((x -3)//2):
    print('*', end='')
    for i in range( int((x-3)/2)):
        print(' ', end='')
    print('*')
    
    
for i in range(x):
    print('*', end='')
print()


for i in range((x-3)//2):
    for k in range((x-3)//2 + 1):
        print(' ', end='')
    print('*', end='')
    for k in range((x-3)//2):
        print(' ', end='')
    print('*', end='')
    print()
    
for i in range((x + 1)//2):
    print('*', end ='')
print()