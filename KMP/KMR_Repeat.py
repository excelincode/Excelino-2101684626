def repeat_sys():
    no = ('no') #used for the Decision repeat
    ye = ('yes') #used for the Decision repeat
    rep = input("Don't you still have another simulation to check on, "
                        "do you? ( Yes / No )").lower()
    if rep == ye:
        main()
    if rep == no:
        print("\n-------------------------------")
        print("Thank you for using this program! Have a nice day! :)")
        input("\nPress 'ENTER' to Exit!")
    else:
        print("Please, answer the question with 'Yes' or 'No'!")
        repeat_sys()
