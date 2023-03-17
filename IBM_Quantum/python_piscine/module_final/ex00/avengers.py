#!/usr/bin/env python3
import pandas as pd
from pysentimiento import create_analyzer
import sys
import matplotlib.pyplot as plt
import numpy as np

file = "tweets.csv"
df = pd.read_csv(file, encoding="ISO-8859-1")
comentarios = df["text"].tolist()

analysis = create_analyzer(task="sentiment", lang="en")
sentiments = []
for elem in comentarios:
  res = analysis.predict(elem)
  sentiments.append(res.output)

pos = sentiments.count("POS")
neu = sentiments.count("NEU")
neg = sentiments.count("NEG")
total = pos + neu + neg
pos_por = (pos / total) * 100
neg_por = (neg / total) * 100
neu_por = (neu / total) * 100
sys.stdout.write("POSITIVE COMMENTS: %d - %.2f%%\nNEGATIVE COMMENTS: %d - %.2f%%\nNEUTRAL COMMENTS: %d - %.2f%%\nTOTAL COMMENTS: %d" % (pos, pos_por, neg, neg_por, neu, neu_por, total))

lst_names = ["POS", "NEG", "NEU"]
lst_dec = np.array([pos, neg, neu])
lst_por = np.array([pos_por, neg_por, neu_por])
plt.pie(lst_por, labels=lst_names, autopct = "%.2f%%")
plt.show()
plt.bar(lst_names, lst_dec, auto = "%.2f%%")
plt.show()
