from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import word_tokenize

def word_to_index(tokens: list[str]) -> dict[str, int]:
    unique_tokens = sorted(set(tokens))
    return {word: i + 1 for i, word in enumerate(unique_tokens)} 
    
def one_hot_encoding(word_index: dict[str, int]) -> list[list[int]]:
    vocab_size = len(word_index)
    result = []
    for word, num in word_index.items():
        lst = [0] * vocab_size
        lst[num - 1] = 1
        result.append(lst)
    return result


tokenizer = TreebankWordTokenizer()
texts = ["The cat saw the cat chasing the mouse while \
        the cat hid behind the tree, and the mouse that \
            the cat was chasing didn't see the other cat \
                watching fence"]

tokens = [token for text in texts for token in tokenizer.tokenize(text)]
A = word_to_index(tokens)
print(A)
text1 = one_hot_encoding(A)
for encoding in text1:
    print(encoding)