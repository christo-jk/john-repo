try:
    a=int(input("enter a number :"))
    b=int(input("enter another number :"))
    result=a/b
    print("result:",result)
except zerodivisionerror:
    print("error:division by zero is not allowed")
except valueerror:
    print("error:please enter valid integer")
