#!/usr/bin/env python3
# coding: utf-8

### import modules ###
import os
import numpy as np
import matplotlib.pyplot as plt

#回数
times = 2
num = 0
ns = []
file_list = []
infile = "回目"
dir = './result(csv)'
#dir = './fake_result(csv)'

#実行
while(True):
    print(str(num + 1) + "回目")
    file_list.append(str(num + 1) + infile)
    a = np.random.randint(12345,123456)
    while(True):
        if a not in ns:
            ns.append(a)
            os.system("python grid_simulator.py " + str(a))
            num += 1
            break
        else:
            a = np.random.randint(12345,123456)
    if len(os.listdir(dir)) == 50:
        print("### 50回目終了 ###")
    if len(os.listdir(dir)) == times:
        print("### 100回目終了 ###")
        break
    #os.system("python argv.py " + str(a))

#print(file_list)
