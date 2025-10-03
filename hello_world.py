print("hello, world!")
# This is a comment in the code you would use to explain what the code does.
# The code above prints "hello, world!" to the console.
print("This line will be executed.")
# The line below is commented out and will not be executed.
# print("This line will not be executed."
age = 30
name = "Guido van Rossum"
print(age)
print(name)
print("I am " + str(age) + " years old.")
print("My name is " + name + ".")
greeting = "Hello, Python!"
fact = 'Python is fun.'
print(greeting)
print(fact)
# The code below demonstrates the use of single and double quotes in strings.
quote = 'He said, "Python is awesome!"'
print(quote)
# The code below demonstrates the use of escape characters in strings.
escaped_quote = "He said, \"Python is awesome!\""
name = "Bob"
age = 37
print(name + " is " + str(age) + " years old.")
# The code above concatenates strings and variables to form a complete sentence.
print(f"{name} is {age} years old.")
# The code above uses an f-string to format the output. an f-string is a string literal that is prefixed with 'f' or 'F' and contains expressions inside curly braces {} that are evaluated at runtime.
fruits = ["apple", "banana", "cherry"]
# The code above creates a list of fruits. an array is a data structure that can hold multiple values.
mixed_list = [1, "two", 3.0, True]
# The code above creates a list of mixed data types. strings, integers, floats, and booleans can all be stored in a list or array. this is a feature of dynamic typing in Python.
print(fruits)
print(mixed_list)
coordinates = (10.0, 20.0)
# The code above creates a tuple of coordinates. a tuple is similar to a list, but it is immutable, meaning its values cannot be changed after creation.
rgb_color = (255, 0, 128)
# The code above creates a tuple representing an RGB color. tuples are often used to represent fixed collections of related values.
print(coordinates)
print(rgb_color)
# The code above prints the tuples to the console.
print(f"Coordinates: {coordinates}")
print(f"RGB Color: {rgb_color}")
# The code above uses f-strings to format the output of the tuples.
person = {
    "name": "Frank Castle",
    "age": 40,
    "is_hero": False,
    "skills": ["marksmanship", "hand-to-hand combat", "tactics"],
    "enemies": ("Kingpin", "Jigsaw", "Bullseye"),
    "address": {
        "street": "123 Justice St",
        "city": "New York",
        "zip": "10001"},
    "allies": ("Jessica Jones", "Luke Cage", "Daredevil")
}
# The code above creates a dictionary representing a person. a dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value.
print(person)
# The code above prints the dictionary to the console.
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"Is Hero: {person['is_hero']}")
print(f"Skills: {', '.join(person['skills'])}")
print(f"Enemies: {', '.join(person['enemies'])}")
print(f"Address: {person['address']['street']}, {person['address']['city']}, {person['address']['zip']}")
print(f"Allies: {', '.join(person['allies'])}")
# The code above uses f-strings to format the output of the dictionary.
# It accesses specific values using their keys and formats lists and tuples for better readability.
hero_name = "Spider-Man"
hero_age = 30
hero_power = (  "wall-crawling", 
              "enhanced strength", "spider-sense")
hero_friends = ["Mary Jane", "Aunt May", "Harry Osborn"]
hero_villains = ("Green Goblin", "Doctor Octopus", "Venom")
hero_info = {
    "name": hero_name,
    "age": hero_age,
    "power": hero_power,
    "friends": hero_friends,
    "villains": hero_villains
}
# The code above creates a dictionary representing a superhero. it includes various attributes such as name, age, powers, friends, and villains.
print(hero_info)
# The code above prints the superhero dictionary to the console.
print(f"Hero Name: {hero_info['name']}")
print(f"Hero Age: {hero_info['age']}")
print(f"Hero Powers: {', '.join(hero_info['power'])}")
print(f"Hero Friends: {', '.join(hero_info['friends'])}")
print(f"Hero Villains: {', '.join(hero_info['villains'])}")
# The code above uses f-strings to format the output of the superhero dictionary.
# It accesses specific values using their keys and formats lists and tuples for better readability.
# if, elif, and else statements are used for conditional branching in Python.
number = 10
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print(f"{number} is zero.")
# The code above checks if a number is positive, negative, or zero and prints the appropriate message.
# The code below demonstrates the use of logical operators (and, or, not) in conditional statements.
age = 25
has_id = True
if age >= 18 and has_id:
    print("You are allowed to enter the club.")
else:
    print("You are not allowed to enter the club.")
# The code above checks if a person is old enough and has an ID to enter a club.
# The code below demonstrates the use of nested if statements.
score = 85
if score >= 60:
    if score >= 90:
        print("You received an A.")
    elif score >= 80:
        print("You received a B.")
    elif score >= 70:
        print("You received a C.")
    else:
        print("You received a D.")
else:
    print("You received an F.")
# The code above checks a score and prints the corresponding letter grade.
# The code below demonstrates the use of a while loop to print numbers from 1 to 5.
count = 1
while count <= 5:
    print(count)
    count += 1
# The code above initializes a counter variable and uses a while loop to print numbers from 1 to 5.
# The code below demonstrates the use of a while loop to calculate the factorial of a number.
number = 5
factorial = 1
while number > 1:
    factorial *= number
    number -= 1
print(f"Factorial: {factorial}")
# The code above calculates the factorial of a number using a while loop and prints the result.
# The code below demonstrates the use of a for loop to iterate over a list of fruits.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# The code above iterates over a list of fruits and prints each fruit to the console.
# The code below demonstrates the use of a for loop to iterate over a range of numbers.
for i in range(1, 6):
    print(i)
# The code above uses a for loop to print numbers from 1 to 5 using the range function.
# The code below demonstrates the use of a for loop to iterate over a dictionary.
person = {
    "name": "Alice",
    "age": 28,
    "city": "Wonderland"
}
for key, value in person.items():
    print(f"{key}: {value}")
# The code above iterates over a dictionary and prints each key-value pair using an f-string.
# The code below demonstrates the use of a for loop with the enumerate function to get both index and value.
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Color {index + 1}: {color}")
# The code above uses the enumerate function to get both the index and value of each color in   the list and prints them using an f-string.