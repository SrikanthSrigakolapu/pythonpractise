print("1.simple addition 2 + 2 is ", 2 + 2)
print("2.normal division 19/3 is ", 19/3)
print("3.with no decimal values:  division 19//3 is ", 19//3)
print("4.with Remainder as value: divison 19%3 is ", 19%3)

#if we dont want to character prefaced by \ to be interpreted as special characters
#Then we can simply specify the raw string
# format of raw string is r'hello \n what '
print("5.With out raw string ")
print("hello \n world ")

print("6.With raw string ")
print(r'hello \n world ')

print("\n7.use of  ''' <string> ''' in python \n")
#we can use ''' <string> '''  to print multiple lines in the same format that is given in print
print('''hello
what is this man
It is fantastic''')


#multiple the string literal
print("\n8. multiple the string literal 3 * 'Value ' ")
print(3 * 'Value ')
print("Note: Cannot be used with variable names")


#string auto concatenation between strings with space gap
print("\n9. string auto concatenation between strings with space gap \"val\" \"ue\" ")
print("val" "ue")
print("Note: Cannot be used with variable names")