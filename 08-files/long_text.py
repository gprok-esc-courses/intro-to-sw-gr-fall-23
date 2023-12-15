
file = open("long_text.txt")

lines = file.readlines()

sentence_counter = 0
word_counter = 0

for line in lines:
    sentences = line.strip().split('.')
    for sentence in sentences:
        if sentence != '':
            sentence_counter += 1
            words = sentence.strip().split(' ')
            word_counter += len(words)

print("Sentences: ", sentence_counter)
print("Words:", word_counter)