import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag

def recognize_dialog_acts(dialog):
    dialog_acts = []

    # Tokenize sentences
    sentences = sent_tokenize(dialog)

    for sentence in sentences:
        # Tokenize words and perform part-of-speech tagging
        words = word_tokenize(sentence)
        pos_tags = pos_tag(words)

        # Recognize dialog acts based on patterns (customize as needed)
        dialog_act = recognize_dialog_act(pos_tags)
        dialog_acts.append((sentence, dialog_act))

    return dialog_acts

def recognize_dialog_act(pos_tags):
    # Define simple patterns for recognizing dialog acts
    question_words = ['what', 'when', 'where', 'who', 'whom', 'whose', 'which', 'why', 'how']
    modal_verbs = ['can', 'could', 'will', 'would', 'shall', 'should', 'may', 'might', 'must']
    greetings = ['hi', 'hello', 'hey']
    affirmatives = ['yes', 'yeah', 'yep', 'sure']
    negatives = ['no', 'nope', 'nah']

    # Check for question patterns
    if pos_tags[0][0].lower() in question_words or pos_tags[0][1] == 'MD':
        return 'question'

    # Check for imperative patterns
    if pos_tags[0][1] == 'VB' or pos_tags[0][1] == 'MD':
        return 'imperative'

    # Check for greetings
    if pos_tags[0][0].lower() in greetings:
        return 'greeting'

    # Check for affirmatives
    if pos_tags[0][0].lower() in affirmatives:
        return 'affirmative'

    # Check for negatives
    if pos_tags[0][0].lower() in negatives:
        return 'negative'

    # Default case
    return 'statement'

# Example usage
if __name__ == "__main__":
    dialog = (
        "User: Hi, how are you?\n"
        "Chatbot: I'm doing well, thank you!\n"
        "User: Can you help me with something?\n"
        "Chatbot: Sure, what do you need help with?\n"
        "User: When is the deadline for the project?\n"
        "Chatbot: The deadline is next Friday.\n"
        "User: Great, thanks!\n"
    )

    # Recognize dialog acts
    dialog_acts = recognize_dialog_acts(dialog)

    # Display the results
    print("Dialog Acts:")
    for sentence, dialog_act in dialog_acts:
        print(f"{dialog_act.capitalize()}: {sentence}")
