import os
import re

with open("movieData.csv") as f:
    data = f.read()

movieData=data.strip().split("\n")
movieData = movieData[1:]

writingDetails = ["Title", "Year", "Director", "Cast", "Genre","Notes"]

os.chdir("./NewData")
for movieRecord in movieData:
    movieDetails = movieRecord.split('\t')
    length = len(movieDetails)
    title = movieDetails[0]
    movieDetails = [x.replace("\"","") for x in movieDetails]
    title = re.sub('[^A-Za-z0-9]+', '', title)
    f = open(title + '.txt', 'w')
    for i in range(length):
        f.write(writingDetails[i] + ": " + movieDetails[i] + '\n')
    f.close()