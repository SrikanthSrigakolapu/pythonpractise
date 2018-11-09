#a simple python script to practise try and catch feature

try:
    print("hello try catch")
    #print(1/0)
except Exception as e:
    print("caught you")
    print(e)
finally:
    print("even though you have an exception I am always here")
