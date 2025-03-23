import numpy as np
import pandas as pd
#EX1
def swap(l: list, i: int, j: int):
    l[i], l[j] = l[j], l[i]
def reverse(l: list):
    for i in range(0, int(len(l)/2)):
        swap(l, i, len(l) - i - 1)
    return l
my_list = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
my_list = reverse(my_list)
print(my_list)

#EX2
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([10, 30, 40])
result = np.isin(array1, array2)
print(result)

#EX3
def findMaxMin(l:list) -> list:
    min = max = l[0]
    max_idx = min_idx = 0
    for i in range(1, int(len(l))):
        if (l[i] > max):
            max = l[i]
            max_idx = i
        elif (l[i] < min):
            min = l[i]
            min_idx = i
    return [min_idx, max_idx]
my_list_1 = [17, 18, 37, 12, 16, 28, 31, 19, 34, 29, 36, 13, 27, 24, 14, 21, 22, 26, 33, 20, 35, 23, 30, 15, 32, 25]
max_min_idx = findMaxMin(my_list_1)
print("Min number index:", max_min_idx[0])
print("Max number index:", max_min_idx[1])
print("Max number index:", max_min_idx[1])

#EX4:
import string
words_list = []
with open("story.txt", "r") as file:
    for line in file:
        clean_line = line.translate(str.maketrans('', '', string.punctuation))
        words = clean_line.strip().split()
        words_list.extend(word.lower() for word in words)
print(words_list)
# Convert to a DataFrame
df = pd.DataFrame(words_list, columns=["Word"])
freqs = df.value_counts()
print(freqs[0:100])


