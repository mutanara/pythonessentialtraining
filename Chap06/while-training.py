
secret = "swordfish"
pw = ""
count = 0
auth = False

while pw != secret:
    count += 1   # always remember to put this while loop controller first
    if count > 3: break
    pw = input(f" {count}:What's the secret word? : ")
else:
    auth = True
print("Authorized" if auth else "Calling the FBI ...")


