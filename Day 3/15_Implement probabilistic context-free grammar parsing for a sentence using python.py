import nltk
from nltk import PCFG, ViterbiParser

# Define a simple probabilistic context-free grammar for subject-verb agreement
pcfg_rules = """
    S -> NP VP [1.0]
    NP -> Det N [0.5] | N [0.5]
    VP -> V [1.0]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'dog' [0.5] | 'cat' [0.5]
    V -> 'runs' [0.7] | 'barks' [0.3]
"""

# Create a PCFG object
pcfg = PCFG.fromstring(pcfg_rules)

# Create a Viterbi parser for the PCFG
parser = ViterbiParser(pcfg)

def parse_sentence(sentence):
    # Tokenize the input sentence
    tokens = nltk.word_tokenize(sentence)

    # Parse the sentence using the Viterbi parser
    try:
        trees = list(parser.parse(tokens))
        # If parsing is successful, return the most likely parse tree
        return trees[0]
    except ValueError:
        # If parsing fails, print an error message
        print(f"Error: Unable to parse the sentence '{sentence}'")
        return None

# Example usage
if __name__ == "__main__":
    sentence1 = "the dog runs"
    sentence2 = "the cat barks"
    sentence3 = "a dog barks"

    parse_tree1 = parse_sentence(sentence1)
    parse_tree2 = parse_sentence(sentence2)
    parse_tree3 = parse_sentence(sentence3)

    if parse_tree1:
        print(f"Parse tree for '{sentence1}':")
        print(parse_tree1)

    if parse_tree2:
        print(f"Parse tree for '{sentence2}':")
        print(parse_tree2)

    if parse_tree3:
        print(f"Parse tree for '{sentence3}':")
        print(parse_tree3)
