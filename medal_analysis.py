def medals_by_country_year(df):
    return df.groupby(['Year', 'Country'])['Medal'].count().reset_index(name='Total_Medals')

def top_countries(df, top_n=10):
    return df.groupby('Country')['Medal'].count().sort_values(ascending=False).head(top_n).reset_index(name='Total_Medals')
