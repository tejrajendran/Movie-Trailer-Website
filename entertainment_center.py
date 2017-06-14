# use the class we defined in the media file
# keep class definitions in their own file

import json
import urllib

import fresh_tomatoes
import media
import requests

# response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=5d5127ef839b750c40642786f6692867&query=The+Dark+Knight')
# batman_data = json.loads(response.text)
# print batman_data
#
# response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=5d5127ef839b750c40642786f6692867&query=Toy+Story')
# toy_story = json.loads(response.text)
#
# response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=5d5127ef839b750c40642786f6692867&query=avatar')
# avatar_data = json.loads(response.text)
#
# response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=5d5127ef839b750c40642786f6692867&query=Finding+Nemo')
# nemo_data = json.loads(response.text)

batman_data = json.loads(urllib.urlopen('https://api.themoviedb.org/3/movie/49026?api_key=5d5127ef839b750c40642786f6692867').read())
avatar_data = json.loads(urllib.urlopen('https://api.themoviedb.org/3/movie/19995?api_key=5d5127ef839b750c40642786f6692867').read())
toy_story_data = json.loads(urllib.urlopen('https://api.themoviedb.org/3/movie/862?api_key=5d5127ef839b750c40642786f6692867').read())
nemo_data = json.loads(urllib.urlopen('https://api.themoviedb.org/3/movie/12?api_key=5d5127ef839b750c40642786f6692867').read())
wonder_woman_data = json.loads(urllib.urlopen('https://api.themoviedb.org/3/movie/297762?api_key=5d5127ef839b750c40642786f6692867').read())
guardians_data = json.loads(urllib.urlopen('https://api.themoviedb.org/3/movie/283995?api_key=5d5127ef839b750c40642786f6692867').read())


toy_story = media.Movie(toy_story_data['title'],
                        toy_story_data['overview'],
                     "https://image.tmdb.org/t/p/w500" + toy_story_data['poster_path'],
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(avatar_data['title'],
                     avatar_data['overview'],
                     "https://image.tmdb.org/t/p/w500" + avatar_data['poster_path'],
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")


batman = media.Movie(batman_data['title'],
                     batman_data['overview'],
                     "https://image.tmdb.org/t/p/w500" + batman_data['poster_path'],
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY")

nemo = media.Movie(nemo_data['title'],
                   nemo_data['overview'],
                     "https://image.tmdb.org/t/p/w500" + nemo_data['poster_path'],
                   "https://www.youtube.com/watch?v=wZdpNglLbt8")

wonder_woman = media.Movie(wonder_woman_data['title'],
                           wonder_woman_data['overview'],
                     "https://image.tmdb.org/t/p/w500" + wonder_woman_data['poster_path'],
                        "https://www.youtube.com/watch?v=1Q8fG0TtVAY")

guardians = media.Movie(guardians_data['title'],
                        guardians_data['overview'],
                     "https://image.tmdb.org/t/p/w500" + guardians_data['poster_path'],
                        "https://www.youtube.com/watch?v=duGqrYw4usE")

movies = [toy_story,avatar,batman,nemo, wonder_woman, guardians]
fresh_tomatoes.open_movies_page(movies)