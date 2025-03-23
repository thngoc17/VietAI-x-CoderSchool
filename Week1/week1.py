import pandas as pd
import numpy as np

#EX1
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
def positive_count(a:list):
    count = int()
    for i in range(0, int(len(a))):
        if a[i] > 0:
            count = count + 1
    return count

def negative_count(a:list):
    count = int()
    for i in range(0, int(len(a))):
        if a[i] < 0:
            count = count + 1
    return count
print("Positive Numbers Count:", positive_count(data1))
print("Negative Numbers Count:", negative_count(data1))

#EX2
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
data2p = pd.Series(data2)
k = 3
freqs = data2p.value_counts()
print("Elements with frequency greater than", k, ":")
for value in freqs.index:
    if freqs[value] > k:
        print(value)

#EX3
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]
strongest_neighbours = [max(data3[i], data3[i+1]) for i in range(len(data3) - 1)]
print("Strongest Neighbours:", strongest_neighbours)

#EX4 ?

#EX5
data5_list1 = [[4, 3, 5], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]
for i in range (0, int(len(data5_list1))):
    data5_list1[i] = np.concatenate((data5_list1[i], data5_list2[i])).tolist()
print("Updated Matrix:", data5_list1)

#EX6
data6 = list(range(2000, 3201))
for i in data6:
    if i % 7 == 0 and i % 5 != 0:
        print(i, end = ", ")

#EX7
data7 = int(2000)
print(data7)
while data7 < 3000:
    print(data7, end = ", ")
    if data7 % 10 == 8:
        data7 = data7 + 12
    else:
        data7 = data7 + 2

#EX8 ?


