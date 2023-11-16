# Define transformation rules for part-of-speech tagging
transformation_rules = [
    (r'\b[A-Z][a-z]*\b', 'NOUN'),  # Proper nouns
    (r'\b[a-z]+(s|es)\b', 'NOUN'),  # Plural nouns
    (r'\b[a-z]+\b', 'NOUN'),  # Singular nouns
    (r'\b[AaIiEeOoUu]+\b', 'NOUN'),  # Single-letter words (A, I, a, etc.)
    (r'\b\d+\b', 'NUM'),  # Numbers
    (r'\b[AaIiEeOoUu]+\b', 'PRON'),  # Pronouns (I, you, he, she, it)
    (r'\b[WeYy]\b', 'PRON'),  # More pronouns (we, you, they)
    (r'\b(are|am|is)\b', 'VERB'),  # Present tense verbs
    (r'\b(was|were)\b', 'VERB'),  # Past tense verbs
    (r'\b([Hh]ave|[Hh]as)\b', 'VERB'),  # Present perfect verbs
    (r'\b[Oo]ne\b', 'NUM'),  # The number one
    (r'\b[a-z]+[aeiou]ing\b', 'VERB'),  # Present participle verbs
    (r'\b[a-z]+[aeiou]ed\b', 'VERB'),  # Past participle verbs
    (r'\b[a-z]+\b', 'ADJ'),  # Adjectives
    (r'\b[.,!?;]\b', 'PUNCT'),  # Punctuation
]

# Sample sentence for transformation-based tagging
sentence = "The quick brown fox jumps over the lazy dog. They are happy."

# Initialize an empty list to store tagged words
tagged_words = []

# Apply transformation rules to tag words
for word in sentence.split():
    tagged = False
    for pattern, tag in transformation_rules:
        if re.match(pattern, word):
            tagged_words.append((word, tag))
            tagged = True
            break
    if not tagged:
        tagged_words.append((word, 'UNKNOWN'))  # Default to UNKNOWN if no match

# Display the tagged sentence
print(tagged_words)
