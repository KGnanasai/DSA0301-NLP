from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def lesk_algorithm(word, context):
    best_sense = None
    max_overlap = 0

    # Tokenize the context and remove stopwords
    context_words = set(word_tokenize(context.lower()))
    stop_words = set(stopwords.words('english'))
    context_words = [word for word in context_words if word not in stop_words]

    # Iterate over the senses of the word in WordNet
    for sense in wordnet.synsets(word):
        # Combine words from the definition and examples
        sense_words = set(word_tokenize(sense.definition().lower()))
        sense_words.update([word.lower() for example in sense.examples() for word in word_tokenize(example)])

        # Remove stopwords
        sense_words = [word for word in sense_words if word not in stop_words]

        # Calculate the overlap between the context and the sense
        overlap = len(set(context_words).intersection(set(sense_words)))

        # Update the best sense if the overlap is greater
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense

# Example usage
if __name__ == "__main__":
    target_word = "bank"
    context = "He went to the bank to deposit his money."

    # Perform Word Sense Disambiguation using the Lesk algorithm
    result_sense = lesk_algorithm(target_word, context)

    if result_sense:
        print(f"Target word: {target_word}")
        print(f"Context: {context}")
        print(f"Best sense: {result_sense.name()} - {result_sense.definition()}")
    else:
        print(f"No suitable sense found for the target word.")
