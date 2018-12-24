<<<<<<< HEAD
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> while True print('Hello world')
SyntaxError: invalid syntax
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    10 * (1/0)
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    4 + spam*3
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    '2' + 2
TypeError: can only concatenate str (not "int") to str
>>> while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except ValueError:
		print("Oops!  That was no valid number.  Try again...")

		
Please enter a number: 22
>>> 
>>> class B(Exception):
	pass
class C(B):
	
SyntaxError: invalid syntax
>>> 
>>> import sys
>>> try:
	f = open('myfile.txt')
	s = f.readline()
	i = int(s.strip())
except OSError as err:
	print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

OS error: [Errno 2] No such file or directory: 'myfile.txt'
>>> 
>>> for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

        
>>> 
>>> try:
	raise Exception('spam', 'eggs')
 except Exception as inst:
	 
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> 
>>> try:
	raise Exception('spam', 'eggs')
except Exception as inst:
	print(type(inst))
	print(inst.args)
	print(inst)

	
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
>>> x, y = inst.args
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    x, y = inst.args
NameError: name 'inst' is not defined
>>> 
>>> def this_fails():
	x = 1/0

	
>>> try:
	this_fails()
	except ZeroDivisionError as err:
		
SyntaxError: invalid syntax
>>> 
>>> try:
	this_fails()
except ZeroDivisionError as err:
	print('Handling run-time error:', err)

	
Handling run-time error: division by zero
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    raise NameError('HiThere')
NameError: HiThere
>>> 
>>> try:
	raise NameError('HiThere')
except NameError:
	print('An exception flew by!')
	raise

An exception flew by!
Traceback (most recent call last):
  File "<pyshell#65>", line 2, in <module>
    raise NameError('HiThere')
NameError: HiThere
>>> 
>>> class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
        
SyntaxError: invalid syntax
>>> 
>>> try:
	raise KeyboardInterrupt
finally:
	print('Goodbye, world!')

	
Goodbye, world!
Traceback (most recent call last):
  File "<pyshell#73>", line 2, in <module>
    raise KeyboardInterrupt
KeyboardInterrupt
>>> 
>>> def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print("division by zero!")
	else:
		 print("result is", result)
	finally:
		print("executing finally clause")

		
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    divide("2", "1")
  File "<pyshell#84>", line 3, in divide
    result = x / y
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> 
>>> for line in open("myfile.txt"):
    print(line, end="")

    
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    for line in open("myfile.txt"):
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
>>> 
>>> for line in open("myfile.txt"):
	print(line, end="")

	
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    for line in open("myfile.txt"):
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
>>> 
>>> with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

        
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    with open("myfile.txt") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
>>> 
>>> with open("myfile.txt") as f:
	for line in f:
		
KeyboardInterrupt
>>> 
>>> 
>>> with open("myfile.txt") as f:
	for line in f:
		print(line, end="")

		
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    with open("myfile.txt") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
>>> 
=======
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> while True print('Hello world')
SyntaxError: invalid syntax
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    10 * (1/0)
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    4 + spam*3
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    '2' + 2
TypeError: can only concatenate str (not "int") to str
>>> while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except ValueError:
		print("Oops!  That was no valid number.  Try again...")

		
Please enter a number: 22
>>> 
>>> class B(Exception):
	pass
class C(B):
	
SyntaxError: invalid syntax
>>> 
>>> import sys
>>> try:
	f = open('myfile.txt')
	s = f.readline()
	i = int(s.strip())
except OSError as err:
	print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

OS error: [Errno 2] No such file or directory: 'myfile.txt'
>>> 
>>> for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

        
>>> 
>>> try:
	raise Exception('spam', 'eggs')
 except Exception as inst:
	 
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> 
>>> try:
	raise Exception('spam', 'eggs')
except Exception as inst:
	print(type(inst))
	print(inst.args)
	print(inst)

	
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
>>> x, y = inst.args
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    x, y = inst.args
NameError: name 'inst' is not defined
>>> 
>>> def this_fails():
	x = 1/0

	
>>> try:
	this_fails()
	except ZeroDivisionError as err:
		
SyntaxError: invalid syntax
>>> 
>>> try:
	this_fails()
except ZeroDivisionError as err:
	print('Handling run-time error:', err)

	
Handling run-time error: division by zero
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    raise NameError('HiThere')
NameError: HiThere
>>> 
>>> try:
	raise NameError('HiThere')
except NameError:
	print('An exception flew by!')
	raise

An exception flew by!
Traceback (most recent call last):
  File "<pyshell#65>", line 2, in <module>
    raise NameError('HiThere')
NameError: HiThere
>>> 
>>> class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
        
SyntaxError: invalid syntax
>>> 
>>> try:
	raise KeyboardInterrupt
finally:
	print('Goodbye, world!')

	
Goodbye, world!
Traceback (most recent call last):
  File "<pyshell#73>", line 2, in <module>
    raise KeyboardInterrupt
KeyboardInterrupt
>>> 
>>> def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print("division by zero!")
	else:
		 print("result is", result)
	finally:
		print("executing finally clause")

		
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    divide("2", "1")
  File "<pyshell#84>", line 3, in divide
    result = x / y
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> 
>>> for line in open("myfile.txt"):
    print(line, end="")

    
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    for line in open("myfile.txt"):
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
>>> 
>>> for line in open("myfile.txt"):
	print(line, end="")

	
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    for line in open("myfile.txt"):
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
>>> 
>>> with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

        
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    with open("myfile.txt") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
>>> 
>>> with open("myfile.txt") as f:
	for line in f:
		
KeyboardInterrupt
>>> 
>>> 
>>> with open("myfile.txt") as f:
	for line in f:
		print(line, end="")

		
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    with open("myfile.txt") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
>>> 
>>>>>>> decdea822f6a158ba446ae39927ab39b83ff7588
