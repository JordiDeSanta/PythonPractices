print("Create a username: ")

minimunlength = 6
aprobated = False

# While the password is not aprobated, ask to the user again
while aprobated == False:
    # USername ask
    username = input()
    # Check the number of characters of the introduced username
    if(len(username) < minimunlength):
        print("Please insert an user name with 6 characters minimun")
    else:
        print("Success")
        aprobated = True
        pass
    pass
