First_number=input("First:")
Second_number=input("Second:")
Sum=float(First_number)+float(Second_number)
print("Sum="+ str(Sum))

Subtraction=float(First_number)-float(Second_number)
print("Subtraction="+ str(Subtraction))

Multiplication=float(First_number)*float(Second_number)
print("Multiplication="+ str(Multiplication))

Division=float(First_number)/float(Second_number)
print("Division"+ str(Division))

Cube=float(First_number)**float(Second_number)
print("Cube"+ str(Cube))

x=int(input("Please input a number: "))
y=int(input("Please input a number: "))
print(x-y)
print(x+y)
print(x*y)
print(x**y)
if y==0:
   print("Please input a nonzero number")
else:
    print(x/y)
