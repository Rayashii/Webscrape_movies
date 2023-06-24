import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

movie_list = soup.find('tbody', {'class': 'lister-list'}).find_all('tr')

# Create a new CSV file
csv_file = open('imdb_top_movies.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)

# Write the header row
writer.writerow(['Title', ' Released on', ' Rating'])

# Iterate over each movie and extract the details
for movie in movie_list:
    title_column = movie.find('td', {'class': 'titleColumn'})
    title = title_column.find('a').text
    year = title_column.find('span', {'class': 'secondaryInfo'}).text.strip('()')
    rating = movie.find('strong').text

    # Write the movie details to the CSV file
    writer.writerow([title , year , rating])

# Close the CSV file
csv_file.close()

print("Movie details have been saved to 'imdb_top_movies.csv'.")
