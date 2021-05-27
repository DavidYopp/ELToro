
numbersList = [1,2,3,4,5,6,7,8,9,10]

#testing by using modulo
#modulo tests if the number is divisible by 2
#if it is the program tells us it is even
#if not then the program tells us that it is odd
for num in numbersList:
    if num % 2 == 0:
        print("{} is even".format(num))
    else:
        print("{} is odd".format(num))

#testing by using division
#by default python returns a floating point on divide operations
#this is unless we use integer division by specifying two division symbols
#but if the floating point decimal is .0 is_integer will still return true
for num in numbersList:
    if (num/2).is_integer():
        print("{} is even".format(num))
    else:
        print("{} is odd".format(num))
