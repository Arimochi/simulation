#!/usr/bin/env python3
# coding: utf-8
import numpy as np
import os

dir = './result'
#count_file = 0
counter = 0
duration_list = []
duration_all_list = []
duration_avg_list = []
distance_list = []
distance_all_list = []
distance_avg_list = []

for file_name in os.listdir(dir):
    file_path = os.path.join(dir,file_name)
    print(file_path)
    #if os.path.isfile(file_path):
        #count_file += 1
    
    duration_list1 = []
    distance_list1 = []
    infile1 = open(file_path,"r",encoding="utf-8")
    line_counter = 0
    for line in infile1:
        if line_counter == 0:
            line_counter += 1
            continue
        if line[0] == "#":
            break

        data_list = line.replace("¥n","").split(",")
        duration_list1.append(int(data_list[0]))
        distance_list1.append(float(data_list[1]))
        line_counter += 1
    infile1.close()
    
    if counter == 0:
        for i in range(len(duration_list1)):
            duration_list.append(duration_list1[i])
        for i in range(len(distance_list1)):
            distance_list.append(distance_list1[i])
    else:
        #移動時間
        for i in range(len(duration_list1)):
            duration_all_list.append(duration_list[i] + duration_list1[i])
        duration_list.clear()
        for i in range(len(duration_all_list)):
            duration_list.append(duration_all_list[i])
        duration_all_list.clear()
        #移動距離
        for i in range(len(distance_list1)):
            distance_all_list.append(distance_list[i] + distance_list1[i])
        distance_list.clear()
        for i in range(len(distance_all_list)):
            distance_list.append(distance_all_list[i])
        distance_all_list.clear()
    counter += 1
    #print(duration_list1)
    print(distance_list1)


for i in range(len(duration_list)):
    duration_avg_list.append(int(duration_list[i]/counter))
for i in range(len(distance_list)):
    distance_avg_list.append(round(distance_list[i]/counter,1))
    
#print("移動時間")
#print(duration_list)
#print(duration_avg_list)
print("移動距離")
print(distance_list)
print(distance_avg_list)