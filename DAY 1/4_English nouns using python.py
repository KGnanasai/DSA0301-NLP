class PluralizationFSM:
    def __init__(self):
        self.state = 0
    
    def transition(self, char):
        if self.state == 0 and char == 's':
            self.state = 1
        elif self.state == 0 and char == 'y':
            self.state = 2
        elif self.state == 0 and char.isalpha():
            self.state = 3
    
    def pluralize(self, word):
        self.state = 0
        self.word = word
        
        self.transition(word[-1])
        if self.state == 1:
            return self.word + 'es'  # Add "es" for words ending in 's'
        elif self.state == 2:
            return self.word[:-1] + 'ies'  # Change 'y' to 'ies' for words ending in 'y'
        elif self.state == 3:
            return self.word + 's'  # Add "s" for regular pluralization


# Example usage
pluralizer = PluralizationFSM()
words = ['cat', 'dog', 'bus', 'city', 'baby', 'class', 'glass']

for word in words:
    plural_form = pluralizer.pluralize(word)
    print(f"Singular: {word}, Plural: {plural_form}")
