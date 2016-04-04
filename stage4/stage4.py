from train import training
import pickle

review_file = open('data.txt', 'r')
vocabulary_file = open('vocabulary.txt', 'r')
model_file = open('model', 'wb')

reviews = review_file.read().splitlines()
vocabulary = vocabulary_file.read().splitlines()

(P1, P2, pp, np) = training(reviews, vocabulary)
a = (P1, P2, vocabulary, pp, np)

pickle.dump(a, model_file)
model_file.close()
