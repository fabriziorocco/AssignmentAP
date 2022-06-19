### The following script contains a function to automatize the development of user's choices in the CLI.

def let_user_pick(options):
    print("Please choose: \n")
    for idx, element in enumerate(options):
        print("{}) {}".format(idx+1,element))
    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            return int(i)
    except:
        pass
    return None



