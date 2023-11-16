import spacy

def semantic_analysis(sentence):
    # Load spaCy English model
    nlp = spacy.load("en_core_web_sm")

    # Process the input sentence
    doc = nlp(sentence)

    # Extract noun phrases and their meanings
    noun_phrases_and_meanings = []
    for chunk in doc.noun_chunks:
        noun_phrase = chunk.text
        # Replace this with your own logic for obtaining meanings based on noun phrases
        meaning = get_meaning_for_noun_phrase(noun_phrase)
        noun_phrases_and_meanings.append((noun_phrase, meaning))

    return noun_phrases_and_meanings

def get_meaning_for_noun_phrase(noun_phrase):
    # Replace this with your own logic for obtaining meanings based on noun phrases
    # For this example, a simple mapping is used
    meaning_mapping = {
        "the cat": "a domesticated carnivorous mammal",
        "a dog": "a domesticated carnivorous mammal",
        "the book": "a set of written or printed pages, usually bound with a protective cover",
    }
    return meaning_mapping.get(noun_phrase, "Meaning not found")

# Example usage
if __name__ == "__main__":
    input_sentence = "The cat and a dog are sitting on the mat. The book is on the shelf."

    # Perform syntax-driven semantic analysis
    results = semantic_analysis(input_sentence)

    # Display the results
    print("Input Sentence:", input_sentence)
    print("\nSemantic Analysis:")
    for noun_phrase, meaning in results:
        print(f"{noun_phrase} - {meaning}")
