with open("Chapter9/01/PS/text_for_editing.txt", "r") as f:
          content = f.read()

content_new = content.replace("donkey" , "D#####")

with open("Chapter9/01/PS/text_for_editing.txt", "w") as f:
          f.write(content_new)