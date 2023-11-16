import nltk

def resolve_references(text):
    sentences = nltk.sent_tokenize(text)
    resolved_text = []

    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        tagged_tokens = nltk.pos_tag(tokens)

        # Use the default nltk English parser for named entity recognition
        named_entities = nltk.ne_chunk(tagged_tokens, binary=True)

        resolved_sentence = resolve_sentence_references(named_entities)
        resolved_text.append(resolved_sentence)

    return ' '.join(resolved_text)

def resolve_sentence_references(tree):
    resolved_sentence = []

    for subtree in tree:
        if isinstance(subtree, nltk.Tree):
            # If the subtree is a named entity, replace with the entity label
            if subtree.label() == 'NE':
                entity_label = ' '.join(word for word, pos in subtree.leaves())
                resolved_sentence.append(entity_label)
            else:
                resolved_sentence.append(resolve_sentence_references(subtree))
        else:
            # If the leaf is a word, include it in the resolved sentence
            resolved_sentence.append(subtree[0])

    return ' '.join(resolved_sentence)

# Example usage
if __name__ == "__main__":
    input_text = "John saw Mary, and he gave her a book. The book was interesting."

    # Perform reference resolution
    resolved_text = resolve_references(input_text)

    # Display the results
    print("Input Text:")
    print(input_text)
    print("\nReference Resolution:")
    print(resolved_text)
