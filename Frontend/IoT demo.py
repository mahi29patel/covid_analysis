#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
df = pd.read_csv(r'C:\Users\margi\Downloads\patients_data.csv')

#print(df.tail())


# In[25]:


length= len(df.index)
#print(length)
for i in range (length):
    if df.SpO2[i]<90:
        print(i, "Extremely Severe")
    elif df.Temperature[i]>104:
        print(i, "Extremely Severe")
    elif df.HeartRate[i]>110:
        print(i, "Extremely Severe")
    elif df.RespiratoryRate[i]>25:
        print(i, "Extremely Severe")
    elif df.Temperature[i]>100.4 and df.HeartRate[i]>100:
        print(i, "Moderately Severe")
    elif df.Temperature[i]>100.4 and df.SpO2[i]>=90 and df.SpO2[i]<=92:
        print(i, "Moderately Severe")
    elif df.RespiratoryRate[i]>22 and df.SpO2[i]>=90 and df.SpO2[i]<=92:
        print(i, "Moderately Severe")
    elif df.Age[i]>60 and (df.HeartRate[i]>100 or (df.SpO2[i]>=90 and df.SpO2[i]<=92) or df.RespiratoryRate[i]>22 or df.Temperature[i]>100.4):
        print(i, "Moderately Severe")
    elif df.SpO2[i]>=90 and df.SpO2[i]<=92 and df.HeartRate[i]>100:
        print(i, "Moderately Severe")
    

