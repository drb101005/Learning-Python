no_of_vids = int(input("Enter the number of videos: "))
def counter():
    done = int(input("Enter the number of vids done so far: "))

    percentage_completed = (done / no_of_vids) * 100

    print(percentage_completed)

while True:
    counter()