import json
import urllib

import fresh_tomatoes
import media

# Use themoviedb API to get info for each movie
batman_data = json.loads(urllib.urlopen('https://api.themoviedb.org/3/movie/49026?api_key=5d5127ef839b750c40642786f6692867').read())
avatar_data = json.loads(urllib.urlopen('https://api.themoviedb.org/3/movie/19995?api_key=5d5127ef839b750c40642786f6692867').read())
toy_story_data = json.loads(urllib.urlopen('https://api.themoviedb.org/3/movie/862?api_key=5d5127ef839b750c40642786f6692867').read())
nemo_data = json.loads(urllib.urlopen('https://api.themoviedb.org/3/movie/12?api_key=5d5127ef839b750c40642786f6692867').read())
wonder_woman_data = json.loads(urllib.urlopen('https://api.themoviedb.org/3/movie/297762?api_key=5d5127ef839b750c40642786f6692867').read())
guardians_data = json.loads(urllib.urlopen('https://api.themoviedb.org/3/movie/283995?api_key=5d5127ef839b750c40642786f6692867').read())

# Create media instances from each movie with respective data
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

# Create movies array to load onto fresh_tomatoes movie page
movies = [toy_story,avatar,batman,nemo, wonder_woman, guardians]
fresh_tomatoes.open_movies_page(movies)