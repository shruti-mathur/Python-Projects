Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = {2,65,25,0,'Hey', 53}
>>> type(s)
<class 'set'>
>>> a = {'Age' : 23, 'Name' : 'Sanaya'}
>>> type(a)
<class 'dict'>
>>> s = {2,65,25,0,'Hey', 53}
>>> type(s)
<class 'set'>
>>> s1 = {5,7,5,22,11}
>>> s.intersection(s1)
set()
>>> s1 = {53,7,2,11}
>>> s.intersection(s1)
{2, 53}
>>> s.union(s1)
{0, 65, 2, 7, 11, 53, 25, 'Hey'}
>>> b = [1,4,2,2,5,8,9,6]
>>> type(b)
<class 'list'>
>>> set(b)
{1, 2, 4, 5, 6, 8, 9}
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s[2]
TypeError: 'set' object does not support indexing
>>> 
