#!/usr/bin/env python3
# coding: utf-8
import numpy as np
import os
import csv
import matplotlib.pyplot as plt

#変更箇所
number_of_cars = 300
dir = './result'
#dir = './fake_result'
output_name1 = "result average.csv"
output_name2 = "result std.csv"
#output_name1 = "fake_result average.csv"
#output_name2 = "fake_result std.csv"
folder_name = "result"
#folder_name = "fake_result"

#count_file = 0
counter = 0

duration_all_list = []
duration_avg_list = []
distance_all_list = []
distance_avg_list = []
duration_std = []
distance_std = []

for file_name in os.listdir(dir):
    file_path = os.path.join(dir,file_name)
    print(file_path)
    
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

    duration_all_list.append(duration_list1)
    distance_all_list.append(distance_list1)

#平均の計算
duration_avg_list = np.mean(duration_all_list, axis=0)
duration_avg_list = np.round(duration_avg_list, 1)
distance_avg_list = np.mean(distance_all_list, axis=0)
distance_avg_list = np.round(distance_avg_list, 1)
#標準偏差の計算
duration_std = np.std(duration_all_list, axis=0)
duration_std = np.round(duration_std, 1)
distance_std = np.std(distance_all_list, axis=0)
distance_std = np.round(distance_std, 1)


#print(duration_avg_list)
#print(distance_avg_list)
#print(duration_std)
#print(distance_std)

plt.hist(distance_avg_list, bins=50, rwidth=0.9, color='b')
plt.savefig(folder_name  + '/' + "総移動距離の平均.png")
plt.clf()

plt.hist(distance_std, bins=50, rwidth=0.9, color='b')
plt.savefig(folder_name  + '/' + "総移動距離の標準偏差.png")
plt.clf()

plt.hist(duration_avg_list, bins=50, rwidth=0.9, color='b')
plt.savefig(folder_name  + '/' + "ゴールタイムの平均.png")
plt.clf()

plt.hist(distance_std, bins=50, rwidth=0.9, color='b')
plt.savefig(folder_name  + '/' + "ゴールタイムの標準偏差.png")
plt.clf()

with open(folder_name  + '/' + output_name1, 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(len(duration_avg_list)):
        writer.writerow([duration_avg_list[i],distance_avg_list[i]])

with open(folder_name  + '/' + output_name2, 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(len(duration_std)):
        writer.writerow([duration_std[i],distance_std[i]])
    
"""if counter == 0:
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
    duration_avg_list.append(int(duration_list[i]/counter))
for i in range(number_of_cars):
    distance_avg_list.append(round(distance_list[i]/counter,1))
    
#print("移動時間")
print(duration_list)
print(duration_avg_list)
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
        writer.writerow([duration_avg_list[i],distance_avg_list[i]])"""