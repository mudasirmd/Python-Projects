import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd

# Load the datasets
shootings_df = pd.read_csv('fatal_police_shootings.csv')
census_df = pd.read_csv('us_census_data.csv')

# Clean and preprocess data (handling missing values, data types, etc.)
shootings_df['date'] = pd.to_datetime(shootings_df['date'], errors='coerce')
shootings_df['state'] = shootings_df['state'].str.upper()
census_df['state'] = census_df['state'].str.upper()

# Merge datasets on state
merged_df = pd.merge(shootings_df, census_df, on='state', how='inner')

# Analysis 1: Fatal shootings by year
shootings_by_year = shootings_df.groupby(shootings_df['date'].dt.year).size()

# Plot trend of fatal shootings over the years
plt.figure(figsize=(10, 6))
sns.lineplot(x=shootings_by_year.index, y=shootings_by_year.values)
plt.title('Fatal Police Shootings Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Shootings')
plt.show()

# Analysis 2: Shootings by state and race
shootings_by_state_race = shootings_df.groupby(['state', 'race']).size().unstack().fillna(0)

# Plot the number of fatal shootings by race and state
shootings_by_state_race.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Fatal Police Shootings by Race and State')
plt.ylabel('Number of Shootings')
plt.xlabel('State')
plt.xticks(rotation=90)
plt.show()

# Further Analysis: Correlation between social indicators and police shootings
correlation_df = merged_df[['poverty_rate', 'high_school_graduation_rate', 'median_income', 'shootings_count']]
correlation_matrix = correlation_df.corr()

# Plot correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Between Social Indicators and Police Shootings')
plt.show()
