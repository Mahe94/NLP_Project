# making a mega review document with all the review concatenated into one line
review = ''	
unigram_list = []
bigram_list = []

# making a mega review text
with open("data.txt", "r") as fin:
	review = ''		
	for line in fin:
		review += line[1:].rstrip()	

# creating a unigram set
ug = set(review.split())
# separating unigram with count > 1
for key in ug:
	if review.count(key) > 1:
		# print str(key)+"\r" 
		unigram_list.append(key)

# tokenising and creating all bigram combinations 
input_list = review.split()
for i in range(len(input_list)-1):
    bigram_list.append((input_list[i], input_list[i+1]))

# creating a bigram set and separating bigram with count > 1
bg = set(bigram_list)
bigram_list = []
for key in bg:
	substr = str(key[0])+" "+str(key[1])
	if review.count(substr) > 1:
		bigram_list.append(substr)


# print unigram_list
unigram_list.sort()
bigram_list.sort()
with open("unigram.txt", "w") as fd:
	for i in unigram_list:
		fd.write(str(i))
		fd.write("\n")

with open("bigram.txt", "w") as fd:
	for i in bigram_list:
		fd.write(i)
		fd.write("\n")

print "ugram length ", len(unigram_list)
print "bigram length ", len(bigram_list)
print "unique ug created earlier", len(ug)
print "unique bg created earlier", len(bg)