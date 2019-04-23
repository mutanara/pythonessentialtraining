#1: SIMPLE WHILE LOOP.
#the loop will continue to appear unless you typed the correct password below.

count = 0
Auth = False

email = input("Please enter your email: ")
password1 = input("Please enter your password: ")
password2 = input("Please re-enter your password: ")                                        )


while password1 != password2:
    count =+1
    print("PASSWORDS ABOVE DO NOT MATCH")
    password1 = input(f"{count}:re-enter your first password: ")
    password2 = input(f"{count}:re-enter the same password as above: ")
    
    if count > 3 : break



#2: COMPLICATED WHILE LOOP
#the loop bring gives you the ability to match your password for three trails,
# then if you fail them, it shows a message that it is calling RIB (Rwanda Investigation Bureau)..

Failed = True
email = input("Please enter your email: ")
password1 = input("Please enter your password: ")
password2 = input("Please re-enter your password: ")

count = 0
while password1 != password2:
    count += 1
    if count > 2 : break
    print("PASSWORDS ABOVE DO NOT MATCH")
    password1 = input(f"{count}:re-enter your first password: ")
    password2 = input(f"{count}:re-enter the same password as above: ")
else:
    Failed = False
print("Calling RIB..." if Failed else "Access guaranteed")    
