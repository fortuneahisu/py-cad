# A simple local intent dictionary mapping variations to a single standardized keyword
stem_dictionary = {
    "calculating": "math",
    "calculate": "math",
    "computations": "math",
    "compute": "math",
    "+": "math",
    "chatting": "talk",
    "gossip": "talk",
    "sup": "talk",
    "vibe": "talk"
}

message = input("Speak: ").lower().split()

# Normalize the user's words based on your custom local stem map
normalized_tokens = [stem_dictionary.get(word, word) for word in message]

print(f"Original: {message}")
print(f"Normalized: {normalized_tokens}")
# Now your bots only have to check for "math" or "talk" instead of 50 different variations!
