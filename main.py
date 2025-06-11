from scripts.data_loader import load_data
from scripts.data_cleaning import clean_data
from scripts.medal_analysis import medals_by_country_year, top_countries
from scripts.visualization import plot_medal_trend, plot_top_countries

def main():
    df = load_data('data/olympics_history.csv')
    df = clean_data(df)

    medals_df = medals_by_country_year(df)
    top_df = top_countries(df)

    print("Top Countries:\n", top_df)

    plot_top_countries(top_df)
    plot_medal_trend(medals_df, top_df['Country'].tolist())

if __name__ == '__main__':
    main()
