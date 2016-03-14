def training(reviews, vocabulary):
	N = len(reviews)	#	number of reviews
	N1 = 0			#	number of positive reviews
	N2 = 0			#	number of negative reviews
	
	positiveReview = ''	#	super doc for positive reviews
	negativeReview = ''	#	super doc for negative reviews

	for review in reviews:
		if review[0] == '+':
			N1 += 1
			positiveReview += ' ' + review[1:] 
		else:
			N2 += 1
			negativeReview += ' ' + review[1:]
	

	P1 = (1.0 * N1)/N		#	p(+)	
	P2 = (1.0 * N2)/N		#	p(-)	

	positiveProbabilities = []	#	p(word|+)	
	negativeProbabilities = []	#	p(word|-)	
	
	totalCountInPositive = 0
	totalCountInNegative = 0

	for word in vocabulary:
		totalCountInPositive += positiveReview.count(word) + 1
		totalCountInNegative += negativeReview.count(word) + 1

	for word in vocabulary:
		positiveCount = positiveReview.count(word) + 1
		positiveProbabilities.append((1.0 * positiveCount)/totalCountInPositive)	#	(count(word in +) + 1) / sum of (count(word' in +) + 1)

		negativeCount = negativeReview.count(word) + 1
		negativeProbabilities.append((1.0 * negativeCount)/totalCountInNegative)	#	(count(word in -) + 1) / sum of (count(word' in -) + 1)
	
	return (P1, P2, positiveProbabilities, negativeProbabilities)
	 
