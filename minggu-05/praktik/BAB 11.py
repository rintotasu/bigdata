<<<<<<< HEAD
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
>>> 
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
							    'yellow'], 'blue']]]
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
>>> 
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
>>> 
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv()
>>> x = 1234567.8
>>> locale.format("%d", x, grouping=True)

Warning (from warnings module):
  File "__main__", line 1
DeprecationWarning: This method will be removed in a future version of Python. Use 'locale.format_string()' instead.
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
				    conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
>>> 
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
>>> 
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    t.substitute(d)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\string.py", line 132, in substitute
    return self.pattern.sub(convert, self.template)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\string.py", line 125, in convert
    return str(mapping[named])
KeyError: 'owner'
>>> 
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
	elimiter = '%'

	
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f
>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
	base, ext = os.path.splitext(filename)
	newname = t.substitute(d=date, n=i, f=ext)
	print('{0} --> {1}'.format(filename, newname))

	
img_1074.jpg --> Ashley_%n%f
img_1076.jpg --> Ashley_%n%f
img_1077.jpg --> Ashley_%n%f
>>> 
>>> import struct
>>> with open('myfile.zip', 'rb') as f:
	data = f.read()

	
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    with open('myfile.zip', 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.zip'
>>> 
>>> import struct
>>> with open('myfile.zip', 'rb') as f:
	data = f.read()
start = 0
SyntaxError: invalid syntax
>>> import struct
>>> with open('myfile.zip', 'rb') as f:
	data = f.read()
	start = 0

	
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    with open('myfile.zip', 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.zip'
>>> import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> import threading, zipfile
>>> class AsyncZip(threading.Thread):
	def __init__(self, infile, outfile):
		threading.Thread.__init__(self)
		self.infile = infile
		self.outfile = outfile
	def run(self):
		f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
		f.write(self.infile)
		f.close()
		print('Finished background zip of:', self.infile)

		
>>> background = AsyncZip('mydata.txt', 'myarchive.zip')
>>> background.start()
>>> Exception in thread Thread-1:
Traceback (most recent call last):
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\threading.py", line 917, in _bootstrap_inner
    self.run()
  File "<pyshell#72>", line 8, in run
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\zipfile.py", line 1688, in write
    zinfo = ZipInfo.from_file(filename, arcname)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\zipfile.py", line 483, in from_file
    st = os.stat(filename)
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'mydata.txt'

print('The main program continues to run in foreground.')
The main program continues to run in foreground.
>>> background.join()
>>> print('Main program waited until background was done.')
Main program waited until background was done.
>>> 
>>> import logging
>>> logging.debug('Debugging information')
>>> logging.info('Informational message')
>>> logging.warning('Warning:config file %s not found', 'server.conf')
WARNING:root:Warning:config file server.conf not found
>>> logging.error('Error occurred')
ERROR:root:Error occurred
>>> logging.critical('Critical error -- shutting down')
CRITICAL:root:Critical error -- shutting down
>>> 
>>> import weakref, gc
>>> class A:
	def __init__(self, value):
		self.value = value
		def __repr__(self):
			return str(self.value)

		
>>> a = A(10)
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a
>>> d['primary']
<__main__.A object at 0x000002BB1F5CD780>
>>> del a
>>> gc.collect()
0
>>> d['primary']
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    d['primary']
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\weakref.py", line 137, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
>>> 
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
>>> 
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
>>> 
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)
>>> heappush(data, -5)
>>> [heappop(data) for i in range(3)]
[-5, 0, 1]
>>> 
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
>>> 
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995
>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> sum([0.1]*10) == 1.0
False
>>> 
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
>>> 
>>> 
=======
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
>>> 
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
							    'yellow'], 'blue']]]
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
>>> 
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
>>> 
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv()
>>> x = 1234567.8
>>> locale.format("%d", x, grouping=True)

Warning (from warnings module):
  File "__main__", line 1
DeprecationWarning: This method will be removed in a future version of Python. Use 'locale.format_string()' instead.
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
				    conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
>>> 
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
>>> 
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    t.substitute(d)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\string.py", line 132, in substitute
    return self.pattern.sub(convert, self.template)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\string.py", line 125, in convert
    return str(mapping[named])
KeyError: 'owner'
>>> 
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
	elimiter = '%'

	
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f
>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
	base, ext = os.path.splitext(filename)
	newname = t.substitute(d=date, n=i, f=ext)
	print('{0} --> {1}'.format(filename, newname))

	
img_1074.jpg --> Ashley_%n%f
img_1076.jpg --> Ashley_%n%f
img_1077.jpg --> Ashley_%n%f
>>> 
>>> import struct
>>> with open('myfile.zip', 'rb') as f:
	data = f.read()

	
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    with open('myfile.zip', 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.zip'
>>> 
>>> import struct
>>> with open('myfile.zip', 'rb') as f:
	data = f.read()
start = 0
SyntaxError: invalid syntax
>>> import struct
>>> with open('myfile.zip', 'rb') as f:
	data = f.read()
	start = 0

	
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    with open('myfile.zip', 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.zip'
>>> import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> import threading, zipfile
>>> class AsyncZip(threading.Thread):
	def __init__(self, infile, outfile):
		threading.Thread.__init__(self)
		self.infile = infile
		self.outfile = outfile
	def run(self):
		f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
		f.write(self.infile)
		f.close()
		print('Finished background zip of:', self.infile)

		
>>> background = AsyncZip('mydata.txt', 'myarchive.zip')
>>> background.start()
>>> Exception in thread Thread-1:
Traceback (most recent call last):
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\threading.py", line 917, in _bootstrap_inner
    self.run()
  File "<pyshell#72>", line 8, in run
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\zipfile.py", line 1688, in write
    zinfo = ZipInfo.from_file(filename, arcname)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\zipfile.py", line 483, in from_file
    st = os.stat(filename)
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'mydata.txt'

print('The main program continues to run in foreground.')
The main program continues to run in foreground.
>>> background.join()
>>> print('Main program waited until background was done.')
Main program waited until background was done.
>>> 
>>> import logging
>>> logging.debug('Debugging information')
>>> logging.info('Informational message')
>>> logging.warning('Warning:config file %s not found', 'server.conf')
WARNING:root:Warning:config file server.conf not found
>>> logging.error('Error occurred')
ERROR:root:Error occurred
>>> logging.critical('Critical error -- shutting down')
CRITICAL:root:Critical error -- shutting down
>>> 
>>> import weakref, gc
>>> class A:
	def __init__(self, value):
		self.value = value
		def __repr__(self):
			return str(self.value)

		
>>> a = A(10)
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a
>>> d['primary']
<__main__.A object at 0x000002BB1F5CD780>
>>> del a
>>> gc.collect()
0
>>> d['primary']
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    d['primary']
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\weakref.py", line 137, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
>>> 
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
>>> 
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
>>> 
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)
>>> heappush(data, -5)
>>> [heappop(data) for i in range(3)]
[-5, 0, 1]
>>> 
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
>>> 
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995
>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> sum([0.1]*10) == 1.0
False
>>> 
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
>>> 
>>> 
>>>>>>> decdea822f6a158ba446ae39927ab39b83ff7588
