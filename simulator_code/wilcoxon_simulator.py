#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import datetime

repetition=100000
n1=50
n2=50

folder_name = "wilcoxon_sample"

U_list=[]
for i in range(repetition):
    if i % 1000 == 0:
        print(i,datetime.datetime.now())
    sampleX=[]
    sampleY=[]

    #ランダムサンプリング
    for j in range(n1):
        sampleX.append(np.random.pareto(1.0))
    sampleX_sorted=sorted(sampleX)

    for j in range(n2):
        sampleY.append(np.random.pareto(1.0))
    sampleY_sorted=sorted(sampleY)

    U=0
    for j in range(n2):
        for k in range(n1):
            if sampleX_sorted[k]>sampleY_sorted[j]:
                U+=1
    U_list.append(U)

print(repetition,datetime.datetime.now())
n,bins,patches=plt.hist(U_list,bins=n1*n2)

accum=0.0
for i in range(len(n)):
    accum += float(n[i])
    if (accum/repetition) > 0.025:
        print(n[i],bins[i])
        lower_bound=bins[i]
        y_val1=n[i]
        break
accum=0.0
for i in range(len(n)):
    accum += float(n[len(n)-1-i])
    if (accum/repetition) > 0.025:
        print(n[len(n)-1-i],bins[len(n)-1-i+1])
        upper_bound=bins[len(n)-1-i+1]
        y_val2=n[len(n)-1-i]
        break

plt.axvline(x=lower_bound,color="red",linestyle="--")
plt.axvline(x=upper_bound,color="red",linestyle="--")
plt.text(x=lower_bound,y=y_val1,s=str(lower_bound),color="red",fontsize=12)
plt.text(x=upper_bound,y=y_val2,s=str(upper_bound),color="red",fontsize=12)
plt.savefig(folder_name + '/' + "wilcoxon_n="+str(n1)+"repetiton="+str(repetition)+".png")
plt.clf()
