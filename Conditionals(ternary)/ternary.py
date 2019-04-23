hungry = True
SIMPLE TERNARY EXAMPLE

1ST EXAMPLE
x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
print(x)


2ND EXAMPLE
a , b = 10, 20
max = b if a <= b else a
print(max)

Another way of writting it:
if a <= b:
    max = b
    print(b)
else:
    print(a)


NESTED TERNARY OPERATOR

first way:
print("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a") 

second_way:
if a != b:
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than b")
else:
    print("both a and b are equal")

