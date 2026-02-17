import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    X = df.drop("label", axis=1)
    y = df["label"]
    return X, y
