import csv
import random

# number of rows in the csv files
jokesSize = 38271
jokes_hiSize = 22

# jokes.csv obtained from r/Jokes and jokes_hi.csv is obtained from publically available data

# function returns a list of random question and answer from the jokes.csv file


def qandaJokes():
    with open('./data/jokes.csv', encoding='utf8') as file:
        jokes = csv.DictReader(file)
        randNum = random.randint(1, jokesSize)
        joke = list(jokes)
        returnList = [joke[randNum]['Question'], joke[randNum]['Answer']]
        return returnList

# function returns a random string from the jokes_hi.csv file


def hindiJokes():
    with open('./data/jokes_hi.csv', encoding='utf8') as file:
        jokes = csv.DictReader(file)
        randNum = random.randint(1, jokes_hiSize)
        joke = list(jokes)
        return joke[randNum]['Joke']
