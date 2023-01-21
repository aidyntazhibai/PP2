#string used by quotation
a="Hello world"
print(a)
#we can use loong text by multiple quotes
a="""Almatyda jok jok
Aqtobede jok jok
seni izdedim
umitty uzbedim
"""
print(a)
#or with single quotes
a='''Menimen bile,denendi bos usta
bul diskoteka iz devianostyh
Magnitafondy, barina kosta
Oinasyn ander iz devianostyh
'''

print(a)

#there is no char in python so single character in python is str with lenghts of 1
#so we can use arrays
a="Aidyn"
print(a[0])

#also we can use loops for str

for x in "abcd":
    print(x)

#we can know lenght by len()operator

a="Erlanagai"
print(len(a))

#also check phrase
a="let me tell u samtin"
print("samtin" in a)
#its bool

#also
a="let me tell u samtin"
print("samtin" not in a)

#there is opportunity to slice string (cut them in given range)

a="adcefkbtukfvf"
print(a[5:9])

#if we leave first index it will show till the end (second one not included)
a = "kbtukfvf"
print(a[:4])

#same thing

a = "adcefkbtu"
print(a[5:])

# in the negative numbers it start from the end first index not included second included

a="adcefkbtukfvf"
print(a[-4:-8])

#upper used to switch all letters to uppercase

a = "ya uchus v kbtu"
print(a.upper())

#and lower in same way

a = "YA AITISHNIK"
print(a.lower())

#strip method used to delete all spaces in the beginning and end

a = "    Etu sumku mne muzh kupil            "
print(a.strip()) # returns "Hello, World!"

# and other operators

a = "KAP KARASHKA"
print(a.replace("K", "S"))

a = "AIDYNsTAzhybay"
print(a.split("s"))

a = "Erlan"
b = "Karabalyev"
c = a + b
print(c)

a = "Aaso"
b = "Zero"
c = a + " " + b
print(c)

ret = 4
txt = "I have {} retakes"
print(txt.format(ret))

# or we can just

ret = str(4)
txt = "overall retakes"
print(txt + " " + ret)

ret = 2
fx = 2
nb = 11
txt = "I have {} retakes {} fx and {} nb"
print(txt.format(ret, fx, nb))

txt = "Da agai ya \"uchu\" ppshku"
print(txt)

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning



