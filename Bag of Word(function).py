import re
from nltk.tokenize import word_tokenize

def vector_word_of_bag(sents: list[str]) -> list[list[int]]:
    sents = [re.sub("[^a-zA-Z0-9\s]", "", sent) for sent in sents]
    tokens: list[list[str]] = [word_tokenize(sent) for sent in sents]
    
    word_bag: dict[str, int] = {}
    for token in sum(tokens, []):
        if token not in word_bag.keys():
            word_bag[token] = len(word_bag)
    print(word_bag)
    
    result: list[list[int]] = []
    for sent in tokens:
        temp: list[int] = []
        for word in word_bag.keys():
            if word in sent:
                temp.append(sent.count(word))
            else:
                temp.append(0)
        result.append(temp)
    return result

sentences = ["The cat saw the cat chasing the mouse while the cat hid behing the tree, \
             and the mouse that the cat was chaing didn't see the other cat watching from the fence."]
vectors = vector_word_of_bag(sentences)

for vector in vectors:
    print(vector)