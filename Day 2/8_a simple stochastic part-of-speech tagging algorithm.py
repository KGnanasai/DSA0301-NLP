# Sample tagged corpus (word, POS) for training the model
tagged_corpus = [
    ("I", "PRON"),
    ("am", "VERB"),
    ("reading", "VERB"),
    ("a", "DET"),
    ("book", "NOUN"),
    (",", "PUNCT"),
    ("and", "CONJ"),
    ("it", "PRON"),
    ("is", "VERB"),
    ("interesting", "ADJ"),
    (".", "PUNCT")
]

# Calculate the word and POS tag frequencies
word_count = {}
pos_count = {}
pos_word_count = {}

for word, pos in tagged_corpus:
    word_count[word] = word_count.get(word, 0) + 1
    pos_count[pos] = pos_count.get(pos, 0) + 1
    if pos in pos_word_count:
        pos_word_count[pos][word] = pos_word_count[pos].get(word, 0) + 1
    else:
        pos_word_count[pos] = {word: 1}

# Calculate the probabilities of each word given a POS tag
word_given_pos_prob = {}
for pos, word_freqs in pos_word_count.items():
    total_words = pos_count[pos]
    word_given_pos_prob[pos] = {word: freq / total_words for word, freq in word_freqs.items()}

# Example sentence to tag
sentence = ["I", "am", "reading", "an", "interesting", "book", "."]

# Stochastic POS tagging based on the probabilities
tagged_sentence = []
for word in sentence:
    max_prob = 0
    likely_tag = "NOUN"  # Default to NOUN if unknown word

    for pos, prob_dict in word_given_pos_prob.items():
        if word in prob_dict and prob_dict[word] > max_prob:
            max_prob = prob_dict[word]
            likely_tag = pos

    tagged_sentence.append((word, likely_tag))

# Display the tagged sentence
print(tagged_sentence)
