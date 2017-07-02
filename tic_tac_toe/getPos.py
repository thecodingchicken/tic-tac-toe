def __get_row__(player):
    x='a'
    print("Enter a number from 1 to 3.")
    while type(x) != int:
        x=input("Row for Player %s:  "%player)
        if x=='exit' or x=='quit':
            print("Goodbye.  Please play later.")
            import sys
            sys.exit()
        try:x=int(x)
        except:
            print("Enter a number. ")
            continue
        if not ((3>=x) and (x>=1)):
            print("Enter a number BETWEEN 1 and 3")
            x='a'
    return x-1

def __get_col__(player):
    x='a'
    print("Enter a number from 1 to 3.")
    while type(x) != int:
        x=input("Column for Player %s:  "%player)
        if x=='exit' or x=='quit':
            print("Goodbye.  Please play later.")
            import sys
            sys.exit()
        try:x=int(x)
        except:
            print("Enter a number. ")
            continue
        if not ((3>=x) and (x>=1)):
            print("Enter a number BETWEEN 1 and 3")
            x='a'
    return x-1
