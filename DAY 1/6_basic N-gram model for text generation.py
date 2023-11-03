import random

# Sample text for training the bigram model
corpus = "This is a simple example of a bigram model. A bigram is a sequence of two words."

# Tokenize the text into words
words = corpus.split()

# Create a dictionary to store bigrams and their following words
bigrams = {}
for i in range(len(words) - 1):
    word, next_word = words[i], words[i + 1]
    if word in bigrams:
        bigrams[word].append(next_word)
    else:
        bigrams[word] = [next_word]

# Generate text using the bigram model
start_word = random.choice(words)  # Choose a random starting word
generated_text = [start_word]

while len(generated_text) < 20:  # Generate 20 words
    current_word = generated_text[-1]
    if current_word in bigrams:
        next_word = random.choice(bigrams[current_word])
        generated_text.append(next_word)
    else:
        break

# Join the generated words to create the final text
generated_text = ' '.join(generated_text)

# Display the generated text
print(generated_text)
