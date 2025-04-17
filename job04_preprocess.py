import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt, Komoran

df = pd.read_csv('./crawling_data/naver_headline_total_250416.csv')
df.info()
print(df.head())
print(df.category.value_counts())

X = df.titles
Y = df.category

print(X[0])
okt = Okt()
okt_x = okt.morphs(X[0])
print(okt_x)
okt_x = okt.morphs(X[0], stem=True)
print(okt_x)

print(X[1])
okt = Okt()
okt_x = okt.morphs(X[1])
print(okt_x)
okt_x = okt.morphs(X[1], stem=True)
print(okt_x)


komoran = Komoran()
komoran_x = komoran.morphs([0])
print(komoran_x)