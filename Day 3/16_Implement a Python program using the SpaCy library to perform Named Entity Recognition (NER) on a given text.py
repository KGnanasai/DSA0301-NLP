import spacy

def perform_ner(text):
    # Load the spaCy English NER model
    nlp = spacy.load("en_core_web_sm")

    # Process the text using spaCy NER
    doc = nlp(text)

    # Extract named entities from the processed document
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return entities

# Example usage
if __name__ == "__main__":
    # Example text
    text = "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne. It is headquartered in Cupertino, California."

    # Perform Named Entity Recognition
    named_entities = perform_ner(text)

    # Display the named entities and their types
    print("Named Entities:")
    for entity, entity_type in named_entities:
        print(f"{entity} - {entity_type}")
