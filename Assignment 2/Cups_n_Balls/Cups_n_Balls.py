def main():
    import sys
    a = 1
    b = c = i = 0
    n = input("Please, input your series of alphabets (A/B/C): ").lower()
    for i in range(len(n)): #will keep processing the data until the final input data or n[-1]
        if n[i] == "a": #if the n[i] is "a" it will swap the [a,b] to [b,a]
            a,b = b,a
        if n[i] == "b": #if the n[i] is "b" it will swap the [b,c] to [c,a]
            b,c = c,b
        if n[i]  == "c": #if the n[i] is "c" it will swap the [a,c] to [c,a]
            a,c = c,a
        elif n[i] != "a" and n[i] != "b" and n[i] != "c":
            print("Pattern is unidentified!")
            sys.exit()
        else:
            i=i+1
    print(a,b,c)
    if a == 1:
        print("The ball is in the first cup.")
    if b == 1:
        print("The ball is in the second cup.")
    if c == 1:
        print("The ball is in the third cup")
    else:
        False
main()
