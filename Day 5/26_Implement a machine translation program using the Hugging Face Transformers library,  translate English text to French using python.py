from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, model_name="Helsinki-NLP/opus-mt-en-fr"):
    # Load pre-trained translation model and tokenizer
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokenize input text
    input_ids = tokenizer.encode(text, return_tensors="pt")

    # Perform translation
    translation_ids = model.generate(input_ids)

    # Decode and return the translated text
    translated_text = tokenizer.decode(translation_ids[0], skip_special_tokens=True)
    
    return translated_text

# Example usage
if __name__ == "__main__":
    # English text to be translated
    english_text = "Hello, how are you? This is a sample translation."

    # Translate English to French
    french_translation = translate_text(english_text)

    # Display the results
    print("Input (English):")
    print(english_text)
    print("\nTranslation (French):")
    print(french_translation)
