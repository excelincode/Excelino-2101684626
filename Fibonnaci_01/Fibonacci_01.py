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
