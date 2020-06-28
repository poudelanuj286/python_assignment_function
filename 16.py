list1 = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]
print("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, list1))
print(square_nums)
print("\nCube every number of the said list:")
cube_nums = list(map(lambda x: x ** 3, list1))
print(cube_nums)