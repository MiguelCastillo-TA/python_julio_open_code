allUsers = [
    {
        "name": "Miguel Castillo",
        "email": "miguel@email.com"
    },
    {
        "name": "Ana Rodriguez",
        "email": "ana@email.com"
    },
    {
        "name":  "Richard Torres",
        "email": "richard@email.com"
    }
]

flag = True
while(flag):
    print(f"WELCOME! PLEASE CHOOSE AN OPTION")
    print("*"*30)
    print("1. View Users")
    print("2. Add User")
    print("3. Remove User")
    print("4. To exit")
    print('\n')

    option = int(input("Select your option \n"))

    if option == 1:
        for user in allUsers:
            print(user)

    elif option == 2:
        print('ADDING NEW USER')
        userName = input('What is the user name?')
        userEmail = input('What is the user email?')
        print(userName, userEmail)
        ##########################
        newUser = {
            "name":  userName,
            "email": userEmail
        }
        allUsers.append(newUser)
        print("NEW USER ADDED")

    elif option == 3:
        print('Please enter the index or name of user to delete')
        userToDelete = input("User ID or Name\n")

        try:
            userToDelete = int(userToDelete) # if it fails to moves on to catch
            deletedUser = allUsers.pop(userToDelete)
            print(f"The following was deleted: \n {deletedUser}")
            
        except:
            for index, user in enumerate(allUsers):
                if user["name"] == userToDelete:
                    deletedUser = allUsers.pop(index)
                    print(f"The following was deleted: \n {deletedUser}")

    elif option == 4:
        flag = False
    print('\n')