num1 = 42  #Variable declaration & number

num2 = 2.3   #Variable declaration & float number

boolean = True  #Variable declaration & Bool

string = 'Hello World'   #Variable Declaration & String

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #Variable declaration & List

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #Variable declaration & dictionary

fruit = ('blueberry', 'strawberry', 'banana')  #Variable declaration & tuple

print(type(fruit))  #print & Type

print(pizza_toppings[1])  #print & list Array

pizza_toppings.append('Mushrooms')  #List Add

print(person['name'])  #Print & Dictonary access value

person['name'] = 'George'  #Dictionary change


person['eye_color'] = 'blue'  #Dictionary change

print(fruit[2])  #print & tuple data


#Conditional & print, Contiional & Print
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")


#Conditional & print
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

#for loop 0>stop before 5
for x in range(5):
    print(x)

#for loop 2> stop before 5
for x in range(2,5):
    print(x)

#for loop 2> stop before 10, by 3's
for x in range(2,10,3):
    print(x)


#While Loop w/ Variable declaration
x = 0
while(x < 5):
    print(x)  #print
    x += 1  #incrementing

#Delete the End
pizza_toppings.pop()
pizza_toppings.pop(1)  #delete declared


print(person)  #print declared
person.pop('eye_color')  #delete declared
print(person)  #print declared

#for loop like array
for topping in pizza_toppings:
    if topping == 'Pepperoni':  #Conditional
        continue  #continue
    print('After 1st if statement')   #print
    if topping == 'Olives':
        break   #stop

#function declaration
def print_hello_ten_times():
    for num in range(10):  #for loop 0> up to 10
        print('Hello')  #print


#function call to print
print_hello_ten_times()


#Function Declaration w/ parameter
def print_hello_x_times(x):
    for num in range(x):n  #for loop until x
        print('Hello')   #print

#function call to print up to 4
print_hello_x_times(4)

#function declaration with parameter
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):  #for loop till x
        print('Hello')  #print


#print 10 times
print_hello_x_or_ten_times()

#print to 4
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