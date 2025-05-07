import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the data
df = pd.read_csv('path_to_your_space_mission_data.csv')

# Initial Exploration
print(df.head())  # Preview the first few rows of the data
print(df.info())  # Check data types and missing values
print(df.isnull().sum())  # Count missing values

# Clean the data (example: handling missing values, correcting data types)
df['launch_date'] = pd.to_datetime(df['launch_date'], errors='coerce')  # Convert to datetime
df['mission_cost'] = pd.to_numeric(df['mission_cost'], errors='coerce')  # Convert cost to numeric

# Answer the first question: Who launched the most missions in any given year?
missions_by_year = df.groupby(['year', 'country']).size().reset_index(name='mission_count')
top_launching_countries = missions_by_year.groupby('year')['mission_count'].idxmax()
top_launching_countries = missions_by_year.loc[top_launching_countries]

plt.figure(figsize=(10,6))
sns.barplot(x='year', y='mission_count', hue='country', data=top_launching_countries)
plt.title("Top Launching Countries per Year")
plt.xticks(rotation=45)
plt.show()

# Question 2: How has the cost of a space mission varied over time?
avg_cost_by_year = df.groupby('year')['mission_cost'].mean().reset_index()

plt.figure(figsize=(10,6))
sns.lineplot(x='year', y='mission_cost', data=avg_cost_by_year)
plt.title("Average Cost of Space Missions Over Time")
plt.show()

# Question 3: Which months are the most popular for launches?
df['month'] = df['launch_date'].dt.month
missions_by_month = df.groupby('month').size().reset_index(name='mission_count')

plt.figure(figsize=(10,6))
sns.barplot(x='month', y='mission_count', data=missions_by_month)
plt.title("Number of Space Missions by Month")
plt.xticks(ticks=range(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.show()

# Question 4: Have space missions gotten safer or has the chance of failure remained unchanged?
# Assuming there is a 'status' column indicating success or failure:
failure_rate_by_year = df.groupby('year')['status'].apply(lambda x: (x == 'Failure').mean()).reset_index(name='failure_rate')

plt.figure(figsize=(10,6))
sns.lineplot(x='year', y='failure_rate', data=failure_rate_by_year)
plt.title("Failure Rate of Space Missions Over Time")
plt.show()
