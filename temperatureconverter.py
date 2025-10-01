def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32  

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9 

def celsius_to_kelvin(c):
    return c + 273.15      

def kelvin_to_celsius(k):
    return k - 273.15      

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15  

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32 

def show_menu():
    print("1.celsius to kelvin and fahrenheit")
    print("2.kelvin to celsius and fahrenheit")
    print("3.fahrenheit to kelvin and celsius")
    print("4.exit")

while True:
    show_menu()
    choice=int(input("Enter your choice "))
    temp=float(input("Enter the quantity of temperature "))
    if choice==1:
        print(f"the kelvin is {celsius_to_kelvin(temp)} and the fahrenheit is {celsius_to_fahrenheit(temp)}")
    elif choice==2:
        print(f"the celsius is {kelvin_to_celsius(temp)} and the fahrenheit is {kelvin_to_fahrenheit(temp)}")
    elif choice==3:
        print(f"the  celsius is {fahrenheit_to_celsius(temp)} and the kelvin is {fahrenheit_to_kelvin(temp)}")
    elif choice==4:
        print("exited")
        break
    else:
        print("invalid choice")