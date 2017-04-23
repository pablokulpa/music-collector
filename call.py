import csv
from datetime import date
import random
import os.path
import sys
import operator


# checking file existences
def checking_file(filename):
    if os.path.exists(filename) is False:
        sys.exit("Databese file doesnt exist")


# Open file and adding to list
def read(albumy):
    with open(csvname) as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        tuple1 = ()
        tuple2 = ()
        try:
            for albums in readCSV:
                tuple1 = albums[0].strip().lower(), albums[1].strip().lower()
                tuple2 = int(albums[2].strip()), albums[3].strip().lower(), albums[4].strip()
                albumy.append((tuple(tuple1), tuple(tuple2)))
        except IndexError:
                pass
    return albumy


# Adding new album to list and after to gile csv
def adding_album(albumy):
    author = input("Artist name: ").lower()
    album_name = input("Write album name: ").lower()
    year_release = input("Write the year of release: ").lower()
    genre = input("Write genre: ").lower()
    lenght = input("Write lenght: ").lower()
    tuple1 = ()
    tuple2 = ()
    tuple1 = author, album_name
    tuple2 = year_release, genre, lenght
    albumy.append((tuple1, tuple2))
    with open(csvname, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='|')
        for albums in albumy:
            spamwriter.writerow([albums[0][0]]+[albums[0][1]]+[albums[1][0]]+[albums[1][1]]+[albums[1][2]])
#        spamwriter.writerow([albums[0][0]]+[albums[0][1]])


# Finding album by artist name
def find_by_artist(albumy):
    author = input("Write artist name: ")
    for albums in albumy:
        if author in albums[0][0]:
            print('autor:', albums[0][0])
            print('album name:', albums[0][1])
            print('year relase:', albums[1][0])
            print('genre:', albums[1][1])
            print('lenght:', albums[1][2], end='\n')


# Counting year of album
def album_year(albumy):
    today_year = date.today().year
    for albums in albumy:
        year_old = today_year-int(albums[1][0])
        print('album name:', albums[0][1], end=' ')
        print('Years:', year_old)


# Finding album by genre adding to list and next choosing random from list
def random_album_by_genre(albumy):
    genre = input('Write genre: ')
    lista_genre = []
    for albums in albumy:
        if genre in albums[1][1]:
            lista_genre.append(albums)
    random_album = random.choice(lista_genre)
    print('autor:', random_album[0][0])
    print('album name:', random_album[0][1])
    print('year relase:', random_album[1][0])
    print('lenght:', random_album[1][2], end='\n')


# Finding album by year
def find_by_year(albumy):
    give = True
    while give:
        try:
            year_search = int(input('Write a year: '))
        except ValueError:
            print("Wrong sign")
        else:
            give = False
    for albums in albumy:
        if year_search == albums[1][0]:
            print('autor:', albums[0][0])
            print('album name:', albums[0][1])
            print('genre:', albums[1][1])
            print('lenght:', albums[1][2], end='\n')


def find_by_genre(albumy):
    genre = input("Write genre: ").lower()
    for albums in albumy:
        if genre in albums[1][1]:
            print('autor:', albums[0][0])
            print('album name:', albums[0][1])
            print('year relase:', albums[1][0])
            print('lenght:', albums[1][2], end='\n')


def find_author_by_album(albumy):
    album_name = input("Write album name:").lower()
    for albums in albumy:
        if album_name in albums[0][1]:
            print('autor:', albums[0][0])


def find_by_album_letter(albumy):
    letters_album = input("Write letter(s) album name: ").lower()
    for albums in albumy:
        if letters_album in albums[0][1]:
            print('autor:', albums[0][0])
            print('album name:', albums[0][1])
            print('genre:', albums[1][1])
            print('lenght:', albums[1][2], end='\n')


def find_all_album_one_artist(albumy):
    counter = 0
    author = input("Write artist name: ").lower()
    for albums in albumy:
        if author in albums[0][0]:
            counter += 1
    print("Albums number:", counter)


def longest_time(albumy):
    album_times = {}
    for albums in albumy:
        album_times[albums[0][1]] = albums[1][2]
    sorted_album = sorted(album_times.items(), key=operator.itemgetter(1))
    print(sorted_album[-1][0])

# START PROGRAM
csvname = 'music.csv'
checking_file(csvname)
albumy = []
read(albumy)


#  MENU
options_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Welcome in the CoolMusic! Choose the action: ")
print('Welcome in music collector created by Pablo')
print('1. Add new album')
print('2. Find albums by artist')
print('3. Find albums by year')
print('4. Find musician by album')
print('5. Find albums by letter(s)')
print('6. Find albums by genre')
print('7. Calculate the age of all albums')
print('8. Choose a random album by genre')
print('9. Show the amount of albums by an artist')
print('10. Find the longest-time album')


menu_answer = int(input('Write number 1-10: '))
while menu_answer not in options_list:
    print('Wrong number!')
    menu_answer = int(input('Write number 1-10: '))


if menu_answer == options_list[1]:
    adding_album(albumy)
elif menu_answer == options_list[2]:
    find_by_artist(albumy)
elif menu_answer == options_list[3]:
    find_by_year(albumy)
elif menu_answer == options_list[4]:
    find_author_by_album(albumy)
elif menu_answer == options_list[5]:
    find_by_album_letter(albumy)
elif menu_answer == options_list[6]:
    find_by_genre(albumy)
elif menu_answer == options_list[7]:
    album_year(albumy)
elif menu_answer == options_list[8]:
    random_album_by_genre(albumy)
elif menu_answer == options_list[9]:
    find_all_album_one_artist(albumy)
elif menu_answer == options_list[10]:
    longest_time(albumy)
