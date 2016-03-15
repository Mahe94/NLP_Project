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

def testing(test_list, v, P1, P2, pp, np):
	result_value = []
	for test in test_list:
		test = test.split()
		
		sum_of_pprob = 0
		sum_of_nprob = 0
		for word in test:
			if vocabulary.count(word):
				index = vocabulary.index(word)
				sum_of_pprob += math.log1p(pp[index])
				sum_of_nprob += math.log1p(np[index])

		positiveProbability = sum_of_pprob + math.log1p(P1)
		negativeProbability = sum_of_nprob + math.log1p(P2)

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

vocabulary_file = open('vocabulary.txt', 'r')
vocabulary = vocabulary_file.read().splitlines()
reviews_file = open('data.txt', 'r')
reviews = createParts(reviews_file.read().splitlines())

accuracy = 0
for i in range(10):
	actual_values = []
	for review in reviews[i]:
		test_set = review[1:]
		actual_values.append(review[0])
	
	training_set = []
	for j in range(10):
		if i != j:
			training_set.extend(reviews[j])
	
	P1, P2, pp, np = training(training_set, vocabulary)
	
	result_values = testing(test_set, vocabulary, P1, P2, pp, np)

	current_accuracy = getAccuracy(actual_values, result_values)
	print current_accuracy

	accuracy += current_accuracy

print accuracy/9
