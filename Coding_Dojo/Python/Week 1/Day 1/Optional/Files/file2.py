num1 = 42 #         - Numbers
num2 = 2.3 #         - Numbers
boolean = True #         - Boolean 
string = 'Hello World' #         - Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionnair
fruit = ('blueberry', 'strawberry', 'banana') #tuple
print(type(fruit))   #output: tuple type check
print(pizza_toppings[1]) # access value
pizza_toppings.append('Mushrooms') # -
fruit.append('slata meshwia')
print(person['name']) #'John'
person['name'] = 'George' #change value
person['eye_color'] = 'blue' #add value
print(fruit[2]) #banana

if num1 > 45: #if statment
    print("It's greater")
else:
    print("It's lower")
    #its lower

if len(string) < 5:
    print("It's a short word!") #false
elif len(string) > 15:
    print("It's a long word!") #false 
else:
    print("Just right!") # true


for x in range(5):
    print(x) #0,1,2,3,4 
for x in range(2,5):
    print(x) #2,3,4
for x in range(2,10,3):
    print(x) #2,5,8
x = 0
while(x < 5):
    print(x)
    x += 1
#0,1,2,3,4

pizza_toppings.pop() #mashroum deleted
pizza_toppings.pop(1) #sausage

print(person) #console log the person
person.pop('eye_color') #deleted
print(person) #person without eyecolor

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)