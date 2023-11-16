def predict(grammar, state, chart, position):
    for production in grammar:
        if production["lhs"] == state["rhs"][0]:
            chart[position].append({
                "lhs": production["lhs"],
                "rhs": production["rhs"],
                "dot": 0,
                "start": position,
                "origin": position
            })

def scan(state, token, chart, position):
    if state["rhs"][state["dot"]] == token:
        chart[position + 1].append({
            "lhs": state["lhs"],
            "rhs": state["rhs"],
            "dot": state["dot"] + 1,
            "start": state["start"],
            "origin": state["origin"]
        })

def complete(state, chart, position):
    for item in chart[state["origin"]]:
        if item["dot"] < len(item["rhs"]) and item["rhs"][item["dot"]] == state["lhs"]:
            chart[position].append({
                "lhs": item["lhs"],
                "rhs": item["rhs"],
                "dot": item["dot"] + 1,
                "start": item["start"],
                "origin": item["origin"]
            })

def earley_parse(grammar, tokens):
    chart = [[] for _ in range(len(tokens) + 1)]
    start_state = {
        "lhs": grammar[0]["lhs"],
        "rhs": grammar[0]["rhs"],
        "dot": 0,
        "start": 0,
        "origin": 0
    }
    chart[0].append(start_state)

    for position in range(len(tokens) + 1):
        while True:
            added = False
            for state in chart[position]:
                if state["dot"] < len(state["rhs"]) and state["rhs"][state["dot"]] in grammar:
                    predict(grammar, state, chart, position)
                elif state["dot"] < len(state["rhs"]) and state["rhs"][state["dot"]] == tokens[position]:
                    scan(state, tokens[position], chart, position)
                elif state["dot"] == len(state["rhs"]):
                    complete(state, chart, position)
                added = True
            if not added:
                break

    for state in chart[-1]:
        if state["lhs"] == start_state["lhs"] and state["dot"] == len(state["rhs"]):
            return True

    return False

# Example usage
grammar = [
    {"lhs": "S", "rhs": ["NP", "VP"]},
    {"lhs": "NP", "rhs": ["Det", "N"]},
    {"lhs": "VP", "rhs": ["V", "NP"]},
    {"lhs": "Det", "rhs": ["the"]},
    {"lhs": "N", "rhs": ["cat", "dog"]},
    {"lhs": "V", "rhs": ["chased", "ate"]}
]

tokens = ["the", "cat", "chased", "the", "dog"]

if earley_parse(grammar, tokens):
    print("Parsing successful: Valid sentence.")
else:
    print("Parsing failed: Invalid sentence.")
