from sklearn.feature_extraction.text import CountVectorizer

sentences = ["The cat saw the cat chasing the mouse while the cat hid behing the tree, \
             and the mouse that the cat was chaing didn't see the other cat watching from the fence."]

vectorizer = CountVectorizer()
vectorizer.fit(sentences)
word_bag = vectorizer.vocabulary_
result = vectorizer.transform(sentences).toarray()

print(word_bag)
print(result)