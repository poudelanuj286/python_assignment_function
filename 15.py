list1 = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]

# if divisible by 13 or not
result = list(filter(lambda x: (x % 13 == 0), list1))

# printing the result
print(result)