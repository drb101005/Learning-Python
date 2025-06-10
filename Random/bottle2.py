# Message in a Bottle - Interactive Version

# Ask the user to write a message
message = input("Write a message to put in the bottle: ")

# Put the message in the bottle (simulated with a dictionary)
bottle = {
    "material": "glass",
    "floating": True,
    "message_inside": message
}

# Simulate sending the bottle
print("\nSending the bottle...")
print("Bottle details:")
print(f"Material: {bottle['material']}")
print(f"Is it floating? {'Yes' if bottle['floating'] else 'No'}")
print(f"Message inside: {bottle['message_inside']}")
