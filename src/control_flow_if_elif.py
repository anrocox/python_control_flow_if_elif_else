#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2014

@author: anroco

How to use the control structure elif in Python?

¿Cómo usar la estructura de control elif de Python?
'''

#elif is the same as if, but it must come after if and before else. It can come
#at the end.

#create a integer
n = 30

#check if n is greater than 100
if n > 100:
    print('the value of n is greater than 100')
#check if n is greater than 50 and less than or equal to 100
elif n > 50 and n <= 100:
    print('the value of n is greater than 50 and less than or equal to 100')
#check if n is greater than 0 and less than or equal to 50
elif n > 0 and n <= 50:
    print('the value of n is greater than 0 and less than or equal to 50')
else:
    print('the value of n less than or equal to 0')
