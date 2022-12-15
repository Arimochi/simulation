#!/usr/bin/env python3
# coding: utf-8
import numpy as np

### read data ###
#infilename1 = "result grid3x3.net.xml rate=1.0cars600obstacles10fake_cars0fake_obs0.csv"
infilename1 = "result grid5x5.net.xml rate=1.0cars600obstacles10fake_cars0fake_obs0.csv"
#infilename2 = "result grid3x3.net.xml rate=1.0cars600obstacles10fake_cars3fake_obs1.csv"
infilename2 = "result grid5x5.net.xml rate=1.0cars600obstacles10fake_cars3fake_obs1.csv"

duration_list1 = []
distance_list1 = []
infile1 = open(infilename1,"r",encoding="utf-8")
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

duration_list1_sorted = sorted(duration_list1)[int(len(duration_list1)/2):]
distance_list1_sorted = sorted(distance_list1)[int(len(duration_list1)/2):]
duration_list_sorted1 = []
distance_list_sorted1 = []
for i in range(300):
    duration_list_sorted1.append((np.random.choice(duration_list1_sorted)))
    distance_list_sorted1.append((np.random.choice(distance_list1_sorted)))

duration_list2 = []
distance_list2 = []
infile2 = open(infilename2,"r",encoding="utf-8")
line_counter = 0
for line in infile2:
    if line_counter == 0:
        line_counter += 1
        continue
    if line[0] == "#":
        break

    data_list = line.replace("¥n","").split(",")
    duration_list2.append(int(data_list[0]))
    distance_list2.append(float(data_list[1]))
    line_counter += 1
infile2.close()

duration_list2_sorted = sorted(duration_list2)[int(len(duration_list1)/2):]
distance_list2_sorted = sorted(distance_list2)[int(len(duration_list1)/2):]
duration_list_sorted2 = []
distance_list_sorted2 = []
for i in range(300):
    duration_list_sorted2.append((np.random.choice(duration_list2_sorted)))
    distance_list_sorted2.append((np.random.choice(distance_list2_sorted)))

### main calculation ###

# duration's U
#移動時間の転倒数
U = 0
for j in range(len(duration_list_sorted2)):
    for k in range(len(duration_list_sorted1)):
        if duration_list_sorted2[j] > duration_list_sorted1[k]:
            U += 1

print("duration:",U,"(average:",len(duration_list_sorted1)*len(duration_list_sorted2)/2,")")

# distance's U
#移動距離の転倒数
U = 0
for j in range(len(distance_list_sorted2)):
    for k in range(len(distance_list_sorted1)):
        if distance_list_sorted2[j] > distance_list_sorted1[k]:
            U += 1

print("distance:",U,"(average:",len(distance_list_sorted1)*len(distance_list_sorted2)/2,")")
