import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt

df = pd.read_csv('./crawling_data/naver_headline_total_250416.csv')
df.info()
print(df.head())