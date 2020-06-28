def ran_check(num,low,high):
    for i in range(low,high+1):
        if num==i:
            print('Number is within the range')
            break
    else :
            print ('Number is out of range')

n = int(input("enter  a number to be checked"))
h = int(input("enter  high range be checked"))
l = int(input("enter  lowest  range be checked"))
ran_check(n,h,l)