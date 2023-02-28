import re

# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

string = input("Enter a string: ")

pattern = r'a[b]*'

if re.search(pattern, string):
    print("Match found!")
else:
    print("No match found.")


# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.


string = input("Enter a string: ")

pattern = r'a[b]{2,3}'

if re.search(pattern, string):
    print("Match found!")
else:
    print("No match found.")

# Write a Python program to find sequences of lowercase letters joined with a underscore.


string = input("Enter a string: ")

pattern = r'[a-z]+_[a-z]+'

matches = re.findall(pattern, string)

if matches:
    print("Matches found:")
    for match in matches:
        print(match)
else:
    print("No matches found.")

# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

def findSequences(string):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, string)
    return sequences

# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

def matchstring(string):
    pattern = r'a.*b$'
    match = re.match(pattern, string)
    return bool(match)

# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

def replaceChars(string):
    replace_chars = ' ,.'
    replacement = ':'

    for char in replace_chars:
        string = string.replace(char, replacement)
    
    return string

# Write a python program to convert snake case string to camel case string.

def myfunc(string):
    words = string.split('_')
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    
    return camel_case

# Write a Python program to split a string at uppercase letters.

def split(string):
    split_string = []
    start_index = 0
    for i in range(len(string)):
        if string[i].isupper():
            split_string.append(string[start_index:i])
            start_index = i
    split_string.append(string[start_index:])
    return split_string

# Write a Python program to insert spaces between words starting with capital letters.

def insertSpaces(string):
    new_string = ""
    for i in range(len(string)):
        if i > 0 and string[i].isupper() and string[i-1].islower():
            new_string += " "
        new_string += string[i]
    return new_string

# Write a Python program to convert a given camel case string to snake case.

def myfunc(string):
    snake_string = ""
    for i in range(len(string)):
        if string[i].isupper() and i > 0:
            snake_string += "_"
        snake_string += string[i].lower()
    return snake_string