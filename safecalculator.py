def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divi(a,b):
    if(b==0):
        raise ZeroDivisionError("the number zero cannot be divided by")
    return a/b
def show_menu():
    print("\n---Safe calculator---\n")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.division")
    print("5.exit")
while True:
    show_menu()
    choice=int(input("Enter your choice"))
    if choice==5:
        print("successfully exited the program")
    try:
        num1=int(input("Enter the first number"))
        num2=int(input("Enter the second number"))
        if(choice==1):
            print("result=",add(num1,num2))
        elif(choice==2):
            print("result=",sub(num1,num2))
        elif(choice==3):
            print("result=",multi(num1/num2))
        elif(choice==4):
            print("result=",divi(num1/num2))
        else:
            print("invalid choice")
    except ValueError:
        print("invalid input")
    except ZeroDivisionError as e:
        print("ZeroDivisionError called")
    except Exception as g:
        print(g)
    finally:
        print("the safe calculator is working")
