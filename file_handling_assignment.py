def create_file():
    """Creates a new text file and writes initial content."""
    try:
        # Create a new text file named "my_file.txt" in write mode
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("Hello, my name is valary.\n")
            file.write("Here is my age number: 21\n")
            file.write("I am a student at power learn project africa.\n")
        print("File 'my_file.txt' created and initial content written.")
    
    except (PermissionError, OSError) as e:
        print(f"Error creating file: {e}")
    finally:
        print("Finished attempting to create the file.")

def read_file():
    """Reads the contents of the file and displays them on the console."""
    try:
        # Read the contents of "my_file.txt"
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Contents of 'my_file.txt':")
            print(content)
    
    except FileNotFoundError:
        print("File 'my_file.txt' does not exist. Cannot read the file.")
    except (PermissionError, OSError) as e:
        print(f"Error reading file: {e}")
    finally:
        print("Finished attempting to read the file.")

def append_to_file():
    """Appends additional content to the existing file."""
    try:
        # Open "my_file.txt" in append mode
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text
            file.write("I am from Nairobi, Kenya.\n")
            file.write("My tribe is Luhya which has sub tribes amounting to: 17\n")
            file.write("Am happy to be in this program: Goodbye!\n")
        print("Additional lines appended to 'my_file.txt'.")
    
    except (PermissionError, OSError) as e:
        print(f"Error appending to file: {e}")
    finally:
        print("Finished attempting to append to the file.")

if __name__ == "__main__":
    create_file()    # Step 1: Create the file
    read_file()      # Step 2: Read and display contents
    append_to_file() # Step 3: Append additional content
    read_file()      # Step 4: Read and display updated contents again