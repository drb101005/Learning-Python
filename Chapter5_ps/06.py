friend1 = input("Enter your name: ")
friend2 = input("Enter your name: ")
friend3 = input("Enter your name: ")
friend4 = input("Enter your name: ")

lang1 = input(f"Enter your fav language {friend1} :")
lang2 = input(f"Enter your fav language {friend2} :")
lang3 = input(f"Enter your fav language {friend3} :")
lang4 = input(f"Enter your fav language {friend4} :")

dic = {
    friend1 : lang1,
    friend2 : lang2,
    friend3 : lang3,
    friend4 : lang4
}

question = input("Enter the name of friend whos lang do you want to know :")

print(dic[question])

print(dic)