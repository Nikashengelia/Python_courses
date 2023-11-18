#1 what is the function used to display text in python? -print
print()

#2  - In Python, which data type is used to store a whole number?  -int  როიმელიც ინახავს მთელ რიცხვებს
age = 15
print(type(age))


#3 - Which of the following data types is used to store text in Python? - string
name = "Nikoloz"
print(type(name))

#4What is the result of the expression 10 + 5 * 2 in Python? - პირველად რიგში სრულდება გამრავლება შემდეგ მიღებულ პასუხს ვუმატებთ 10-ს და პასუხია 20
print(10 + 5 * 2)


#5  Which of the following is the correct way to assign the value 42 to a variable named answer in Python? - პირველ რიგში  შემოგვაქვს  რაიმე ცვლადი და შემდეგ  მას ვანიჭებთ  რაიმე მნიშვნელობას,
answer=42
print(answer)

#6 - What is the process of identifying and fixing errors in a program called? - debugging
# name = nikoloz - არასწორია
name = "Nikoloz" # - სწორია
print(name)


#7 - Which is commonly used in Python for naming variables and functions, where words are separated by underscore? -ამას ქვია  snake_case
first_name = "Nika"
print(first_name)


#8 -What is the primary purpose of adding comments to your Python code? - კომენტარები ჩვენ გვეხმარება რომ გავიგოთ კოდი და ეს არამარტო ჩვენ არამედ სხვა პროგრამისტებსაც ეხმარება რომ გაიგონ კოდი.


#9 - How can you take user input in Python? - ამისთვის ჩვენ გვჭირდება input()
name =input("what's your name?")
print(name)

#10 - Which of the following is not a built-in data type in Python? - აქედან array არ არის ჩაშენებული მონაცემთა ტიპი


#11 - What function can be used to check the data type of a variable in Python? - მონაცემთა ტიპი რომ შევამოწმოთ ჩვენ გვჭირედება type()
x = 300
print(type(x))


#12 - How can you convert an integer to a string in Python? - ამისათვის ჩვენ აუცილებლად უნდა გამოვიყენოთ str()
x= 75
str_x = str(x)
print(str_x)
print(type(str_x))



#13 - What is the term for converting one data type into another in Python? - converting
a = 30
y = "zzz"
format_string = "{} {}".format(a, y)
print(format_string)


#14 - Which operator is used to check if two values are equal in Python? - აქ გამოიყენება ორი ტოლობა ანუ:==
print(10 == 10)


#15 - What is the result of the logical AND operation between True and False in Python? - იმისათვის რომ პასუხი ჩაითვალოს   საჭიროა რომ ორივე იყოს სწორი
print(100 == 100)#true
print(100 == 50)#false

#16 - What will the expression (5 > 3) and (10 < 20) evaluate to in Python? - ეს კოდი სწორია რადგან ორივე პირობა არის სწორი
print((5 > 3) and (10 < 20))

#17 - In Python, what is used to make decisions and execute different code blocks based on conditions? - გადაწყვეტილებების მისაღებათ გამოიყენება if-else
x = 10

if x > 0:
    print("true")
else:
    print("false")



#18 - Which type of loop is used to iterate over a sequence (e.g., a list or string) in Python? -ამისათვის გამოიყენება  for ციკლი
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)


#19 - What type of loop is used when you want to repeat a block of code as long as a condition is true? - while

count = 0

while count < 5:
    print("Count is:", count)
    count += 1


#20 -  What does the range() function in Python return?
for i in range(5):
    print(i)


#21 - Which keyword is used to start an "if" statement in Python? - ამისათვის ჩვენ ვიყენებთ if keyword
x = 10

if x > 5:
    print("x is greater than 5")


#22 - What is the purpose of the "else" statement in Python's "if-else" construct? - ამისთვის ჩვენ ვიყენებთ else 
x = 8

if x % 2 == 0:
    print("x is an even number")
else:
    print("x is an odd number")




#23 - Which data structure is used to store an ordered collection of items in Python?
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  
print(my_list[2])

#24 - In Python, which index represents the first element of a sequence?
my_list = [10, 20, 30, 40, 50]
first_element = my_list[0]
print(first_element)


#25 - How can you access the third element of a list in Python? - ამ შემთხვევაშ 3 ელემენტს აქვს 2 ინდექსი
my_list = [10, 20, 30, 40, 50]
third_element = my_list[2]
print(third_element)


#26 - What does slicing allow you to do with a sequence in Python? - slicing იმისთვის ვიყენებთ რომ მივწვდეთ კონკრეტულ ელემენტს
list = [0, 1, 2, 3, 4, ]
print(list[1:3])

#27 -  How can you extract a subsequence of a list from index 2 to index 5 (5 must be included) in Python?

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
subset = my_list[2:7]
print(my_list)
print(subset)

#28 - What does the "step" value in slicing indicate?
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
every_second_element = my_list[1:8:2]
print("Original List:", my_list)
print("Every Second Element:", every_second_element)


#29 -  What is a reusable block of code in Python that performs a specific task called? - ამას ეწოდება function
def greet(name):
    """This function prints a greeting message."""
    print("Hello, " + name + "!")


#30 - In Python, what are the values passed to a function called? - ამას arguments ეწოდება
def x7(n):#აქ n არის პარამეტრი
    print(n)
x7(n = 20)


#31 -  Which string method is used to convert a string to uppercase in Python? - ამ მეთოდს ეწოდება upper()
original_string = "hello, world!"
uppercase_string = original_string.upper()

print("Original String:", original_string)
print("Uppercase String:", uppercase_string)


#32 - What list method is used to add an element to the end of a list in Python? - ამ მეთოდს ეწოდება append()
my_list2 = [1, 2, 3, 4, 5]
print("Original List:", my_list2)
my_list2.append(6)
print(my_list2)


#33 -  In Python, which keyword is used to define a new function? - ამისათვის გამოიყენება def ფუნქცია რომ განვსაზღვროთ ახალი ფუნქცია
def greet(name):
    """This function prints a greeting message."""
    print("Hello, " + name + "!")


#34 - What keyword is used to return a value from a function in Python? - 
def add_numbers(a, b):
    """This function adds two numbers and returns the result."""
    sum_result = a + b
    return sum_result

result = add_numbers(3, 7)

print("Sum:", result)