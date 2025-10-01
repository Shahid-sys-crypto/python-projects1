contact={}
def show_menu():
    print("------options-------")
    print("1-add contact")
    print("2-view contact")
    print("3-search contact")
    print("4-delete contact")
    print("5-exit")

def add_contact():
    name=input("enter your name\n")
    number=int(input("enter your number\n"))
    place=input("enter your place\n")
    contact[name]={"number":number,"place":place}
    print(f"successfully added the contact of {name}\n")

def view_contact(): 
    if contact:
        print("-------your contact list-------\n")
        for key,value in contact.items():
            print(f"name:{key}")
            print(f"number:{value['number']}")
            print(f"place:{value['place']}\n\n")
    else:
        print("contact list is empty\n")
def search_contact():
    name=input("enter the name to be searched\n")
    if name in contact:
        print(f"name:{name}")
        print(f"number:{contact[name]['number']}")
        print(f"place:{contact[name]['place']}")
    else:
        print("not found")
def edit_contact():
    name=input("enter the name\n")
    number=int(input("enter the number\n"))
    place=input("enter the place\n")
    contact[name]={"number":number,"place":place}
    print(f"successfully uptated {name} contact\n")
def delete_contact():
    name=input("enter the name\n")
    if name in contact:
        del contact[name]
        print(f"successfully deleted the {name} contact\n")
    else:
        print(f"the {name} contact no found\n")
while True:
    show_menu()
    num=int(input("enter the choice\n"))
    if(num==1):
        add_contact()
    elif(num==2):
        view_contact()
    elif(num==3):
        search_contact()
    elif(num==4):
        delete_contact()
    elif(num==5):
        break

