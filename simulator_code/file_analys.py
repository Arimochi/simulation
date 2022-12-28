#!/usr/bin/env python3
# coding: utf-8
import numpy as np
import os
import csv
import matplotlib.pyplot as plt

#変更箇所
number_of_cars = 300
#dir = './result'
dir = './fake_result'
#output_name = "result average.csv"
output_name = "fake_result average.csv"
#folder_name = "result"
folder_name = "fake_result"

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
        data_list = line.replace("¥n","").split(",")
        duration_list1.append(int(data_list[0]))
        distance_list1.append(float(data_list[1]))
        line_counter += 1
    infile1.close()
    
    if counter == 0:
        for i in range(number_of_cars):
            duration_list.append(duration_list1[i])
        for i in range(number_of_cars):
            distance_list.append(distance_list1[i])
    else:
        #移動時間
        for i in range(number_of_cars):
            duration_all_list.append(duration_list[i] + duration_list1[i])
        duration_list.clear()
        for i in range(number_of_cars):
            duration_list.append(duration_all_list[i])
        duration_all_list.clear()
        #移動距離
        for i in range(number_of_cars):
            distance_all_list.append(distance_list[i] + distance_list1[i])
        distance_list.clear()
        for i in range(number_of_cars):
            distance_list.append(distance_all_list[i])
        distance_all_list.clear()
    counter += 1
    #print(duration_list1)
    #print(distance_list1)


for i in range(number_of_cars):
    duration_avg_list.append(int(duration_list[i]/(counter)))
for i in range(number_of_cars):
    distance_avg_list.append(round(distance_list[i]/(counter),1))
    
#print("移動時間")
#print(duration_list)
#print(duration_avg_list)
#print("移動距離")
#print(distance_list)
#print(distance_avg_list)
plt.hist(distance_avg_list, bins=50, rwidth=0.9, color='b')
plt.savefig(folder_name  + '/' + "総移動距離の平均.png")
plt.clf()

plt.hist(duration_avg_list, bins=50, rwidth=0.9, color='b')
plt.savefig(folder_name  + '/' + "ゴールタイムの平均.png")
plt.clf()

with open(folder_name  + '/' + output_name, 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(len(duration_avg_list)):
        writer.writerow([duration_avg_list[i],distance_avg_list[i]])