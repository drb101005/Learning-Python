no_of_vids = int(input("Enter the number of videos: "))   
done = int(input("Enter the number of vids done so far: "))

def counter():
    global done  

    percentage_completed = (done / no_of_vids) * 100
    print(f"Progress: {percentage_completed:.2f}%")

    change = input("Increase or decrease (i/d): ").lower()  
    if change == 'i':
        if done < no_of_vids:
            done += 1
        else:
            print("All videos are already completed.")
    elif change == 'd':
        if done > 0:
            done -= 1
        else:
            print("You can't go below 0 videos.")
    else:
        print("Invalid input. Use 'i' to increase or 'd' to decrease.")

while True:
    counter()
