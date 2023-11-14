name="iheb"
# - variable declaration
age = 12
# - log statement
print(age)
# - type check
print(type(age)) 
# - length check
# print(len(age))
# - comment
#     - single line  #SINGLE LINE
#     - multiline 
"""                              
This is a comment             
                                
written in
more than just one line
"""
# - Data Types
#        - Primitive
# int float boolean Strings
#         - Boolean 
a=True
#         - Numbers
a=20
#         - Strings
a="lol"
#     - Composite
#         - List 
#             - initialize 
list=["dhia","myman"]
#             - access value
print(list[0])
#             - change value
list[0]="itskk"
#             - add value
list.append("dhia")
#             - delete value
print(list)
list.pop()
print(list)
#         - Tuples
#             - initialize
tup = ('Elcapon','Elpacho')
#             - access value
print(tup[0])
#             - change value
#error
#             - add value
#error
#             - delete value
#error
#         - Dictionary
#             - initialize
dicRollsRoyce={"Color":"Ultra White","Doors":"4","Buyer":"OussamaJomaa","Phone":"50171466" }
#             - access value
print(dicRollsRoyce.get("Doors"))
#             - change value
dicRollsRoyce["Buyer"]="SadikZrelli"
print(dicRollsRoyce)
#             - add value
dicRollsRoyce.update(PersonalLogo="LALO",Doors="3")
dicRollsRoyce.pop("Color")
print(dicRollsRoyce)
#             - delete value
#dicRollsRoyce.pop("Phone")
dicRollsRoyce.update(PersonalLogo='')
print(dicRollsRoyce)
# - conditional
a=19
b=20
#     - if 
if(b>a):
    print("i like you")
#     - else if
elif(a==19):
    print("i hate you")
#     - else
else:
    print("lets go on date")
# - for loop
for x in range(5):
    print(x)
#     - start
#1
#     - stop
#4
#     - increment
#default 1
#     - break
for j in range (1,20,1):
    if(j==10):
        print(j)
    break
#     - continue
#     - sequence
# - while loop
#     - start
#     - stop
#     - increment
# - function
#     - parameter
#     - argument
#     - return

# * Bonus: Errors

# - NameError: name <variable name> is not defined
# - TypeError: 'tuple' object does not support item assignment
# - KeyError: 'favorite_team'
# - IndexError: list index out of range
# - IndentationError: unexpected indent
# - AttributeError: 'tuple' object has no attribute 'pop'
# - AttributeError: 'tuple' object has no attribute 'append'
# - Tuples
#     - change value
#     - add value
#     - delete value


