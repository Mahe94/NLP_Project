import pickle
import math
from train import training

def createParts(reviews_list):
	reviews = [[],[],[],[],[],[],[],[],[],[]]
	for i in range(len(reviews_list)):
		reviews[i/80].append(reviews_list[i])
	return reviews

def getReviews(reviews_list):
	review_value = []
	for review in reviews_list:
		review_value.append(review[0])
	return review_value

def testing(test_list, univocabulary, bivocabulary, P1, P2, upp, unp, bpp, bnp):
	result_value = []
	for test in test_list:
		test = test.split()
		
#		print test
		if univocabulary.count(test[0]) == 0:
			sum_of_pprob = 0
			sum_of_nprob = 0
		else:
			sum_of_pprob = math.log1p(upp[univocabulary.index(test[0])])
			sum_of_nprob = math.log1p(unp[univocabulary.index(test[0])])
		for i in range(len(test)-1):
			word = test[i]+" "+test[i+1]
			if bivocabulary.count(word):
				index = bivocabulary.index(word)
				sum_of_pprob += math.log1p(bpp[index])
				sum_of_nprob += math.log1p(bnp[index])
			else:
				if univocabulary.count(test[i+1]):
					index = univocabulary.index(test[i+1])
					sum_of_pprob += math.log1p(upp[index])
					sum_of_nprob += math.log1p(unp[index])

		positiveProbability = sum_of_pprob + math.log1p(P1)
		negativeProbability = sum_of_nprob + math.log1p(P2)
		
#		print positiveProbability
#		print negativeProbability
#		input('probability')

		if positiveProbability >= negativeProbability:
			result_value.append('+')
		else:
			result_value.append('-')
	return result_value

def getAccuracy(actual, result):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == result[i]:
			correct += 1
	return (1.0 * correct)/len(actual)	

if __name__ == '__main__':
		
	# vocabulary_file = open('vocabulary.txt', 'r')
	# vocabulary = vocabulary_file.read().splitlines()
	# reviews_file = open('data.txt', 'r')
	# reviews = createParts(reviews_file.read().splitlines())

	data = open("data.txt", "r")
	file1 = open("unigram.txt", "r")
	file2 = open("bigram.txt", "r")

	reviews = createParts(data.read().splitlines())
	univocabulary = file1.read().splitlines()
	bivocabulary = file2.read().splitlines()

	accuracy = 0
	for i in range(10):
		actual_values = []
		test_set = []
		for review in reviews[i]:
			test_set.append(review[1:])
			actual_values.append(review[0])
		
		training_set = []
		for j in range(10):
			if i != j:
				training_set.extend(reviews[j])
		
		P1, P2, upp, unp, bpp, bnp = training(training_set, univocabulary, bivocabulary)
		
	#	print P1
	#	print P2
	#	print pp
	#	print np
	#	input('training')
		
		result_values = testing(test_set, univocabulary, bivocabulary, P1, P2, upp, unp, bpp, bnp)
		
	#	print result_values
	#	input('result values')

		current_accuracy = getAccuracy(actual_values, result_values)
		print current_accuracy

		accuracy += current_accuracy

	print "Accuracy: ", accuracy/10
