import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required resources (if not already downloaded)
nltk.download('punkt')
nltk.download('wordnet')

# Sample text
text = "The quick brown foxes jumped over the lazy dogs. They are running in the park."

# Tokenize the text into words
words = word_tokenize(text)

# Initialize the WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Perform morphological analysis (lemmatization) on each word
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Display the original words and their lemmatized forms
print("Original Words:", words)
print("Lemmatized Words:", lemmatized_words)
