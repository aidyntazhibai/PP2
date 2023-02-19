# Create a generator that generates the squares of numbers up to some number N.

# def squares_until_n(n):
#     for i in range(1, n+1):
#         yield i**2   #generator lazy iterator, yield used to return iterator 
    
# n = int(input())

# for squares in squares_until_n(n):
#     print(squares)


# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.



# def print_even_num(n):
#     for i in range(0, n+1): #from zero to n
#         if(i%2==0):
#             yield i

    
# n = int(input())

# for evens in print_even_num(n):
#     print(evens)



# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.



# def some_iter(n):
#     for i in range(0, n+1):
#         if(i % 3 == 0 and i % 4 == 0):
#             yield i

# n = int(input())

# for myit in some_iter(n):
#     print(myit)



# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

# def squares(a, b):
#     for i in range(a, b+1):
#         yield i**2

# a = int(input())
# b = int(input())

# for square in squares(a, b):
#     print(square)

# Implement a generator that returns all numbers from (n) down to 0.


def reversive(n):
    for i in range(n, 0, -1):
        yield i 

n = int(input())

for rev in reversive(n):
    print(rev)




