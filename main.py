from bs4 import BeautifulSoup
import requests
from math import ceil

url = "https://en.wikipedia.org/wiki/Golden_Globe_Award_for_Best_Motion_Picture_%E2%80%93_Drama"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')


def find_winners(year_in_tens, movies, directors, producers, years):
    decade = soup.find('span', class_="mw-headline", id=f"{year_in_tens}s")
    table = decade.find_next('table', class_='wikitable').find('tbody')

    year = year_in_tens

    n = 0
    winner = table('b')
    for w in winner:
        if n % 3 == 0:
            movies.append(w.text)
        if n % 3 == 1:
            directors.append(w.text)
        if n % 3 == 2:
            producers.append(w.text)
            year += 1
            years.append(year)
        n += 1


movies_list = []
directors_list = []
producers_list = []
year_list = []

start_year = int(input("Year start:"))
stop_year = int(input("Year stop:"))

start_year = round(start_year,-1)
stop_year = round(stop_year,-1)

for i in range(start_year, 2020, 10):
    find_winners(i, movies_list, directors_list, producers_list, year_list)

print("Golden Globe Award for Best Motion Picture – Drama")
print("")
print("")

for i in range(len(movies_list)):
    print(f"Year:{year_list[i]}")
    print(f"Film: {movies_list[i]}")
    print(f"Director: {directors_list[i]}")
    print(f"Producer: {producers_list[i]}")
    print("")
