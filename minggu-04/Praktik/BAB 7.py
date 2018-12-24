<<<<<<< HEAD
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
>>> 
>>> 
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
>>> 
>>> 
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
>>> 
>>> 
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
>>> 
>>> 
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
	print(f'{name:10} ==> {phone:10d}')

	
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
>>> 
>>> 
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
>>> 
>>> 
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
>>> 
>>> 
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
>>> 
>>> 
>>> print('This {food} is {adjective}.'.format(
	food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
>>> 
>>> 
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
						       other='Georg'))
The story of Bill, Manfred, and Georg.
>>> 
>>> 
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
	  'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
>>> 
>>> 
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
>>> 
>>> 
>>> for x in range(1, 11):
	
KeyboardInterrupt
>>> print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
ValueError: Unknown format code 'd' for object of type 'float'
>>> 
>>> 
>>> for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

	
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
>>> 
>>> 
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
>>> 
>>> 
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
>>> f = open('workfile', 'w')
>>> 
>>> with open('workfile') as f:
	read_data = f.read()

	
>>> f.closed
True
>>> 
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    f.read()
ValueError: I/O operation on closed file.
>>> 
>>> f.read()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    f.read()
ValueError: I/O operation on closed file.
>>> 
>>> f.readline()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    f.readline()
ValueError: I/O operation on closed file.
>>> f.readline()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    f.readline()
ValueError: I/O operation on closed file.
>>> for line in f:
	print(line, end='')

	
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    for line in f:
ValueError: I/O operation on closed file.
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)
13
>>> f.read(1)
b'd'
>>> import json
>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'
>>> 
=======
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
>>> 
>>> 
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
>>> 
>>> 
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
>>> 
>>> 
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
>>> 
>>> 
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
	print(f'{name:10} ==> {phone:10d}')

	
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
>>> 
>>> 
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
>>> 
>>> 
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
>>> 
>>> 
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
>>> 
>>> 
>>> print('This {food} is {adjective}.'.format(
	food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
>>> 
>>> 
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
						       other='Georg'))
The story of Bill, Manfred, and Georg.
>>> 
>>> 
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
	  'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
>>> 
>>> 
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
>>> 
>>> 
>>> for x in range(1, 11):
	
KeyboardInterrupt
>>> print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
ValueError: Unknown format code 'd' for object of type 'float'
>>> 
>>> 
>>> for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

	
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
>>> 
>>> 
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
>>> 
>>> 
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
>>> f = open('workfile', 'w')
>>> 
>>> with open('workfile') as f:
	read_data = f.read()

	
>>> f.closed
True
>>> 
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    f.read()
ValueError: I/O operation on closed file.
>>> 
>>> f.read()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    f.read()
ValueError: I/O operation on closed file.
>>> 
>>> f.readline()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    f.readline()
ValueError: I/O operation on closed file.
>>> f.readline()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    f.readline()
ValueError: I/O operation on closed file.
>>> for line in f:
	print(line, end='')

	
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    for line in f:
ValueError: I/O operation on closed file.
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)
13
>>> f.read(1)
b'd'
>>> import json
>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'
>>> 
>>>>>>> decdea822f6a158ba446ae39927ab39b83ff7588
