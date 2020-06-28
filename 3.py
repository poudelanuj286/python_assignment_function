def mul():
    prod = 1
    num = int(input('How many numbers: '))
    for n in range(num):
        numbers = int(input('Enter number '))
        #lst.append(numbers)
        prod = prod * numbers
    return prod
print("product of elements in given list is :", mul())