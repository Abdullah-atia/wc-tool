import sys
import os

def word_count(option, file_path = None):
    try:
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                file_name = file.name
        else:
            content = sys.stdin.read()
            file_name = "stdin"

        char_count = len(content)
        word_count = len(content.split())
        line_count = content.count('\n')
        nums_of_byte = len(content.encode('utf-8'))

        if option == "-c":
            return (nums_of_byte ) if file_path is None else (nums_of_byte, file_name)
        elif option == "-l":
            return (line_count ) if file_path is None else (line_count, file_name)
        elif option == "-w":
            return (word_count ) if file_path is None else (word_count, file_name)
        elif option == "-m":
            return (char_count ) if file_path is None else (char_count, file_name)
        else:
            # Return nums_of_byte, line_count, word_count regardless of file_path
            if file_path:
                return nums_of_byte, line_count, word_count, file_name
            else:
                return nums_of_byte, line_count, word_count

    except FileNotFoundError:
        print("File not found!")
        return (0, "File not found!")

def main():
    if not sys.stdin.isatty():
        # stdin input scenario
        option = sys.argv[1] if len(sys.argv) > 1 else ""
        result = word_count(option)
    else:
        if len(sys.argv) < 2:
            print("Usage: python my_wc.py <file_path> [<option>]")
            return
        elif len(sys.argv) == 2:
            file_path = sys.argv[1]
            option = ""
            result = word_count(option, file_path)
        else:
            option = sys.argv[1]
            file_path = sys.argv[2]
            result = word_count(option, file_path)
    
    if result is not None:
        print(result)

if __name__ == "__main__":
    main()
