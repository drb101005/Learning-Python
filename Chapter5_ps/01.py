# English to Hindi Dictionary Program

# Define the dictionary
eng_to_hindi = {
    "hello": "नमस्ते",
    "world": "दुनिया",
    "apple": "सेब",
    "book": "किताब",
    "computer": "कंप्यूटर",
    "water": "पानी",
    "food": "भोजन",
    "friend": "मित्र",
    "love": "प्यार",
    "mother": "माँ"
}

print("We Going to make a Dictionary (for Eng to Hindi)!!!")
print("Type 'exit' to quit the program.\n")

while True:
    word = input("Enter an English word: ").strip().lower()
    
    if word == "exit":
        print("Exiting the dictionary. धन्यवाद!")
        break
    elif word in eng_to_hindi:
        print(f"The Hindi translation of '{word}' is: {eng_to_hindi[word]}\n")
    else:
        print(f"Sorry, '{word}' is not in the dictionary.\n")
