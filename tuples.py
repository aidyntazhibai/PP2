#same thing as lists
fruits = ("apple", "banana", "cherry")
print(fruits[0])

fruits = ("apple", "banana", "cherry")
print(len(fruits))

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#only diff tuple inchangable thus when we want change it convert it to list

listfruits=list(fruits)
listfruits[0]="nonapple"
fruits=tuple(listfruits)
print(fruits)