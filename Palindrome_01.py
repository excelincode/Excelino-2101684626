#This is a program to check whether your word is a palindrome or not

print ("Welcome to the Palindrome checker code ver0.2a!")
no = ('no')
ye = ('yes')
def main():
    while True:
        Pal = input("\nPlease input your word: ").lower()
        if str(Pal) == ''.join(reversed(Pal)):
            print("Yes! the word of ' " +Pal , "' is a Palindrome! :)")
            rep = input("Don't you still have other word to check on, do you? ( Yes / No )").lower()
            if rep == ye:
                main()
            if rep == no:
                return
            else:
                print("Please, answer the question with 'Yes' or 'No'!")
        else:
            print("Unfortunately! the word of ' " +Pal , "' is NOT a Palindrome! :(")
            rep = input("Don't you still have other word to check on, do you? ( Yes / No )").lower()
            if rep == ye:
                main()
            if rep == no:
                return
            else:
                print("Please, answer the question with 'Yes' or 'No'!")
main()
print("\n-------------------------------")
print("Thank you for using this program! Have a nice day! :)")
input("\nPress 'ENTER' to Exit!")

#Created in 19/9/17 By Excelino.Fernando
#Updated to version 0.2a in 21/9/17 By Excelino.Fernando
'''
#0.1 just a code to run a Palindrome word for a time
#0.2a added some User Interface to let user whether to continue with other word or not, still unstable with some issues
'''
