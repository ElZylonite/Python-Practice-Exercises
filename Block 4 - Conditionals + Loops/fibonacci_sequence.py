n = int(input("Enter the length of the Fibonacci sequence: "))
a = 0
b = 1


for i in range(0,n):
    print(a)
    a, b = b, a + b   

