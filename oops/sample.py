from calculator import calculator


class extendedclass(calculator):
    pass




#with inheritance
inheritedSample = extendedclass()
print("\n\n\bInherited class  \b")
print("Subtraction Value of two elements is ", inheritedSample.addtwo(32,32, 2))
print("Addition Value of two elements is ", inheritedSample.addtwo(32, 2))
#intantiate the python object
sample = calculator()
print("Value of two elements is ", sample.addtwo(32, 2))
