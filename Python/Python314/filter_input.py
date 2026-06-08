"""Aiming to complete mousousammys input filter independently"""


def and_filter(message):
    "Targets only and"
    message = message.split()
    output = []
    for items in message:
        items = items.strip()
        output.append(items)
    try:
        output.remove("and")
    except ValueError as err:
        print(err)
    return output


def negator(message):
    """Targetting negators"""
    if isinstance(message, str) is not list:
        message = message.split()
    output = []
    for items in message:
        items = items.strip()
        output.append(items)
    try:
        output.remove("not")
        output.remove("don't")
        output.remove("won't")
    except ValueError as err:
        print(err)
    return output


def pass_input():
    """Final input filter"""
    message = input("Input: ").strip().lower()
    conjunc_sect = and_filter(message)
    print(negator(conjunc_sect))


item = and_filter(
    'Oba, Me and TK fucked around until "and" '
    "literally died, not . This was all a lie, not the truth"
)
print(negator(item))
