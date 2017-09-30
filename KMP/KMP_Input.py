n_list = [] #null list for inserting the values
sn_list = [""] #storage null list for saving the original name(s)
def in_1(x): #in_1 = input_1, the first input for user
    global n_list
    global sn_list
    name_1 = str(input("Please input your first LAST name: "))
    print("Your inputted name: ", name_1)
    sn_list += name_1
    n_list += name_1[0]

def in_x(y): #in_x = input_x, the x so input for user
    global n_list
    global sn_list
    name_x = str(input("Please input the next LAST name: "))
    print("Your inputted name: ", name_x)
    sn_list += name_x
    n_list += name_x[0]
    print("-------------------------------")

def in_repeat(): #in_repeat = input_repeat, repeat the "in_x" until user END it
    import KMP_Input as a
    global n_list
    global sn_list
    no = ('no') #used for the Decision repeat
    ye = ('yes') #used for the Decision repeat
    print("-------------------------------")
    print("Your current name(s) in the list:", ''.join(sn_list).title())
    rep = input("Don't you still have another name to add in, "
                        "do you? ( Yes / No )").lower()
    print("-------------------------------")
    if rep == ye:
        print("Your current name(s) in the list: ", sn_list)
        print("-------------------------------")
        a.in_x(a)
    if rep == no:
        print("These are the Original Variations names: ")
        print(''.join(sn_list).title())
        print("-------------------------------")
        print("This is the Shortened Variations name: ")
        print(''.join(n_list).upper())
        print("-------------------------------")
    else:
        print("Please, answer the question with 'Yes' or 'No'!")
        print("-------------------------------")
        a.in_repeat()
