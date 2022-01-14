import requests
from bs4 import BeautifulSoup

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

# making a get request to the above URL using requests module
response = requests.get(URL)

# raw html text
website_html = response.text

# making soup
soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

all_movies  = soup.find_all(name = "h3",class_ = "title")
print(all_movies)

# movie_titles = []
# for movie in all_movies:
#   movie_titles.append(movie.getText())
# print(movie_titles)

movie_titles = [movie.getText() for movie in all_movies]
# This gives the list of movies from 100 to 1

# getting the list of movies in reverse order. i.e. 1 to 100
# print(movie_titles[::-1])

movies = []
for n in range(len(movie_titles)-1, -1,-1): # starting from end of list to beginning and stepping by -1
    movies.append(movie_titles[n])
print(movies)

with open("movies.txt", mode ='w') as file:
    for movie in movies:
        file.write(f"{movie}\n")
