def Encoder(df):
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    for column in (df.columns):
        if df[column].dtype == 'object':
            df[column] = le.fit_transform(df[column])

        