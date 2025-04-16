import pandas as pd
import numpy as np

#Week4_1
data1 = pd.read_csv('Week4_1_data.csv')

#1
print(data1.groupby(['educational_level']).size().reset_index(name='count'))

#2
data2 = data1.sort_values(by= 'annual_income', ascending= False)
print(data2.head(20))

#3
data3 = data1[(data1['annual_income'] > 50000) & (data1['year_of_birth'] > 1960)]
print(data3)

#4
data4 = data1[(data1['annual_income'] > 50000) & (data1['year_of_birth'] > 1960)].sort_values(by= 'annual_income', ascending= False)
print(data4.head(20))

#5
data5 = data1[(data1['marital_status'] == 'Divorced') | (data1['marital_status'] == 'Married')]
print(data5)

#6
print(data1.groupby(['educational_level'])['annual_income'].mean())

#7
print(data1.groupby(['educational_level', 'marital_status'])['annual_income'].mean())




#Week4_2
df1 = pd.read_csv('Iris (1).csv')

#1a
print(df1.groupby(['Species'])[['SepalLengthCm', 'SepalWidthCm']].mean())

#2a
print(df1.groupby(['Species'])[['SepalLengthCm', 'SepalWidthCm']].max())

#1b
print(df1.sort_values(by= 'SepalLengthCm', ascending= False).groupby(['Species']).head(10))

#2b
df2 = df1
df2['C'] = df2['SepalLengthCm'] + df2['SepalWidthCm']
print(df2.sort_values(by= 'C', ascending= False).head(50).groupby(['Species']).size().reset_index(name='count'))

#3b
b = float(input("Enter the value for b (PetalLengthCm offset): "))
c = float(input("Enter the value for c (PetalWidthCm offset): "))

#3ba
df2['D'] = np.sqrt((b - df2['PetalLengthCm'])**2 + (c - df1['PetalWidthCm'])**2)
df2 = df2.sort_values(by= 'D')
if df2['D'][0] != df2['D'][1]:
    print(df2['Species'][0])
else:
    check = 1
    i = 0
    while check != 0:
        if df2['D'][i] == df2['D'][i + 1]:
            if df2['Species'][i] == df2['Species'][i + 1]:
                i += 1
                continue
            else:
                i += 2
                continue
        else:
            print(df2['Species'][i])
            check = 0

#3bb
df3 = df2.head(7)
df3 = df3.groupby(['Species']).size().reset_index(name='count')
if len(df3) == 1:
    print(df3['Species'][0])
else:
    df3 = df3.sort_values(by='count')
    if df3['count'][0] == df3['count'][1]:
        print('Bong hoa khong thuoc class nao!')
    else:
        print(df3['Species'][0])

#3bc
df4 = df2[df2['D'] <= 2]
df4 = df3.groupby(['Species']).size().reset_index(name='count')
if len(df3) == 1:
    print(df3['Species'][0])
else:
    df4 = df4.sort_values(by='count')
    if df4['count'][0] == df4['count'][1]:
        print('Bong hoa khong thuoc class nao!')
    else:
        print(df4['Species'][0])



