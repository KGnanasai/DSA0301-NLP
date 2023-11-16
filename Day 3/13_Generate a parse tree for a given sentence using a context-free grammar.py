import nltk
from nltk import CFG
from nltk.parse.chart import ChartParser

# Define a context-free grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP
    Det -> 'the'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'ate'
""")

# Create a ChartParser with the grammar
parser = ChartParser(grammar)

# Input sentence
sentence = "the cat chased the dog"

# Tokenize the sentence
tokens = sentence.split()

# Parse the sentence
parse_trees = list(parser.parse(tokens))

# Display the parse trees
for tree in parse_trees:
    tree.pretty_print()
