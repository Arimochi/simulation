#!/usr/bin/env python3
# coding: utf-8
import numpy as np

infilename1 = "result grid5x5.net.xml rate=1.0cars100obstacles10fake_cars0fake_obs0.csv"
infilename2 = "result grid5x5.net.xml rate=1.0cars100obstacles10fake_cars1fake_obs1.csv"

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

duration_list = []
duration_avg = []
for i in range(len(duration_list1)):
    duration_list.append(duration_list1[i] + duration_list2[i])
    duration_avg.append(duration_list[i]/2)

#print(duration_list1)
#print(duration_list2)
print(duration_list)
print(duration_avg)