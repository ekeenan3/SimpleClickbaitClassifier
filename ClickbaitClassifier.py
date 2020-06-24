import os

print(os.getcwd())

# Open data files
f = open("data/clickbait_data.txt", encoding="utf")
clickbait = f.readlines()
f2 = open("data/non_clickbait_data.txt", encoding="utf")
non_clickbait = f2.readlines()

print(str(len(clickbait)) + " " + str(len(non_clickbait)))

# Process Titles


def classify(title):
