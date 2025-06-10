# Message in a Bottle - Simple Python Code

# Define a message to put in the bottle
message = "Hello from across the sea!"

# Put the message in the bottle (a dictionary for this example)
bottle = {
    "material": "glass",
    "floating": True,
    "message_inside": message
}

# Send the bottle (simulated by printing)
print("Sending the bottle...")
print("Bottle details:")
print(f"Material: {bottle['material']}")
print(f"Is it floating? {'Yes' if bottle['floating'] else 'No'}")
print(f"Message inside: {bottle['message_inside']}")