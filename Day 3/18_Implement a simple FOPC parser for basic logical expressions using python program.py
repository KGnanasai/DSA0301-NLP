import re

class FOPCParser:
    def __init__(self):
        self.tokens = []
        self.current_token = None

    def tokenize(self, expression):
        # Tokenize the FOPC expression
        self.tokens = re.findall(r'\(|\)|\w+|[\>\<\=\!]\=|\&\&|\|\|', expression)
        self.tokens = [token.strip() for token in self.tokens]

    def parse(self, expression):
        self.tokenize(expression)
        self.current_token = None

        # Start parsing
        result = self.parse_expression()

        # Check if there are any remaining tokens
        if self.current_token is not None:
            raise SyntaxError(f"Unexpected token: {self.current_token}")

        return result

    def get_next_token(self):
        if not self.tokens:
            return None
        self.current_token = self.tokens.pop(0)
        return self.current_token

    def parse_expression(self):
        token = self.get_next_token()

        if token == '(':
            # Recursive case for compound expressions
            result = self.parse_compound_expression()
        else:
            # Base case for atomic expressions
            result = token

        return result

    def parse_compound_expression(self):
        operator = self.get_next_token()
        operands = []

        while self.current_token != ')':
            operand = self.parse_expression()
            operands.append(operand)

        # Consume the closing parenthesis
        self.get_next_token()

        return {'operator': operator, 'operands': operands}

# Example usage
if __name__ == "__main__":
    fopc_parser = FOPCParser()

    # Example FOPC expression: (P(x) && Q(y)) || R(z)
    fopc_expression = "(P(x) && Q(y)) || R(z)"

    try:
        parsed_result = fopc_parser.parse(fopc_expression)
        print("Parsed FOPC expression:")
        print(parsed_result)
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
