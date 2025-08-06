# 3. File character counter
with open("sample.txt", "r") as f:
    text = f.read()

vowels = sum(c.lower() in 'aeiou' for c in text)
consonants = sum(c.lower() in 'bcdfghjklmnpqrstvwxyz' for c in text)
digits = sum(c.isdigit() for c in text)
specials = sum(not c.isalnum() and not c.isspace() for c in text)

print(vowels, consonants, digits, specials)
