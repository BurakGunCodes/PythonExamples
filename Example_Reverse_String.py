



from traceback import print_tb
import StackClass

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
str = StackClass.Stack()

for char in string:
    str.push(char)

while not str.is_empty():
    reversed_string += str.pop()
    

print(reversed_string)

# # Your solution here.
# while(str.is_empty() == True):
#     reversed_string += str.pop()
    

# print(reversed_string)