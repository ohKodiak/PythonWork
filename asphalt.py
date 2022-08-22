#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 00:28:18 2022

@author: VPDiddy
"""
density = open('sample_ asphalt_densities.txt','r') 
data = density.read()

datalist = []
datal = data.split('\n')
for i in datal:
    if i == '':
        continue
    else:
        datalist.append(float(i))

summ = 0
counter = 0
for i in datalist:
    summ += i
    counter += 1

average = summ / counter
print(average)
print(counter)
    

    
    

        



    


