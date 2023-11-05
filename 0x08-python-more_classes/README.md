# Object Oriented Programming

# Authoe: Kevin Kipkoech


In object OOP data and functionality are wrapped inside an object. Its a better way of organizing the program unlike having it in block of statements to manipulate the data.
Classes and objects are the two main aspects of OOP. A class creates new type and objects are instances of the class.


## How it works
A new class is created using the 'class' statement and the name of the class. This is followed by intended block which is the body of the class. You can then create an object/instance if this class using the name of the class.

The __init__ method
This method name has a special significance in python classes. The method is run as soon as the object of class is instantiated(created), it is useful to do any initialization you want to do with an object.


### For this Project
The learning objectives of this project was to understand the following;
•	Why Python programming is awesome
•	What is OOP
•	“first-class everything”
•	What is a class
•	What is an object and an instance
•	What is the difference between a class and an object or instance
•	What is an attribute
•	What are and how to use public, protected and private attributes
•	What is self
•	What is a method
•	What is the special __init__ method and how to use it
•	What is Data Abstraction, Data Encapsulation, and Information Hiding
•	What is a property
•	What is the difference between an attribute and a property in Python
•	What is the Pythonic way to write getters and setters in Python
•	What are the special __str__ and __repr__ methods and how to use them
•	What is the difference between __str__ and __repr__
•	What is a class attribute
•	What is the difference between a object attribute and a class attribute
•	What is a class method
•	What is a static method
•	How to dynamically create arbitrary new attributes for existing instances of a class
•	How to bind attributes to object and classes
•	What is and what does contain __dict__ of a class and of an instance of a class
•	How does Python find the attributes of an object or class
•	How to use the getattr function

####Requirements
General
•	Allowed editors: vi, vim, emacs
•	All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
•	All your files should end with a new line
•	The first line of all your files should be exactly #!/usr/bin/python3
•	A README.md file, at the root of the folder of the project, is mandatory
•	Your code should use the pycodestyle (version 2.8.*)
•	All your files must be executable
•	The length of your files will be tested using wc

######Tasks
0. Simple rectangle
	Write an empty class Rectangle that defines a rectangle:
•	You are not allowed to import any module

1. Real definition of a rectangle
	Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	You are not allowed to import any module
2. Area and Perimeter
	Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter is equal to 0
•	You are not allowed to import any module
3. String representation
	Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter has to be equal to 0
•	print() and str() should print the rectangle with the character #: (see example below)
o	if width or height is equal to 0, return an empty string
•	You are not allowed to import any module
4. Eval is magic
	Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter has to be equal to 0
•	print() and str() should print the rectangle with the character #: (see example below)
o	if width or height is equal to 0, return an empty string
•	repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)
•	You are not allowed to import any module
5. Detect instance deletion
	Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter has to be equal to 0
•	print() and str() should print the rectangle with the character #:
o	if width or height is equal to 0, return an empty string
•	repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
•	Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
•	You are not allowed to import any module
6. How many instances
	Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Public class attribute number_of_instances:
o	Initialized to 0
o	Incremented during each new instance instantiation
o	Decremented during each instance deletion
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter has to be equal to 0
•	print() and str() should print the rectangle with the character #:
o	if width or height is equal to 0, return an empty string
•	repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
•	Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
•	You are not allowed to import any module
7. Change representation
	Write a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Public class attribute number_of_instances:
o	Initialized to 0
o	Incremented during each new instance instantiation
o	Decremented during each instance deletion
•	Public class attribute print_symbol:
o	Initialized to #
o	Used as symbol for string representation
o	Can be any type
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter has to be equal to 0
•	print() and str() should print the rectangle with the character(s) stored in print_symbol:
o	if width or height is equal to 0, return an empty string
•	repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
•	Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
•	You are not allowed to import any module
8. Compare rectangles
	Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Public class attribute number_of_instances:
o	Initialized to 0
o	Incremented during each new instance instantiation
o	Decremented during each instance deletion
•	Public class attribute print_symbol:
o	Initialized to #
o	Used as symbol for string representation
o	Can be any type
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter has to be equal to 0
•	print() and str() should print the rectangle with the character #:
o	if width or height is equal to 0, return an empty string
•	repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
•	Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
•	Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
o	rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
o	rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
o	Returns rect_1 if both have the same area value
•	You are not allowed to import any module
9. A square is a rectangle
	Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)
•	Private instance attribute: width:
o	property def width(self): to retrieve it
o	property setter def width(self, value): to set it:
	width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
	if width is less than 0, raise a ValueError exception with the message width must be >= 0
•	Private instance attribute: height:
o	property def height(self): to retrieve it
o	property setter def height(self, value): to set it:
	height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
	if height is less than 0, raise a ValueError exception with the message height must be >= 0
•	Public class attribute number_of_instances:
o	Initialized to 0
o	Incremented during each new instance instantiation
o	Decremented during each instance deletion
•	Public class attribute print_symbol:
o	Initialized to #
o	Used as symbol for string representation
o	Can be any type
•	Instantiation with optional width and height: def __init__(self, width=0, height=0):
•	Public instance method: def area(self): that returns the rectangle area
•	Public instance method: def perimeter(self): that returns the rectangle perimeter:
o	if width or height is equal to 0, perimeter has to be equal to 0
•	print() and str() should print the rectangle with the character #:
o	if width or height is equal to 0, return an empty string
•	repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
•	Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
•	Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
o	rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
o	rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
o	Returns rect_1 if both have the same area value
•	Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size
•	You are not allowed to import any module


