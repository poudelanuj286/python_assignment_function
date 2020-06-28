array1 = [1, 2, 3, 5, 7, 8, 9, 10]
array2 = [1, 2, 4, 8, 9]
print("first arrays:")
print(array1)
print(array2)
insect = list(filter(lambda x: x in array1, array2))
print ("\nIntersection of the said arrays: ",insect)
