sentence = input("Enter a sentence: ")

words = sentence.split()
for word in set(words):
    print(word, ":", words.count(word))