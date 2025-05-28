'''We Going to make a Dictionary(for Eng to Hindi)!!!'''

eng_to_hindi = {
    "Hello" : "Namaste",
    "Bye" : "Alvaida",
    "Mother" : "Maaaaaa",
    "Father" : "Papaaa",
    "Tommrow" : "Kal",
    "Later" : "Badme"
}

word = input("Enter the word(Hello,Bye,Mother,Father,Tommrow,Later): ")

if(word in eng_to_hindi):

    print(f"The translation of the {word} in hindi is {eng_to_hindi[word]}")
else:
    print("Error, Word is not in the list Pal")

