def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


s = input("enter a string")

print("The original string  is : ", s)

print("The reversed string is : ", reverse(s))
