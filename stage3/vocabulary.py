data_file = open('data.txt', 'r')
vocab_file = open('vocabulary.txt', 'w')

words = []
line = data_file.readline().split()
while line:
	review = line.pop(0)
	words.extend(line)
	line = data_file.readline().split()
	
vocabulary = []
for word in words:
	if vocabulary.count(word) == 0 and words.count(word)>1:
		vocabulary.append(word)

vocabulary.sort()

for word in vocabulary:
	vocab_file.write(word+'\n')	
