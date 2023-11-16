import nltk
from nltk import word_tokenize, pos_tag

# Download required resources (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample text for part-of-speech tagging
text = "NLTK is a leading platform for building Python programs to work with human language data."

# Tokenize the text into words
words = word_tokenize(text)

# Perform part-of-speech tagging
pos_tags = pos_tag(words)

# Display the result
for word, pos_tag in pos_tags:
    print(f"Word: {word}, POS Tag: {pos_tag}")
