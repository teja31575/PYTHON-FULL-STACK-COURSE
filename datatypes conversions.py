Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypeb conversions
#int()
int(9)
9
int(8.9)
8
int("teja")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("teja")
ValueError: invalid literal for int() with base 10: 'teja'
int(6+5j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(6+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(6.5)
6.5
float(1)
1.0
float("teja")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("teja")
ValueError: could not convert string to float: 'teja'
float(True)
1.0
float(6+5j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(6+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(False)
0.0
#string
str(1)
'1'
>>> str(2.5)
'2.5'
>>> str("teja")
'teja'
>>> str(5j+2)
'(2+5j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(3)
(3+0j)
>>> complex(4.5)
(4.5+0j)
>>> complex("teja")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    complex("teja")
ValueError: complex() arg is a malformed string
>>> complex(2j+4)
(4+2j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(1)
True
>>> bool(2.4)
True
>>> bool("teja")
True
>>> bool(5j+2)
True
>>> bool(True)
True
>>> bool(False)
False
