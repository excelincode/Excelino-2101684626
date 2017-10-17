hasil = 0
def main():
    global hasil
    list = []
    x = 0
    i = 1
    while i <= 10:
        print("Please, input your", i ,"number: ")
        n = int(input())
        list.append(n)
        print("Your inputted number: ", n)
        print("Your total number(s) in the list now: ", list)
        print("---------------------------------------\n")
        i = i+1
    for y in range(len(list)):
        if list[x] % 42 == 0:
            x = x + 1
        else:
            hasil += 1
            x = x + 1
    return hasil
def result():
    global hasil
    if hasil == 1:
        print("Your total of distinct numbers is ", hasil)
    else:
        print("Your total of distinct numbers are ", hasil)
    input("\nPlease, 'ENTER' to Exit!")
main()
result()
