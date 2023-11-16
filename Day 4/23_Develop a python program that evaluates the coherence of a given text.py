import spacy

def evaluate_coherence(text):
    # Load spaCy English model with full path
    nlp = spacy.load("C:/path/to/en_core_web_sm")

    # Process the input text
    doc = nlp(text)

    # Analyze the dependencies between sentences
    sentence_dependencies = []
    for sent in doc.sents:
        sentence_dependencies.append([token.dep_ for token in sent])

    # Check coherence based on dependencies
    coherence_score = calculate_coherence_score(sentence_dependencies)

    return coherence_score

def calculate_coherence_score(sentence_dependencies):
    # This is a simple example of calculating coherence score based on dependencies
    # You can customize this logic based on your specific requirements

    total_coherence_score = 0
    for i in range(len(sentence_dependencies) - 1):
        common_dependencies = set(sentence_dependencies[i]) & set(sentence_dependencies[i + 1])
        coherence_score = len(common_dependencies) / len(set(sentence_dependencies[i]))
        total_coherence_score += coherence_score

    average_coherence_score = total_coherence_score / (len(sentence_dependencies) - 1)
    return average_coherence_score

# Example usage
if __name__ == "__main__":
    input_text = (
        "Natural language processing (NLP) is a field of artificial intelligence that "
        "deals with the interaction between computers and humans using natural language. "
        "It involves the development of algorithms and models to understand, interpret, "
        "and generate human-like text. NLP applications include machine translation, "
        "chatbots, sentiment analysis, and text summarization."
    )

    # Evaluate coherence
    coherence_score = evaluate_coherence(input_text)

    # Display the results
    print("Input Text:")
    print(input_text)
    print("\nCoherence Score:", coherence_score)
