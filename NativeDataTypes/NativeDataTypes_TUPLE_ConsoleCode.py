Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = (5,56,24,'hello', 100.1)
>>> a[1]
56
>>> a[1:4]
(56, 24, 'hello')
>>> a.index(100.1)
4
>>> a[0] = 'Hey'
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a[0] = 'Hey'
TypeError: 'tuple' object does not support item assignment
>>> for i in a:
	print(i)

	
5
56
24
hello
100.1
>>> 
