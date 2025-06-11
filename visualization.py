import matplotlib.pyplot as plt
import seaborn as sns

def plot_medal_trend(df, country_list):
    plt.figure(figsize=(12, 6))
    for country in country_list:
        country_data = df[df['Country'] == country]
        plt.plot(country_data['Year'], country_data['Total_Medals'], label=country)
    plt.title("Medal Trend Over Years")
    plt.xlabel("Year")
    plt.ylabel("Total Medals")
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_top_countries(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Total_Medals', y='Country', data=df, palette='viridis')
    plt.title("Top Performing Countries by Total Medals")
    plt.xlabel("Total Medals")
    plt.ylabel("Country")
    plt.tight_layout()
    plt.show()
