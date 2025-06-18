# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

try:
    # Using 'with' statement ensures the file is properly closed after use
    with open("Chapter9/01/file.txt", "r") as file:
        # Read and process file contents here
        contents = file.read()
        print("File contents:")
        print(contents)
        
except FileNotFoundError:
    print("Error: The file 'file.txt' was not found in the current directory.")
    print("Please make sure the file exists in the same folder as this script.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")