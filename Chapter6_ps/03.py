#A spam comment is defined as a text containing following keywords:
# "Make a lot of money" , "buy now" , "subscribe this" , "click this".
# write a program to detect these spams.

a = "make a lot of monney"
b = "buy now"
c = "subscrive this"
d = "click this"

msg = input("Enter your message : ")

if(a in msg or b in msg or c in msg or d in msg):
    print("This message is a spam")
else:
    print("Not a spam message")