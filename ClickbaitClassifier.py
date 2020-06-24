import os

print(os.getcwd())

# Open data files
f = open("data/clickbait_data.txt", encoding="utf-8")
clickbait = f.readlines()
f2 = open("data/non_clickbait_data.txt", encoding="utf-8")
non_clickbait = f2.readlines()

# Create test data
test_clickbait_data = clickbait[len(clickbait)*2//3:]
test_non_clickbait_data = non_clickbait[len(non_clickbait)*2//3:]
clickbait = clickbait[:len(clickbait)*2//3-1]
non_clickbait = non_clickbait[:len(non_clickbait)*2//3-1]

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
total_unique_words = len(clickbait_wordcount)
for word in non_clickbait_wordcount:
	if word not in clickbait_wordcount:
		total_unique_words +=1

# Check data
# print(clickbait_wordcount)
# print(non_clickbait_wordcount)
# print(total_clickbait_words)
# print(total_non_clickbait_words)
# print(total_words)

def classify(text):
	P_clickbait = len(clickbait)/(len(clickbait)+len(non_clickbait))
	P_non_clickbait = 1-P_clickbait

	P_text_clickbait = 1
	for word in text.split():
		numer = 1
		if word in clickbait_wordcount:
			numer += clickbait_wordcount[word]
		denom = total_clickbait_words + total_unique_words
		P_text_clickbait *= numer/denom

	P_text_non_clickbait = 1
	for word in text.split():
		numer = 1
		if word in non_clickbait_wordcount:
			numer += non_clickbait_wordcount[word]
		denom = total_non_clickbait_words + total_unique_words
		P_text_non_clickbait *= numer/denom

	proportionality = 1 / (P_clickbait*P_text_clickbait + P_non_clickbait*P_text_non_clickbait)
	P_text_is_clickbait = proportionality*P_clickbait*P_text_clickbait
	P_text_is_not_clickbait = proportionality*P_non_clickbait*P_text_non_clickbait
	print([P_text_is_clickbait, P_text_is_not_clickbait])

	if(P_text_is_clickbait >= P_text_is_not_clickbait):
		return "clickbait"
	else:
		return "not clickbait"

print(classify("The Names Of Popular Celebrities According To My Mom"))
print(classify("Romanian parliament ratifies EU accession treaty"))

correct_count = 0;
for title in test_clickbait_data:
	if(classify(title) == "clickbait"):
		correct_count += 1

for title in test_non_clickbait_data:
	if(classify(title) == "not clickbait"):
		correct_count += 1

accuracy = correct_count / (len(test_clickbait_data)+len(test_non_clickbait_data))
print("Accuracy: " + str(accuracy))
