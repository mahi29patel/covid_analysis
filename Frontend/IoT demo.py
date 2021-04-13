
import pandas as pd

df1 = pd.read_csv('Frontend\hospital_data.csv')
df = pd.read_csv('Frontend\patients_data.csv')



length= len(df.index)
#print(length)
for i in range (length):

    if df.SpO2[i]<90:
        s='Extremely Severe'
    elif df.Temperature[i]>104:
        s='Extremely Severe'
    elif df.HeartRate[i]>110:
        s='Extremely Severe'
    elif df.RespiratoryRate[i]>25:
        s='Extremely Severe'

    elif df.Temperature[i]>100.4 and df.HeartRate[i]>100:
        s= 'Moderately Severe'
    elif df.Temperature[i]>100.4 and df.SpO2[i]>=90 and df.SpO2[i]<=92:
        s= 'Moderately Severe'
    elif df.RespiratoryRate[i]>22 and df.SpO2[i]>=90 and df.SpO2[i]<=92:
        s= 'Moderately Severe'
    elif df.Age[i]>60 and (df.HeartRate[i]>100 or (df.SpO2[i]>=90 and df.SpO2[i]<=92) or df.RespiratoryRate[i]>22 or df.Temperature[i]>100.4):
        s= 'Moderately Severe'
    elif df.SpO2[i]>=90 and df.SpO2[i]<=92 and df.HeartRate[i]>100:
        s= 'Moderately Severe'

    else:
        s= 'Normal'

    df1.loc[i, 'Severity'] = s
    df1 = df1.sort_values(by = 'Severity')
    df1.to_csv('Frontend\hospital_data.csv', index=False)

#df1.to_csv('Frontend\hosp_data.csv', index=False)

print(df1.head())

    

