import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page we want to scrape
url = 'https://www.basketball-reference.com/leagues/NBA_2021_per_game.html'

# Send GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Successfully fetched the page!")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table that contains the player stats
table = soup.find(name='table')

# Extract all the rows from the table
table_rows = table.find_all('tr')

# List to hold player stats
player_stats = []

# Loop through all rows in the table
for row in table_rows:
    # Get all columns (td tags) in the row
    cols = row.find_all('td')
    
    # Skip the rows that do not contain data (empty rows or header rows)
    if len(cols) > 0:
        player_name = cols[1].get_text()
        points = cols[28].get_text()
        assists = cols[23].get_text()
        rebounds = cols[21].get_text()
        
        # Append the extracted data to our list
        player_stats.append({
            'Player': player_name,
            'Points': points,
            'Assists': assists,
            'Rebounds': rebounds
        })

# Convert the list of player stats into a pandas DataFrame
df = pd.DataFrame(player_stats)

# Save the DataFrame to a CSV file
df.to_csv('nba_player_stats.csv', index=False)

print("Data saved to nba_player_stats.csv")
