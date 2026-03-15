import pandas as pd

def transform_data(df):

    df = df.dropna()

    df["revenue"] = df["price"] * df["quantity"]

    df["date"] = pd.to_datetime(df["date"])

    return df
