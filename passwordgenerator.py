import random,string
def generate_password(length):
    if(length<4):
        raise ValueError("password cannot be less than 4 letters")
    uppercase=string.ascii_uppercase
    lowercase=string.ascii_lowercase
    digits=string.digits
    all_chars=uppercase+lowercase+digits
    password=[
    ]
    for i in range(length):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    fast="".join(password)
    print(fast)
try:
    length=int(input("Enter the length of the password"))
    generate_password(length)
except ValueError as a:
    print(a)
finally:
    print("the password is generated successfully")



