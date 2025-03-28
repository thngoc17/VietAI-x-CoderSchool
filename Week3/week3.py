import gensim.downloader as api
import numpy as np
import math
# 25, 50, 100 or 200. Số càng lớn thì càng chính xác, nhưng chạy càng lâu các bạn nhé
model = api.load("glove-twitter-200")
word = "beautiful"
print(model[word])

print("1----------")
result = model.most_similar(word, topn=10)
print(result)

print("2----------")
result = model.most_similar(positive=["january", "february"], topn=10)
print(result)

print("3----------")
result = model.similarity("man", "woman")
print(result)

print("4----------")
result = model.most_similar(positive=["woman", "king"], negative=["man"], topn=1)
print(result)

print("5----------")
result = model.most_similar(positive=["berlin", "vietnam"], negative=["hanoi"], topn=1)
print(result)

print("6----------")
result = model.similarity("marriage", "happiness")
print(result)

def cos_similar_no_numpy(a, b):
    a_model = model(a)
    b_model = model(b)
    sum_a = 0
    sum_b = 0
    for i in range(0, int(len(a))):
        sum_a += a[i] * a[i]
    for i in range(0, int(len(b))):
        sum_a += b[i] * b[i]
    length_a = math.sqrt(sum_a)
    length_b = math.sqrt(sum_b)
    dot_product = 0
    for i in range(0, int(len(a))):
        dot_product += a[i] * b[i]
    if length_a == 0 or length_b == 0:
        return 0
    return dot_product / (length_a * length_b)


def cos_similar_numpy(a, b):
    a_model = model(a)
    b_model = model(b)
    a = np.array(a_model)
    b = np.array(b_model)
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0
    return dot_product / (norm_a * norm_b)
print(cos_similar_no_numpy("marriage", "happiness"))
print(cos_similar_numpy("marriage", "happiness"))