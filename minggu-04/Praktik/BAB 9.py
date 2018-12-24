<<<<<<< HEAD
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
SyntaxError: invalid syntax
>>> 
>>> class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

>>> 
>>> class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart

		
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
>>> def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
SyntaxError: invalid syntax
>>> 
>>> x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> class Dog:
	kind = 'canine'
	def __init__(self, name):
		self.name = name

		
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind
'canine'
>>> e.kind
'canine'
>>> d.name
'Fido'
>>> e.name
'Buddy'
>>> 
>>> class Dog:
	tricks = []
	def __init__(self, name):
		self.name = name
	def add_trick(self, trick):
		self.tricks.append(trick)

		
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over', 'play dead']
>>> 
>>> class Dog:
	def __init__(self, name):
		self.name = name
		self.tricks = []
	def add_trick(self, trick):
		self.tricks.append(trick)

		
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
>>> 
>>> 
>>> def f1(self, x, y):
	return min(x, x+y)
class C:
	
SyntaxError: invalid syntax
>>> 
>>> def f1(self, x, y):
	return min(x, x+y)
Class C:
	
SyntaxError: invalid syntax
>>> 
>>> def f1(self, x, y):
	return min(x, x+y)

>>> class C:
	f = f1
	def g(self):
		return 'hello world'
	h = g

	
>>> 
>>> class Bag:
	def __init__(self):
		self.data = []
	def add(self, x):
		self.data.append(x)
	def addtwice(self, x):
		self.add(x)
		self.add(x)

		
>>> 
>>> class Mapping:
	def __init__(self, iterable):
		self.items_list = []
		self.__update(iterable)
	def update(self, iterable):
		for item in iterable:
			self.items_list.append(item)
	__update = update

	
>>> class MappingSubclass(Mapping):
	def update(self, keys, values):
		for item in zip(keys, values):
			self.items_list.append(item)

			
>>> 
>>> class Employee:
	pass

>>> john = Employee()
>>> ohn.name = 'John Doe'
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    ohn.name = 'John Doe'
NameError: name 'ohn' is not defined
>>> 
>>> class Employee:
	pass
john = Employee()
SyntaxError: invalid syntax
>>> 
>>> for element in [1, 2, 3]:
	print(element)

	
1
2
3
>>> for element in (1, 2, 3):
	print(element)

	
1
2
3
>>> for key in {'one':1, 'two':2}:
	print(key)

	
one
two
>>> for char in "123":
	print(char)

	
1
2
3
>>> for line in open("myfile.txt"):
	print(line, end='')

	
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    for line in open("myfile.txt"):
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
>>> 
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x000001826D247390>
>>> 
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    next(it)
StopIteration
>>> 
>>> class Reverse:
	def __init__(self, data):
		self.data = data
		self.index = len(data)
	def __iter__(self):
		return self
	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]

	
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x000001826D3E4860>
>>> for char in rev:
	print(char)

	
m
a
p
s
>>> 
>>> def reverse(data):
	for index in range(len(data)-1, -1, -1):
		yield data[index]

		
>>> for char in reverse('golf'):
	print(char)

	
f
l
o
g
>>> 
>>> sum(i*i for i in range(10))
285
>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))
260
>>> from math import pi, sin
>>> sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
>>> unique_words = set(word  for line in page  for word in line.split())
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    unique_words = set(word  for line in page  for word in line.split())
NameError: name 'page' is not defined
>>> valedictorian = max((student.gpa, student.name) for student in graduates)
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    valedictorian = max((student.gpa, student.name) for student in graduates)
NameError: name 'graduates' is not defined
>>> 
>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
>>> 
=======
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
SyntaxError: invalid syntax
>>> 
>>> class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

>>> 
>>> class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart

		
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
>>> def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
SyntaxError: invalid syntax
>>> 
>>> x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> class Dog:
	kind = 'canine'
	def __init__(self, name):
		self.name = name

		
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind
'canine'
>>> e.kind
'canine'
>>> d.name
'Fido'
>>> e.name
'Buddy'
>>> 
>>> class Dog:
	tricks = []
	def __init__(self, name):
		self.name = name
	def add_trick(self, trick):
		self.tricks.append(trick)

		
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over', 'play dead']
>>> 
>>> class Dog:
	def __init__(self, name):
		self.name = name
		self.tricks = []
	def add_trick(self, trick):
		self.tricks.append(trick)

		
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
>>> 
>>> 
>>> def f1(self, x, y):
	return min(x, x+y)
class C:
	
SyntaxError: invalid syntax
>>> 
>>> def f1(self, x, y):
	return min(x, x+y)
Class C:
	
SyntaxError: invalid syntax
>>> 
>>> def f1(self, x, y):
	return min(x, x+y)

>>> class C:
	f = f1
	def g(self):
		return 'hello world'
	h = g

	
>>> 
>>> class Bag:
	def __init__(self):
		self.data = []
	def add(self, x):
		self.data.append(x)
	def addtwice(self, x):
		self.add(x)
		self.add(x)

		
>>> 
>>> class Mapping:
	def __init__(self, iterable):
		self.items_list = []
		self.__update(iterable)
	def update(self, iterable):
		for item in iterable:
			self.items_list.append(item)
	__update = update

	
>>> class MappingSubclass(Mapping):
	def update(self, keys, values):
		for item in zip(keys, values):
			self.items_list.append(item)

			
>>> 
>>> class Employee:
	pass

>>> john = Employee()
>>> ohn.name = 'John Doe'
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    ohn.name = 'John Doe'
NameError: name 'ohn' is not defined
>>> 
>>> class Employee:
	pass
john = Employee()
SyntaxError: invalid syntax
>>> 
>>> for element in [1, 2, 3]:
	print(element)

	
1
2
3
>>> for element in (1, 2, 3):
	print(element)

	
1
2
3
>>> for key in {'one':1, 'two':2}:
	print(key)

	
one
two
>>> for char in "123":
	print(char)

	
1
2
3
>>> for line in open("myfile.txt"):
	print(line, end='')

	
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    for line in open("myfile.txt"):
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
>>> 
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x000001826D247390>
>>> 
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    next(it)
StopIteration
>>> 
>>> class Reverse:
	def __init__(self, data):
		self.data = data
		self.index = len(data)
	def __iter__(self):
		return self
	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]

	
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x000001826D3E4860>
>>> for char in rev:
	print(char)

	
m
a
p
s
>>> 
>>> def reverse(data):
	for index in range(len(data)-1, -1, -1):
		yield data[index]

		
>>> for char in reverse('golf'):
	print(char)

	
f
l
o
g
>>> 
>>> sum(i*i for i in range(10))
285
>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))
260
>>> from math import pi, sin
>>> sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
>>> unique_words = set(word  for line in page  for word in line.split())
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    unique_words = set(word  for line in page  for word in line.split())
NameError: name 'page' is not defined
>>> valedictorian = max((student.gpa, student.name) for student in graduates)
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    valedictorian = max((student.gpa, student.name) for student in graduates)
NameError: name 'graduates' is not defined
>>> 
>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
>>> 
>>>>>>> decdea822f6a158ba446ae39927ab39b83ff7588
