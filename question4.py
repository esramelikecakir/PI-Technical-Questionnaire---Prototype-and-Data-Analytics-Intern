import pandas as pd

data = pd.read_csv("/Users/esra/Library/Containers/com.microsoft.Excel/Data/Downloads/country_vaccination_stats-3.csv")
daily_vaccinations = data["daily_vaccinations"]

if daily_vaccinations.isnull().any():
    countries = data.groupby("country")
    daily_vaccinations_perday = data.groupby("country")["daily_vaccinations"].min()
    for i, row in data.iterrows():
        if pd.isnull(row['daily_vaccinations']):
            data.at[i, 'daily_vaccinations'] = daily_vaccinations_perday[row['country']]
    data['daily_vaccinations'] = data['daily_vaccinations'].fillna(0)

new_data = data.to_csv("//Users/esra/Library/Containers/com.microsoft.Excel/Data/Downloads/country_vaccination_stats-3.csv")