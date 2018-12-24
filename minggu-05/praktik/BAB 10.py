<<<<<<< HEAD
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Users\\Doto Baliga\\AppData\\Local\\Programs\\Python\\Python37'
>>> os.chdir('/server/accesslogs')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    os.chdir('/server/accesslogs')
FileNotFoundError: [WinError 3] The system cannot find the path specified: '/server/accesslogs'
>>> os.system('mkdir today')
0
>>> 
>>> 
>>> import shuil
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    import shuil
ModuleNotFoundError: No module named 'shuil'
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    shutil.copyfile('data.db', 'archive.db')
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 120, in copyfile
    with open(src, 'rb') as fsrc:
FileNotFoundError: [Errno 2] No such file or directory: 'data.db'
>>> shutil.move('/build/executables', 'installdir')
Traceback (most recent call last):
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 557, in move
    os.rename(src, real_dst)
FileNotFoundError: [WinError 3] The system cannot find the path specified: '/build/executables' -> 'installdir'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    shutil.move('/build/executables', 'installdir')
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 571, in move
    copy_function(src, real_dst)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 257, in copy2
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 120, in copyfile
    with open(src, 'rb') as fsrc:
FileNotFoundError: [Errno 2] No such file or directory: '/build/executables'
>>> 
>>> 
>>> import glob
>>> glob.glob('*.py')
[]
>>> import sys
>>> print(sys.argv)
['']
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
47
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
>>> 'tea for too'.replace('too', 'two')
'tea for two'
>>> 
>>> 
>>> import math
>>> math.cos(math.pi / 4)
0.7071067811865476
>>> math.log(1024, 2)
10.0
>>> 
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)
[91, 79, 71, 3, 58, 61, 57, 4, 22, 62]
>>> random.random()
0.4182915509058548
>>> random.randrange(6)
4
>>> 
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
>>> 
>>> from urllib.request import urlopen
>>> with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
	for line in response:
		line = line.decode('utf-8')
		if 'EST' in line or 'EDT' in line:
			print(line)

			
Traceback (most recent call last):
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 1317, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1229, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1275, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1224, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1016, in _send_output
    self.send(msg)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 956, in send
    self.connect()
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1392, in connect
    server_hostname=server_hostname)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\ssl.py", line 412, in wrap_socket
    session=session
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\ssl.py", line 850, in _create
    self.do_handshake()
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\ssl.py", line 1108, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1045)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 531, in open
    response = meth(req, response)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 641, in http_response
    'http', request, response, code, msg, hdrs)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 563, in error
    result = self._call_chain(*args)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 503, in _call_chain
    result = func(*args)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 755, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 525, in open
    response = self._open(req, data)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 543, in _open
    '_open', req)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 503, in _call_chain
    result = func(*args)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 1360, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 1319, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1045)>

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    server = smtplib.SMTP('localhost')
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 251, in __init__
    (code, msg) = self.connect(host, port)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 336, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 307, in _get_socket
    self.source_address)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\socket.py", line 727, in create_connection
    raise err
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\socket.py", line 716, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it
>>> server = smtplib.SMTP('localhost')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    server = smtplib.SMTP('localhost')
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 251, in __init__
    (code, msg) = self.connect(host, port)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 336, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 307, in _get_socket
    self.source_address)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\socket.py", line 727, in create_connection
    raise err
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\socket.py", line 716, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
		    To: jcaesar@example.org
		    
SyntaxError: invalid syntax
>>> server.quit()
		    
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    server.quit()
NameError: name 'server' is not defined
>>> 
		    
>>> 
		    
>>> from datetime import date
		    
>>> now = date.today()
		    
>>> now
		    
datetime.date(2018, 10, 3)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
		    
'10-03-18. 03 Oct 2018 is a Wednesday on the 03 day of October.'
>>> birthday = date(1964, 7, 31)
		    
>>> age = now - birthday
		    
>>> age.days
		    
19787
>>> 
		    
>>> import zlib
		    
>>> s = b'witch which has which witches wrist watch'
		    
>>> len(s)
		    
41
>>> t = zlib.compress(s)
		    
>>> len(t)
		    
37
>>> zlib.decompress(t)
		    
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
		    
226805979
>>> 
		    
>>> from timeit import Timer
		    
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
		    
0.13430722700002207
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
		    
0.09413290300017252
>>> 
		    
>>> def average(values):
		    """Computes the arithmetic mean of a list of numbers.
	print(average([20, 30, 70]))
	40.0
	"""
		    return sum(values) / len(values)

		    
>>> import doctest
		    
>>> doctest.testmod()
		    
TestResults(failed=0, attempted=0)
>>> 
		    
>>> import unittest
		    
>>> class TestStatisticalFunctions(unittest.TestCase):
		    def test_average(self):
		    self.assertEqual(average([20, 30, 70]), 40.0)
		    
SyntaxError: expected an indented block
>>> 
		    
>>> import unittest
		    
>>> class TestStatisticalFunctions(unittest.TestCase):
	  self.assertEqual(average([20, 30, 70]), 40.0)
	  self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
	  with self.assertRaises(ZeroDivisionError):
		    average([])
	  with self.assertRaises(TypeError):
		    average(20, 30, 70)

		    
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    class TestStatisticalFunctions(unittest.TestCase):
  File "<pyshell#110>", line 2, in TestStatisticalFunctions
    self.assertEqual(average([20, 30, 70]), 40.0)
