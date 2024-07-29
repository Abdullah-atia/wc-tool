my_wc.py is a Python script that counts characters, words, lines, and bytes in a given file or from standard input. It functions similarly to the Unix wc (word count) command, providing various options to output specific counts.

Usage
bash
Copy code
python my_wc.py <option> <file_path>
<option>: Specifies the type of count to display. Possible options are:
-c: Number of bytes
-l: Number of lines
-w: Number of words
-m: Number of characters
<file_path>: Path to the file to be analyzed. If omitted, the script will read from standard input.
If no option is provided, the script returns the number of bytes, lines, and words.

Options
-c: Count and display the number of bytes.
-l: Count and display the number of lines.
-w: Count and display the number of words.
-m: Count and display the number of characters.
Examples
Count from a File
Count the number of lines in a file:

bash
Copy code
python my_wc.py -l example.txt
Count the number of words in a file:

bash
Copy code
python my_wc.py -w example.txt
Count the number of characters in a file:

bash
Copy code
python my_wc.py -m example.txt
Count the number of bytes in a file:

bash
Copy code
python my_wc.py -c example.txt
Get all counts (bytes, lines, and words) in a file:

bash
Copy code
python my_wc.py example.txt
Count from Standard Input
Count the number of lines from standard input:

bash
Copy code
echo "Hello World" | python my_wc.py -l
Count the number of words from standard input:

bash
Copy code
echo "Hello World" | python my_wc.py -w
Count the number of characters from standard input:

bash
Copy code
echo "Hello World" | python my_wc.py -m
Count the number of bytes from standard input:

bash
Copy code
echo "Hello World" | python my_wc.py -c
Script Explanation
The script defines two main functions: word_count and main.

word_count(option, file_path=None)
This function performs the counting based on the provided option and file path (if any):

If file_path is provided, it reads the content of the file.
If file_path is not provided, it reads the content from standard input.
It then calculates the number of characters, words, lines, and bytes.
Based on the specified option, it returns the appropriate count. If no option is specified, it returns all counts.
main()
This function handles the command-line interface:

It checks if the input is provided via standard input or as command-line arguments.
If input is from standard input, it reads the option and calls word_count.
If input is from command-line arguments, it reads the option and file path, and then calls word_count.
It prints the result returned by word_count.
Handling Errors
If the specified file is not found, the script will print "File not found!" and return (0, "File not found!").

Requirements
Python 3.x