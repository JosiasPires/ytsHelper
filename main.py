#!/usr/bin/env python3
import sys
import requests
import webbrowser

if len(sys.argv) < 2:
    print("Execute -> $ python main.py -help")
    sys.exit(1)

if sys.argv[1] in ['-h', '-help']:
    print("YTS.MX HELPER")
    print(len("YTS.MX HELPER") * "_" + "\n")
    print("-h / -help   | Help get all commands")
    print("-l / -list   | List  movies -> $ python main.py -l <OPTIONAL PAGE INDEX>")
    print("-s / -search | Search movie -> $ python main.py -s <MOVIE NAME>")
    print("-o / -open   | Open yts link to movie on default browser -> $ python main.py -o <MOVIE NAME>")
    print("The <MOVIE NAME> must be in quotation marks")


if sys.argv[1] in ['-l', '-list']:
    if len(sys.argv) == 3:
        page = sys.argv[2]
    else:
        page = 1
    response = requests.get(f"https://yts.mx/api/v2/list_movies.json?page={page}")
    moviedic = response.json()["data"]
    if response.status_code == 200 and 'movies' in moviedic:
        movies = moviedic["movies"]
        print(f"yts.mx | Page {page} \n")
        for movie in movies:
            print(f"{movie['title']} [{movie['year']}] | Code: {movie['imdb_code']}")

if sys.argv[1] in ['-s', '-search']:
    query_term = sys.argv[2]
    response = requests.get(f"https://yts.mx/api/v2/list_movies.json?query_term={query_term}")
    moviedic = response.json()["data"]
    if response.status_code == 200 and 'movies' in moviedic:
        movies = moviedic["movies"]
        for movie in movies:
            print(f"{movie['title']} [{movie['year']}] | Code: {movie['imdb_code']}")

if sys.argv[1] in ['-d', 'download']:
    query_term = sys.argv[2]
    response = requests.get(f"https://yts.mx/api/v2/list_movies.json?query_term={query_term}")
    moviedic = response.json()["data"]
    if response.status_code == 200 and 'movies' in moviedic:
        movie = moviedic["movies"][0]
        print(f"Downloading {movie['title']} [{movie['year']}] ...")
        torrent = movie["torrents"][0]
        magnet = f"magnet:?xt=urn:btih:{torrent['hash']}&dn={torrent['url']}&tr=http://track.one:1234/announce&tr=udp://track.two:80"
        webbrowser.open(magnet)

if sys.argv[1] in ['-o', '-open']:
    query_term = sys.argv[2]
    response = requests.get(f"https://yts.mx/api/v2/list_movies.json?query_term={query_term}")
    moviedic = response.json()["data"]
    if response.status_code == 200 and 'movies' in moviedic:
        movie = moviedic["movies"][0]
        print(f"Opening {movie['title']} [{movie['year']}] ...")
        webbrowser.open_new_tab(movie["url"])
