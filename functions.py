# 1.A recipe you are reading states how many grams you need for the ingredient. 
# Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams

# def grams_to_ounces(grams):
#     return grams * 0.035274
# print(grams_to_ounces(500))


# def grams_to_ounces():
#     grams = float(input("Enter the weight in grams: "))
#     ounces = grams * 0.035274
#     print(grams, "grams is equivalent to", ounces, "ounces")

# grams_to_ounces()




# 2.Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)


# def convert(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius
# print(convert(500))



# 3.Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
# How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

# def solve(numheads, numlegs):
#     for num_rabbits in range(numheads + 1):
#         num_chickens = numheads - num_rabbits
#         if (num_rabbits * 4 + num_chickens * 2) == numlegs:
#             return (num_chickens, num_rabbits)
#     return (None, None)

# numheads = 35
# numlegs = 94

# chickens, rabbits = solve(numheads, numlegs)
# if chickens is None:
#     print("No solution found")
# else:
#     print("Number of chickens:", chickens)
#     print("Number of rabbits:", rabbits)


