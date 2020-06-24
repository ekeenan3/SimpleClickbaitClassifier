import os

print(os.getcwd())

# Open data files
f = open("data/clickbait_data.txt", encoding="utf-8")
clickbait = f.readlines()
f2 = open("data/non_clickbait_data.txt", encoding="utf-8")
non_clickbait = f2.readlines()

print(str(len(clickbait)) + " " + str(len(non_clickbait)))

# Process titles into dictionaries of word count and overall word count for each classification
clickbait_wordcount = {}
total_clickbait_words = 0
for title in clickbait:
	for word in title.split():
		total_clickbait_words += 1
		if word in clickbait_wordcount:
			clickbait_wordcount[word] += 1
		else:
			clickbait_wordcount[word] = 1

non_clickbait_wordcount = {}
total_non_clickbait_words = 0
for title in non_clickbait:
	for word in title.split():
		total_non_clickbait_words += 1
		if word in non_clickbait_wordcount:
			non_clickbait_wordcount[word] += 1
		else:
			non_clickbait_wordcount[word] = 1

# Find total unique words across all titles
total_words = len(clickbait_wordcount)
for word in non_clickbait_wordcount:
	if word not in clickbait_wordcount:
		total_words +=1

print(clickbait_wordcount)
print(non_clickbait_wordcount)
print(total_clickbait_words)
print(total_non_clickbait_words)
print(total_words)
