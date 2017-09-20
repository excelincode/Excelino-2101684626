#This is a program to check whether your word is a palindrome or not
print ("Welcome to the Palindrome checker code ver0.1")
Pal = input("Please input your word: ").lower()

if str(Pal) == ''.join(reversed(Pal)):
    print("It is a Palindrome!")
else:
    print("It is NOT a Palindrome!")
#Created in 19/9/17 By Excelino.Fernando
