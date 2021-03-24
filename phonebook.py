def welcome():

    entry = int(input("""
        1 - create contact
        2 - delete contact 
        3 - list contact 
        4 - Create its txt file
        5 - quit
    """))
    return entry

contact = []

def phonebook():
    
    infinite()
    

def infinite():
    while True:
        entry = welcome()
        if entry == 1:
            name = input("name : ")
            mob = input('Contact : ')
            contact.append(f'{name}')
            print('\n')
            contact.append(f'{mob}')
            

        if entry == 2:
            del_name = input('name : ')
            num = contact.index(f'{del_name}')
            contact.remove(f'{del_name}')
            num_index = num
            del contact[index]
            
            
        if entry == 3:
            print(f'{contact}')

        if entry == 4:
            file = open('Contact Book.txt', 'a')
            file.writelines(contact)
            file.close()
                      

        if entry == 5:
            return

phonebook()
            










   