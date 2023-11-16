from nltk.corpus import wordnet

def explore_word_meanings(word):
    # Get synsets for the given word
    synsets = wordnet.synsets(word)

    if not synsets:
        print(f"No synsets found for '{word}'.")
        return

    print(f"Synsets for '{word}':")
    for synset in synsets:
        print(f" - Definition: {synset.definition()}")
        print(f" - Part of speech: {synset.pos()}")
        print(f" - Examples: {', '.join(synset.examples())}")
        print()

    # Explore hypernyms and hyponyms of the first synset
    first_synset = synsets[0]
    print(f"Hypernyms of '{word}':")
    for hypernym in first_synset.hypernyms():
        print(f" - Hypernym: {hypernym.name()} - Definition: {hypernym.definition()}")

    print(f"\nHyponyms of '{word}':")
    for hyponym in first_synset.hyponyms():
        print(f" - Hyponym: {hyponym.name()} - Definition: {hyponym.definition()}")

# Example usage
if __name__ == "__main__":
    # Word to explore
    target_word = "car"

    # Explore word meanings using WordNet
    explore_word_meanings(target_word)
