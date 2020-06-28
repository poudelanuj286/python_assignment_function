def add():
    lst = []
    num = int(input('How many numbers: '))
    for n in range(num):
        numbers = int(input('Enter number '))
        lst.append(numbers)
    return lst
print("Sum of elements in given list is :", sum(add()))