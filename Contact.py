infos = {}
while True:
    print("""
--------------------------------------------------------------------------------
Contact Management
1- Add a contact
2- View Contact
3- Edit a contact
4- Exit
""")
    c = int(input("Please choose a number from 1-4: "))

    if c == 1:
        id = input("Enter the ID: ")
        name = input("Please type a name: ")
        phone = input("Please type a phone number: ")
        if phone.isdigit():
            infos[id] = {"name":name, "phone":phone}
        else:
            while phone.isdigit() == False:
                phone = input("Please enter a valid number: ")
                if phone.isdigit():
                    infos['phone'] = phone
        print(f"{name} was added successfully..")
    elif c == 2:
        print(infos)
    elif c == 3:
        id = input("Please enter an ID edit: ")
        if id in infos:
            name = input("Enter a new name: ")
            phone = input("Enter a new number: ")
            if phone.isdigit():
                infos[id] = {"name":name, "phone":phone}
            else:
                while phone.isdigit() == False:
                    phone = input("Please enter a valid number: ")
                    if phone.isdigit():
                        infos[id] = {"name":name, "phone":phone}
            print("Success ...")
        else:
            print(f"Sorry, {id} was not found ....")
    elif c == 4:
        print("Exiting the program....")
        break
    else:
        print("Invalid Choice")
