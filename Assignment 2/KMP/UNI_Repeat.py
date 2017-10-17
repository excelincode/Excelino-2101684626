def repeat():
    no = ('no') #used for the Decision repeat
    ye = ('yes') #used for the Decision repeat
    rep = input("Don't you still have another simulation to check on, "
                        "do you? ( Yes / No )").lower()
    if rep == ye:
        import KMP_Fix as a
        a.main()
    if rep == no:
        import sys
        print("\n-------------------------------")
        print("Thank you for using this program! Have a nice day! :)")
        input("\nPress 'ENTER' to Exit!")
        sys.exit()
    elif rep != ye and rep != no:
        print("Please, answer the question with 'Yes' or 'No'!")
        repeat()
