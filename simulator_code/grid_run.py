#!/usr/bin/env python3
# coding: utf-8

### import modules ###
import os
import numpy as np
import matplotlib.pyplot as plt

#回数
times = 100
num = 0
ns = []
file_list = []
file_dic = {}
#infile = "result grid5x5.net.xml rate=1.0cars100obstacles10fake_cars0fake_obs0.csv"
infile = "回目"
dir = './result'
#dir = './fake_result'

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
    if len(os.listdir(dir)) == times:
        break
    #os.system("python argv.py " + str(a))
    #file_dic[num] = "result grid5x5.net.xml rate=1.0cars100obstacles10fake_cars0fake_obs0.csv"

#print(file_list)
#print(file_list[1])
#print(file_dic)
