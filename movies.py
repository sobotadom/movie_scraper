#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import datetime
import sys




#the url has no date attached as the website will by default set it to the current day
url = 'http://www.cineplex.com/Showtimes/any-movie/silvercity-brampton-cinemas?Date='

webpage = requests.get(url)
html = webpage.text


#Get the entire html doc and extract the classes where the movie information is held
soup = BeautifulSoup(html, 'html.parser')
sections = soup.find_all('div', {'class':"grid__item no-page-break-inside"})

print('Showtimes for Silvercity Brampton')
print(datetime.date.today())
print('---------------------------------\n')

for movie in sections:


    #extract the name
    movie_soup = BeautifulSoup(str(movie), 'html.parser')
    names = movie_soup.find_all('a',{'class':"movie-details-link-click"})
    for name in names:
        print('------------------------')
        print(name.text.strip())
        print('------------------------')

    #extract the showtimes


    times = movie_soup.find_all('a', {'class':"showtime "}) #get the showtime field from the website
    times_list = []
    for t in times:

        if t.text.strip() not in times_list: #Get rid of duplicate showtimes
            times_list.append(t.text.strip())

    for t in times_list:
        print(t)
