def tryy():
    try:
        a = int(input("Enter a number : "))
        return 

    except Exception as e:
        print(e)
        return 0

    finally:
        print("I need this to be printed")
#finally will be run even after the function returns
tryy()

print(__name__)


if __name__ == "__main__":
    # If this code is directly executed by running the file its present in
    print("We are directly running this code")
    tryy()
else:
    print("The code is run in a diff file")


print(__name__)