
import pandas as pd
import random
import time

var = 1
while var == 1 :
    df1 = pd.read_csv('Frontend\hospital_data.csv')
    df = pd.read_csv('Frontend\patients_data.csv')
    #print(df.head())

    length= len(df.index)
    #print(length)

    for i in range(length):

        df.loc[i, 'SpO2']=float(random.randrange(800, 1000))/10
        df.loc[i, 'Temperature']=float(random.randrange(9900, 10500))/100
        df.loc[i, 'HeartRate']=random.randint(70,110)
        df.loc[i, 'RespiratoryRate']=random.randint(14,30)


    #print(df.head())


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
    time.sleep(100)

    

