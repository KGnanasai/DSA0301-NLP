class SimpleParser:
    def __init__(self):
        self.grammar = {
            'expr': ['term + expr', 'term'],
            'term': ['factor * term', 'factor'],
            'factor': ['( expr )', 'number'],
            'number': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        }
        self.start_symbol = 'expr'

    def parse(self, input_string):
        self.input = input_string
        self.current_index = 0

        try:
            self.parse_expression(self.start_symbol)
            if self.current_index == len(self.input):
                print("Parsing successful: Valid expression.")
            else:
                print("Parsing failed: Invalid expression.")
        except ValueError:
            print("Parsing failed: Invalid expression.")

    def parse_expression(self, non_terminal):
        for production in self.grammar[non_terminal]:
            original_index = self.current_index

            for token in production.split():
                if token in self.grammar:
                    self.parse_expression(token)
                else:
                    self.match_terminal(token)

            return

        self.current_index = original_index
        raise ValueError("Parsing error")

    def match_terminal(self, terminal):
        if self.input[self.current_index] == terminal:
            self.current_index += 1
        else:
            raise ValueError("Parsing error")

# Example usage
parser = SimpleParser()
expression = "2 * (3 + 4)"
parser.parse(expression)
