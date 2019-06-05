Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [12,45, 'Hello', 12.6]
>>> a[2]
'Hello'
>>> a[-1]
12.6
>>> a[0:2]
[12, 45]
>>> a[1] = 'Welcome'
>>> a
[12, 'Welcome', 'Hello', 12.6]
>>> a.append(5)
>>> a
[12, 'Welcome', 'Hello', 12.6, 5]
>>> a = []
>>> a.append(4,2,5,16)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.append(4,2,5,16)
TypeError: append() takes exactly one argument (4 given)
>>> a.append('add')
>>> a
['add']
>>> a.extend(2,34,21,54,88)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.extend(2,34,21,54,88)
TypeError: extend() takes exactly one argument (5 given)
>>> a.extend([2,54,21,79])
>>> a
['add', 2, 54, 21, 79]
>>> a.append([67,78,90,00])
>>> a
['add', 2, 54, 21, 79, [67, 78, 90, 0]]
>>> a[5]
[67, 78, 90, 0]
>>> a[5][2]
90
>>> a.pop()
[67, 78, 90, 0]
>>> a
['add', 2, 54, 21, 79]
>>> a.insert(0,2)
>>> a
[2, 'add', 2, 54, 21, 79]
>>> a.insert(4,11)
>>> a
[2, 'add', 2, 54, 11, 21, 79]
>>> a.insert(2,3)
>>> a
[2, 'add', 3, 2, 54, 11, 21, 79]
>>> a.insert(4,00)
>>> a
[2, 'add', 3, 2, 0, 54, 11, 21, 79]
>>> a.pop(4)
0
>>> a
[2, 'add', 3, 2, 54, 11, 21, 79]
>>> a.inderx(54)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.inderx(54)
AttributeError: 'list' object has no attribute 'inderx'
>>> a.index(54)
4
>>> a.remove(2)
>>> a
['add', 3, 2, 54, 11, 21, 79]
>>> a.append(11)
>>> a
['add', 3, 2, 54, 11, 21, 79, 11]
>>> a.remove[4][11]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.remove[4][11]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a.remove[11][4]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.remove[11][4]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a.remove[11]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.remove[11]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a.remove(11)
>>> a
['add', 3, 2, 54, 21, 79, 11]
>>> a
['add', 3, 2, 54, 21, 79, 11]
>>> 54 in a
True
>>> 12 in a
False
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> a.remove('add')
>>> a
[3, 2, 54, 21, 79, 11]
>>> a.sort()
>>> a
[2, 3, 11, 21, 54, 79]
>>> a.sort(reverse = True)
>>> a
[79, 54, 21, 11, 3, 2]
>>> a.clear()
>>> a
[]
>>> a.extend([4,65,32,66,8,2,5,3,8])
>>> a
[4, 65, 32, 66, 8, 2, 5, 3, 8]
>>> a.sort()
>>> a
[2, 3, 4, 5, 8, 8, 32, 65, 66]
>>> 
