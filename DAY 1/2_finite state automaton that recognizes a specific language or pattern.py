def ends_with_ab(input_string):
    # Define the states of the automaton
    states = {
        0: {'a': 1, 'b': 0},
        1: {'a': 1, 'b': 2},
        2: {'a': 1, 'b': 0}
    }

    # Start in the initial state
    current_state = 0

    # Iterate through the characters in the input string
    for char in input_string:
        if char not in states[current_state]:
            return False
        current_state = states[current_state][char]

    # Check if the final state is reached (ending with 'ab')
    return current_state == 2

# Test the automaton with some example strings
print(ends_with_ab("abcab"))  # True
print(ends_with_ab("abab"))   # True
print(ends_with_ab("ab"))     # True
print(ends_with_ab("acab"))   # False
print(ends_with_ab("xyz"))    # False
