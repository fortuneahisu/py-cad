"""Aiming to complete mousousammys input filter independently"""


def and_filter(message):
    "Targets only and"
    message = message.split(" and ")
    output = []
    for sentence in message:
        sentence = sentence.strip()
        output.append(sentence)
    return output


def negator(message):
    """Targetting negators"""
    negators = ["not", "un", "don't", "won't"]
    not_output = []
    for grammar in negators:
        not_filter = message.split(grammar)
        for standalone in not_filter:
            not_output.append(standalone.strip())
        return not_output


def pass_input():
    """Final input filter"""
    message = input("Input: ").strip().lower()
    conjunc_sect = and_filter(message)
    print(negator(conjunc_sect))


print(and_filter("hkjj"
))
# for line in init_output:
#     print(negator(line))
