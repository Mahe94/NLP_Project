"""
Code to create bigram by checking if the words in the combinations file exists in
the mega document created, which is nothing but the concatenation of all the 
reviews into one single line.
"""

# making a mega review document with all the review concatenated into one line
with open("megadoc.txt", "w+") as fout:
	with open("data.txt", "r") as fin:
		review = ''		
		for line in fin:
			review += line[1:].rstrip()
		fout.write(review)

# checking if the vocabulary file(voc.txt) containing all the combinations of the
# vocabulary words is present in the mega review document file
with open("doc.txt", "r") as fd:
	with open("voc.txt", "r") as fin:
		with open("bigram.txt", "w") as fout:
			review = fd.read()
			print(review)
			for line in fin:
				line = line.rstrip()
				if line in review:
					print(line)
					fout.write(line+"\n")
