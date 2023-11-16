import nltk
from nltk import CFG, ChartParser

# Define a simple context-free grammar for subject-verb agreement
grammar_rules = """
    S -> NP VP
    NP -> Det N
    VP -> V
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'runs' | 'barks'
"""

# Create a CFG object
grammar = CFG.fromstring(grammar_rules)

# Create a parser for the CFG
parser = ChartParser(grammar)

def check_agreement(sentence):
    # Tokenize the input sentence
    tokens = nltk.word_tokenize(sentence)

    # Parse the sentence using the CFG parser
    try:
        trees = list(parser.parse(tokens))
        # If parsing is successful, the sentence adheres to the grammar rules
        return True
    except ValueError:
        # If parsing fails, the sentence violates the grammar rules
        return False

# Example usage
if __name__ == "__main__":
    sentence1 = "the dog runs"
    sentence2 = "the cat barks"
    sentence3 = "a dog barks"

    print(f"Is '{sentence1}' grammatically correct? {check_agreement(sentence1)}")
    print(f"Is '{sentence2}' grammatically correct? {check_agreement(sentence2)}")
    print(f"Is '{sentence3}' grammatically correct? {check_agreement(sentence3)}")
