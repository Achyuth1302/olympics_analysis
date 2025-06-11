def clean_data(df):
    df.dropna(inplace=True)
    df['Year'] = df['Year'].astype(int)
    df['Country'] = df['Country'].astype(str)
    df['Medal'] = df['Medal'].astype(str)
    return df
