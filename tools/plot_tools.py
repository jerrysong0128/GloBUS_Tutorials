import matplotlib.pyplot as plt

region_names = [
    "Canada",
    "USA",
    "Mexico",
    "Central America",
    "Brazil",
    "Rest of South America",
    "Northern Africa",
    "Western Africa",
    "Eastern Africa",
    "South Africa",
    "Western Europe",
    "Central Europe",
    "Turkey",
    "Ukraine region",
    "Central Asia",
    "Russia region",
    "Middle East",
    "India",
    "Korea region",
    "China region",
    "Southeast Asia",
    "Indonesia region",
    "Japan",
    "Oceania",
    "Rest of South Asia",
    "Rest of Southern Africa"
]

region_abbreviations = [
    "CAN", "USA", "MEX", "CENAM", "BRA", "RSA", "NAF", "WAF", "EAF", "SAF", 
    "WEU", "CEU", "TUR", "UKR", "CAS", "RUS", "ME", "IND", "KOR", "CHN", 
    "SEA", "IDN", "JPN", "OCE", "ROSA", "ROSAF"
]

def plot_database(df, df_title, df_ylabel):
    # Filter the dataframe to include only rows where the year is divisible by 10
    df_filtered = df[df.index % 10 == 0]
    
    fig, ax = plt.subplots(figsize=(18, 4))
    df_filtered.plot(kind='bar', stacked=True, ax=ax)
    ax.legend(region_abbreviations, loc=2, bbox_to_anchor=(1.05, 1.0), ncol=2, borderaxespad=0.)
    ax.set_title(df_title)
    ax.set_xlabel('Year')
    ax.set_ylabel(df_ylabel)
    
    plt.show()
