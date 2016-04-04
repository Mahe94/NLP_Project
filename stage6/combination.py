""" 
Code to create all combinations of vocabulary words.
"""

# vocabulary.txt and vocabulary2.txt contains same contents
with open("vocabulary.txt", 'r') as fvoc:
	# this file contains the final bigra
	with open("bigram.txt", 'w') as fout:
			try:
				i = 0
				for line in fvoc:
					word1 = line.rstrip()
					with open("vocabulary2.txt",  'r') as fvoc2:
						for line2 in fvoc2:
							i+=1
							word2 = line2.rstrip()
							w = ''.join([word1," ",word2,"\n"])
							print(i,": ", w)
							fout.write(w)
			except EOFError:
				pass
