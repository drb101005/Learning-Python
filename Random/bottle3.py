# Message in a Bottle - Improved Version

def send_bottle():
    print("🌊 Welcome to the Message in a Bottle simulator!")
    print("----------------------------------------------")
    
    # Ask the user to type a message
    message = input("✍️  Write your message to put in the bottle: ").strip()
    
    if not message:
        print("⚠️  You didn't write anything! Try again next time.")
        return
    
    # Create the bottle as a dictionary
    bottle = {
        "material": "glass",
        "floating": True,
        "message_inside": message
    }

    # Simulate sending the bottle
    print("\n🧴 Sending the bottle out to sea...")
    print("🌊 Bottle Details:")
    print(f"   • Material       : {bottle['material']}")
    print(f"   • Is it floating?: {'Yes' if bottle['floating'] else 'No'}")
    print(f"   • Message inside : \"{bottle['message_inside']}\"")

    print("\n✅ Your message is now drifting across the ocean... 🌍")

# Run the function
send_bottle()
