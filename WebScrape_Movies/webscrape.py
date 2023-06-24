import csv
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.imdb.com/search/title/'
params = {
    'count': 100,
    'groups': 'top_1000',
    'sort': 'user_rating'
}

# Specify the desired CSV file path
csv_file = 'imdb_top_1000_movies.csv'

# Open the CSV file in write mode
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Title', 'Year', 'Rating'])

    start = 1
    while start <= 1000:
        # Update the 'start' parameter in the URL
        params['start'] = start

        response = requests.get(base_url, params=params)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'lxml')

        movie_containers = soup.find_all('div', class_='lister-item-content')

        # Iterate over the movie containers and extract data to write in the CSV file
        for container in movie_containers:
            title = container.h3.a.text
            year = container.h3.find('span', class_='lister-item-year').text.strip('()')
            rating = container.find('div', class_='ratings-bar').strong.text

            # Write the data row
            writer.writerow([title, year, rating])

        start += 100

print(f"Scraped data has been saved to '{csv_file}'.")
