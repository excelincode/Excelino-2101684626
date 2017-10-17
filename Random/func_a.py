'''
#assigning a function to a variable
def func_a():
    print("a message")
b = func_a()
b

#using return to call out the values
def hypotenuse(n , n2):
    import math
    square_root = math.sqrt(int(n)*int(n2))
    return square_root
print(hypotenuse(81,1))

#If you want to still running the code even though it has a TypeError inside it
def hypotenuse(a , b):
    import math
    try:
        return math.sqrt(a**2+b**2)
    except TypeError:
        return None
print(hypotenuse(2,3)) #two integer
print(hypotenuse("2","3")) #two strings
print(hypotenuse(2,"3")) #one integer and one string

#local variable >> global variable, basically local is higher in priority than the global.
def function():
    a=2
    print (a)
global a
a = 3
function()


n=5
while n != 0:
    print('hello')
    n-=1
    print(n)

'''
#Exercise 4
'''
#https://www.codechef.com/problems/FLOW004
n = input()
print(int(n[0]) + int(n[-1]))
print(n[0]) #First_Index
print(n[-1]) #Second_Index

#https://www.codechef.com/problems/FLOW002
i = 0
cse = int(input())
while i <= cse:
    i = i+1
    n = int(input())
    n2 =  int(input()_
    print("Your total: ", n%n2)

#https://www.codechef.com/problems/CHOPRT
i = 0
cse = int(input())
while i <= cse:
    i = i+1
    n = int(input())
    n2 = int(input())
    if n < n2:
        print("<")
    if n > n2:
        print(">")
    if n == n2:
        print("=")
    else:
        False

'''

'''
#Week3Day3
def calculator(n1 , n2 , op , form):
    try:
        if op == "+":
            hasil = int(n1)+int(n2)
        elif op == "-":
            hasil = int(n1)-int(n2)
        elif op == ":":
            hasil = int(n1)/int(n2)
        elif op == "x":
            hasil = int(n1)/int(n2)
        else:
            hasil = int(n1)+int(n2)

        if form == "integer":
            print(int(hasil))
        if form == "float":
            print(float(hasil))
        elif form != "integer" and form != "float":
            print("Please, input the format!")
        return hasil
    except ValueError:
        print("Please, input the data correctly!")
n1 = input("Please, input your first number: ")
n2 = input("Please input your second number: ")
op = input("Please input your operator (+ or - or : or x): ")
form = input("Please input the format you want (integer or float): ").lower()
calculator(n1 , n2 , op , form)

def calculator(n1 , n2 , form, x = None, y=None):
    x.append(n1)
    y.append(n2)
    if x == None or y == None or form == None:
        print("Please, make sure your input or format is not NULL!")
    elif x != None  or y != None and form == "integer":
        print("Your addition of two numbers: " + int(x)+int(y))
        print("Your subtraction of two numbers: " + int(x)-int(y))
        print("Your multiplication of two numbers: " + int(int(x)*(y)))
        print("Your divison of two numbers: " + int(int(x)/int(y)))
    elif x != None  or y != None and form == "float":
        print("Your addition of two numbers: " + int(x)+int(y))
        print("Your subtraction of two numbers: " + int(x)-int(y))
        print("Your multiplication of two numbers: " + int(int(x)*(y)))
        print("Your divison of two numbers: " + int(int(x)/int(y)))
    return

go = calculator(input("Your First Number: ") ,  input("Your Second Number: "), input("Your format: "))

def calculator(operation = "add",format = "float", *number):
    if number:
        result = number[0]
        if operation == "add" or operation == "+" or operation == "addition" or operation == "":
            for i in number[1:]:
                result += i
        elif operation == "subs" or operation == "sub" or operation == "subtraction" or operation == "-":
            for i in number[1:]:
                result -= i
        elif operation == "multi" or operation == "multiplication" or operation == "*" or operation == "x":
            for i in number[1:]:
                result *= i
        elif operation == "div" or operation == "division" or operation == "/":
            for i in number[1:]:
                result /= i

        if format == "int" or format == "integer":
            return print(int(round(result)))
        elif format == "float" or format == "decimal" or format == "":
            return print(float(result))
    else:
        raise Exception("Input is empty!")


def check(num):
    digits = []
    if num == "":
        return digits
    elif len(num) == 1:
        digits.append(int(num))
        return digits
    elif "," in num:
        num = num.split(",")
        print(num)
        for i in num:
            if "." in i:
                digits.append(float(i))
            elif "." not in i:
                digits.append(int(i))
        return digits
    elif " " in num:
        num = num.split(" ")
        for i in num:
            if "." in i:
                digits.append(float(i))
            elif "." not in i:
                digits.append(int(i))
        return digits
    elif "." in num:
        digits.append(float(num))
        return digits

num = input("type your number,for ex(6,4,9,1 or 6 4 9 1): ")
number = check(num)
operation = input("Operation: ")
format = input("Format: ")
calculator(operation,format,*number)
'''

def swap(a,b):
    result =  a,b = b,a
    return result
print(swap(3,7))
print(swap(4,5))

def swap(a,b):
    print(b,a)
swap(3,7)
