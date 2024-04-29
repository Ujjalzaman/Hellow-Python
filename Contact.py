contact = {}

def showfunction():
    print(contact.items())
    print("Name \t Cotact")
    for key in contact:
        print("{} \t {}".format(key, contact.get(key)))


while True:
    chose = int(input("1. Add new contact \n "
                  "2. Search the contact \n "
                  "3. Display the contact \n "
                  "4. Edit the contact \n "
                  "5. Delete the contact \n "
                  "6. Exit \n"
                  "Please write number between 1-6: "
                 ))
    
    if chose == 1:
        name = input("Add your contact name: ")
        phone = int(input("Add your phone number: "))
        contact[name] = phone
    
    elif chose == 2:
        contactName = input("Search the contact : ")

        if contactName in contact:
            print(contactName, "Contact number is , ", contact[contactName])
        
        else:
            print("Contact is not found ")
    
    elif chose == 3:
        if not contact:
            print("contact book s empty")
        else:
            showfunction()
    
    elif chose == 4:
        editcontact = input("Edit Your Contact : ")
        if editcontact in contact:
            phone = input("Change your Number: ")
            contact[editcontact] = phone
            print("Phone number changed")

    elif chose == 5:
        delContact =  input("Which contact would you like to delete ? ")
        if delContact in contact:
            deleteConfirm = input("Are you sure ? [y/n]")

            if deleteConfirm == 'y' or deleteConfirm == 'Y':
                contact.pop(delContact)
                showfunction()
            else:
                print("the name is not found in the contact")
    
    else :
        break