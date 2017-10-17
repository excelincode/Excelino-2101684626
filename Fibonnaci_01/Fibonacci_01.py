print ("Welcome to the Fibonnaci calculator code ver0.1")
def fibonnaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (fibonnaci (n-1) + fibonnaci (n-2))
print(fibonnaci(int(input("Please input your number: "))))
'''
print ("Welcome to the Fibonnaci calculator code ver0.1")
storage = []
x = int(input("Please input your number: "))
f0 = f1 = 0
f2 = 1
for num in range (x):
    f0 = f1 + f2
    f2 = f1
    f1 = f0
    storage.append(str(f0))
print (num)
'''
