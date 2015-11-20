import pandas as pd


train = pd.read_csv("../data/original/training_set.tsv", sep='\t')

train.to_csv("../data/prepped/train.csv")
