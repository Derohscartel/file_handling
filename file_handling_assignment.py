
def create_file(filename):
    try:
        with open(filename, 'w') as file:
            file.write("Hello, World!\n")       # String
            file.write("The answer is: 42\n")   # Number
            file.write("Python file handling is fun!\n")  # String
        print(f"File '{filename}' created and initial content written.")

    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nContents of the file:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append_to_file(filename):
    try:
        with open(filename, 'a') as file:
            file.write("Appending a new line of text.\n")
            file.write("For the love of the game.\n")
            file.write("I love this Game Football to the world.\n")
        print(f"New content appended to '{filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to append to '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    filename = "my_file.txt"

    # Create a new file and write content
    create_file(filename)

    # Read and display the contents of the file
    read_file(filename)

    # Append additional content to the file
    append_to_file(filename)

    # Read and display the updated contents of the file
    read_file(filename)

if __name__ == "__main__":
    main()