NameError: name 'self' is not defined
>>> unittest.main()
		    

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
>>> 
=======
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Users\\Doto Baliga\\AppData\\Local\\Programs\\Python\\Python37'
>>> os.chdir('/server/accesslogs')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    os.chdir('/server/accesslogs')
FileNotFoundError: [WinError 3] The system cannot find the path specified: '/server/accesslogs'
>>> os.system('mkdir today')
0
>>> 
>>> 
>>> import shuil
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    import shuil
ModuleNotFoundError: No module named 'shuil'
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    shutil.copyfile('data.db', 'archive.db')
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 120, in copyfile
    with open(src, 'rb') as fsrc:
FileNotFoundError: [Errno 2] No such file or directory: 'data.db'
>>> shutil.move('/build/executables', 'installdir')
Traceback (most recent call last):
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 557, in move
    os.rename(src, real_dst)
FileNotFoundError: [WinError 3] The system cannot find the path specified: '/build/executables' -> 'installdir'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    shutil.move('/build/executables', 'installdir')
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 571, in move
    copy_function(src, real_dst)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 257, in copy2
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\shutil.py", line 120, in copyfile
    with open(src, 'rb') as fsrc:
FileNotFoundError: [Errno 2] No such file or directory: '/build/executables'
>>> 
>>> 
>>> import glob
>>> glob.glob('*.py')
[]
>>> import sys
>>> print(sys.argv)
['']
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
47
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
>>> 'tea for too'.replace('too', 'two')
'tea for two'
>>> 
>>> 
>>> import math
>>> math.cos(math.pi / 4)
0.7071067811865476
>>> math.log(1024, 2)
10.0
>>> 
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)
[91, 79, 71, 3, 58, 61, 57, 4, 22, 62]
>>> random.random()
0.4182915509058548
>>> random.randrange(6)
4
>>> 
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
>>> 
>>> from urllib.request import urlopen
>>> with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
	for line in response:
		line = line.decode('utf-8')
		if 'EST' in line or 'EDT' in line:
			print(line)

			
Traceback (most recent call last):
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 1317, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1229, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1275, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1224, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1016, in _send_output
    self.send(msg)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 956, in send
    self.connect()
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1392, in connect
    server_hostname=server_hostname)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\ssl.py", line 412, in wrap_socket
    session=session
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\ssl.py", line 850, in _create
    self.do_handshake()
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\ssl.py", line 1108, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1045)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 531, in open
    response = meth(req, response)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 641, in http_response
    'http', request, response, code, msg, hdrs)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 563, in error
    result = self._call_chain(*args)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 503, in _call_chain
    result = func(*args)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 755, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 525, in open
    response = self._open(req, data)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 543, in _open
    '_open', req)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 503, in _call_chain
    result = func(*args)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 1360, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 1319, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1045)>

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    server = smtplib.SMTP('localhost')
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 251, in __init__
    (code, msg) = self.connect(host, port)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 336, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 307, in _get_socket
    self.source_address)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\socket.py", line 727, in create_connection
    raise err
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\socket.py", line 716, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it
>>> server = smtplib.SMTP('localhost')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    server = smtplib.SMTP('localhost')
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 251, in __init__
    (code, msg) = self.connect(host, port)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 336, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 307, in _get_socket
    self.source_address)
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\socket.py", line 727, in create_connection
    raise err
  File "C:\Users\Doto Baliga\AppData\Local\Programs\Python\Python37\lib\socket.py", line 716, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
		    To: jcaesar@example.org
		    
SyntaxError: invalid syntax
>>> server.quit()
		    
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    server.quit()
NameError: name 'server' is not defined
>>> 
		    
>>> 
		    
>>> from datetime import date
		    
>>> now = date.today()
		    
>>> now
		    
datetime.date(2018, 10, 3)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
		    
'10-03-18. 03 Oct 2018 is a Wednesday on the 03 day of October.'
>>> birthday = date(1964, 7, 31)
		    
>>> age = now - birthday
		    
>>> age.days
		    
19787
>>> 
		    
>>> import zlib
		    
>>> s = b'witch which has which witches wrist watch'
		    
>>> len(s)
		    
41
>>> t = zlib.compress(s)
		    
>>> len(t)
		    
37
>>> zlib.decompress(t)
		    
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
		    
226805979
>>> 
		    
>>> from timeit import Timer
		    
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
		    
0.13430722700002207
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
		    
0.09413290300017252
>>> 
		    
>>> def average(values):
		    """Computes the arithmetic mean of a list of numbers.
	print(average([20, 30, 70]))
	40.0
	"""
		    return sum(values) / len(values)

		    
>>> import doctest
		    
>>> doctest.testmod()
		    
TestResults(failed=0, attempted=0)
>>> 
		    
>>> import unittest
		    
>>> class TestStatisticalFunctions(unittest.TestCase):
		    def test_average(self):
		    self.assertEqual(average([20, 30, 70]), 40.0)
		    
SyntaxError: expected an indented block
>>> 
		    
>>> import unittest
		    
>>> class TestStatisticalFunctions(unittest.TestCase):
	  self.assertEqual(average([20, 30, 70]), 40.0)
	  self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
	  with self.assertRaises(ZeroDivisionError):
		    average([])
	  with self.assertRaises(TypeError):
		    average(20, 30, 70)

		    
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    class TestStatisticalFunctions(unittest.TestCase):
  File "<pyshell#110>", line 2, in TestStatisticalFunctions
    self.assertEqual(average([20, 30, 70]), 40.0)
NameError: name 'self' is not defined
>>> unittest.main()
		    

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
>>> 
>>>>>>> decdea822f6a158ba446ae39927ab39b83ff7588
