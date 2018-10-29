# Python is a dynamic typed language because it checks the types at run time
# whereas the static typed languages like Java checks the types at compile time itself
#below is the example why Python is dynamic typed

def dynamic(a):
    if a > 0:
        print("\n\n@@@@ @@@ @@@ Passed @@@ @@@ @@@@\n\n")
    else:
        print("3"+a)

#Below statement gets executed because the interpreter will not enter the error zone
dynamic(1)

#Below statement fails as the interpreter enters the error zone
dynamic(-1)