#!/usr/bin/env python3
# coding: utf-8
import numpy as np
import os
import csv
import matplotlib.pyplot as plt

dir1 = "./result(csv)"
dir2 = "./fake_result(csv)"

U_duration_list = []
U_distance_list = []
U_duration_avg = 0
U_distance_avg = 0
U_duration_std = 0
U_distance_std = 0

count = 0
#サンプル数
number_of_cars = 300
half_number_of_cars = int(number_of_cars/2)

for file_name1 in os.listdir(dir1):
    file_path1 = os.path.join(dir1,file_name1)
    #print(file_path1)

    duration_list1 = []
    distance_list1 = []
    infile1 = open(file_path1,"r",encoding="utf-8")
    line_counter = 0
    for line in infile1:
        data_list = line.replace("¥n","").split(",")
        duration_list1.append(int(data_list[0]))
        distance_list1.append(float(data_list[1]))
        line_counter += 1
    infile1.close()

    duration_list1_sorted = sorted(duration_list1)[int(len(duration_list1)/2):]
    distance_list1_sorted = sorted(distance_list1)[int(len(duration_list1)/2):]
    duration_list_sorted1 = []
    distance_list_sorted1 = []
    for i in range(half_number_of_cars):
        duration_list_sorted1.append((np.random.choice(duration_list1_sorted)))
        distance_list_sorted1.append((np.random.choice(distance_list1_sorted)))

    file_name2 = os.listdir(dir2)[count]
    file_path2 = os.path.join(dir2,file_name2)
    #print(file_path2)

    duration_list2 = []
    distance_list2 = []
    infile2 = open(file_path2,"r",encoding="utf-8")
    line_counter = 0
    for line in infile2:
        data_list = line.replace("¥n","").split(",")
        duration_list2.append(int(data_list[0]))
        distance_list2.append(float(data_list[1]))
        line_counter += 1
    infile2.close()

    duration_list2_sorted = sorted(duration_list2)[int(len(duration_list1)/2):]
    distance_list2_sorted = sorted(distance_list2)[int(len(duration_list1)/2):]
    duration_list_sorted2 = []
    distance_list_sorted2 = []
    for i in range(half_number_of_cars):
        duration_list_sorted2.append((np.random.choice(duration_list2_sorted)))
        distance_list_sorted2.append((np.random.choice(distance_list2_sorted)))

    U = 0
    for j in range(len(duration_list_sorted2)):
        for k in range(len(duration_list_sorted1)):
            if duration_list_sorted2[j] > duration_list_sorted1[k]:
                U += 1
    U_duration_list.append(U)

    U = 0
    for j in range(len(distance_list_sorted2)):
        for k in range(len(distance_list_sorted1)):
            if distance_list_sorted2[j] > distance_list_sorted1[k]:
                U += 1
    U_distance_list.append(U)

    count += 1

#print(U_duration_list)
#print(U_distance_list)
U_duration_avg = np.mean(U_duration_list)
U_distance_avg = np.mean(U_distance_list)
U_duration_std = np.std(U_duration_list)
U_distance_std = np.std(U_distance_list)
print("転倒数の平均")
print("duration : " + str(int(U_duration_avg)))
print("distance : " + str(int(U_distance_avg)))
print("転倒数の標準偏差")
print("duration : " + str(int(U_duration_std)))
print("distance : " + str(int(U_distance_std)))
