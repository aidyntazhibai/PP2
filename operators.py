#there is a list of operators

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic operators
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #reminder
print(a**b) #a^b
print(a//b) #division to nearest whole num sam thing with 

#assignment operators to make it shorter

	# x += 3	same as  x = x + 3	
	# x -= 3	same as  x = x - 3	
	# x *= 3	same as  x = x * 3	
	# x /= 3	same as  x = x / 3	
	# x %= 3	same as  x = x % 3	
	# x //= 3	same as  x = x // 3	
	# x **= 3	same as  x = x ** 3


# Comparison operators

# Equal	                    x == y	
# Not equal	                x != y	
# Greater than	            x > y	
# Less than	                x < y	
# Greater than or equal to	x >= y	
# Less than or equal to	    x <= y


# Logical operators
x=5
print(x < 5 and  x < 10)         #if both of them true
print(x < 5 or x < 4)            #if at least of of them
print(not(x < 5 and x < 10))     #negative and

# Identity operators

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y



# Membership operators



x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list



# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
# ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off



# IF ELSE

x=3
y=1

if x>y:
    print("YOOOO")

#but you cannot write like that
# if x>y:
# print("YOOOO")  

#and like else if in cpp

if x>y:
    print("YOOOO")
elif x==y:
    print("JOOO")

#and else

if x>y:
    print("YOOOO")
else:
    print("JOOOO")   

#we can add or conditions

if x>y and x==y:
    print("YOOOO")
else:
    print("JOOOO")

if x>y or x==y:
    print("YOOOO")
else:
    print("JOOOO")

#we can add condition in condition

if x>y:
    if x>5:
        print("JasonStatham")

#pass statement leave it empty

a = 33
b = 200

if b > a:
  pass