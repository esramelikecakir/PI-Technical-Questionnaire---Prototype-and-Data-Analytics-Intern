import pandas as pd

data = pd.read_csv("/Users/esra/Library/Containers/com.microsoft.Excel/Data/Downloads/country_vaccination_stats-3.csv")

most_vaccinated_countries = data.groupby("country")["daily_vaccinations"].median().nlargest(3)
