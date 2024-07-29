wc_tool.py is a Python script that counts characters, words, lines, and bytes in a given file or from standard input. It functions similarly to the Unix wc (word count) command, providing various options to output specific counts.

Usage
bash
Copy code
python wc_tool.py <option> <file_path>
1. <option>: Specifies the type of count to display. Possible options are:
- -c: Number of bytes
- -l: Number of lines
- -w: Number of words
- -m: Number of characters
2. <file_path>: Path to the file to be analyzed. If omitted, the script will read from standard input.
If no option is provided, the script returns the number of bytes, lines, and words.

Examples
Count from a File
Count the number of lines in a file:


```
python wc_tool.py -l test.txt
```
Count the number of words in a file:

```
python wc_tool.py test.txt
```
Count from Standard Input
Count the number of lines from standard input:

```
cat test.txt | python wc_tool.py -l
```
Count the number of words from standard input:


Script Explanation

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