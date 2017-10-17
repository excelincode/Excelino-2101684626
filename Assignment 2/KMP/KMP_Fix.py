import UNI_Repeat as rep
print("Welcome to Long to Short variatons converter ver0.2a!")
def main():
    print("-------------------------------")
    n = input("Please, DO your input in this form (Name1-Name2-NameX)!\nYour input, please: ")
    print("These are the inputted names:\n", n)
    print("This is the shortened variations: ")
    print(''.join(fix[0] for fix in n.split("-"))) #Looping all the inputted names and split it
main()
rep.repeat()
