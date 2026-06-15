sentence = "this is a test this is only a test"
words = sentence.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
