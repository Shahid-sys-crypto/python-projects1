shopping_list=[]
def show_list():
    if len(shopping_list)==0:
        print("the shopping list is empty")
    else:
        for index,item in enumerate(shopping_list):
            print(f"{index+1} - {item}")
print("-----shopping list menu------")
print("1-show menu")
print("2-add an item")
print("3-remove an item")
print("4-clear list")
print("5-exit")
x=True
while(x):
    choice =int(input("enter your choice\n"))
    if(choice==2):
        string=input("enter the new item\n1")
        shopping_list.append(string)
        print("new item is added\n")
    elif(choice==1):
        show_list()
    elif(choice==3):
        ssrr=input("what should i remove")
        shopping_list.remove(ssrr)
    elif(choice==4):
        shopping_list.clear()
    elif(choice==5):
        x=False