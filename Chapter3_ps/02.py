name = input("Enter your name:")
date = float(input("Enter todays date :"))


string_value = str(date)

letter = '''        Dear <|Name|>
	You are selected!
	On- <|Date|>.2025'''

print(letter.replace("<|Name|>", name).replace("<|Date|>", string_value))
#print(letter.replace("<|Date|>", string_value))

