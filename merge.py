#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 22:06:26 2018
OBJECTIVE: USE WORDS AND SENTENCES MATRICES TO COMPUTER WORDS/SENTENCES MATRIX
@author: arghanandan
"""

import pandas as pd

def calAvg(avg,word,sent):
    for i in range(len(avg)):
        if sent[i]!=0:
            avg[i]=word[i]/sent[i]
    return avg

for i in range(8,17):
    df_w=pd.read_csv("words/"+str(i+1)+".csv")
    df_s=pd.read_csv("sents/"+str(i+1)+".csv")
    cols=["character"] + list(df_w.columns[1:])
    df_avg=pd.DataFrame(columns=cols)
    for j in df_w.index:
        df_avg.loc[j]=[df_w.iloc[j,0]]+ [0] * len(df_w.index)
        df_avg.iloc[j,1:]=calAvg(df_avg.iloc[j,1:],df_w.iloc[j,1:],df_s.iloc[j,1:])
    df_avg.to_csv("avg/avg"+str(i+1)+".csv")
    print("Averages written to "+"avg/avg"+str(i+1)+".csv")