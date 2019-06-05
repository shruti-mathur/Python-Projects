Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 20
>>> b = 10
>>> c = a > b
>>> c
True
>>> c = a < b
>>> c
False
>>> a is not b
True
>>> a = b
>>> a
10
>>> list_1 = [12,43,23,63,56,41]
>>> list_2 = list_1
>>> list_2
[12, 43, 23, 63, 56, 41]
>>> list_1[1] = "Hey"
>>> list_1
[12, 'Hey', 23, 63, 56, 41]
>>> list_2
[12, 'Hey', 23, 63, 56, 41]
>>> a = 21
>>> b = 18
>>> id(a)
1832477536
>>> id(b)
1832477440
>>> a = b
>>> id(a)
1832477440
>>> id(b)
1832477440
>>> list_1 = [12,'Hey',23,63,56,41]
>>> list_2
[12, 'Hey', 23, 63, 56, 41]
>>> list_3 = list_1[:]
>>> list_3
[12, 'Hey', 23, 63, 56, 41]
>>> list_1 is list_3
False
>>> id(list_1)
386926256712
>>> id(list_3)
386926331976
>>> id(list_2)
386926086984
>>> list_1[0] = "Bye"
>>> list_1
['Bye', 'Hey', 23, 63, 56, 41]
>>> list_1 = ['Bye', 'Hey',23,[63,56,41],10.5,11.5]
>>> list_1
['Bye', 'Hey', 23, [63, 56, 41], 10.5, 11.5]
>>> list_3 = list_1[:]
>>> list_1[0] = 0
>>> list_1
[0, 'Hey', 23, [63, 56, 41], 10.5, 11.5]
>>> list_3
['Bye', 'Hey', 23, [63, 56, 41], 10.5, 11.5]
>>> list_1[3][0] = "Go"
>>> list_1
[0, 'Hey', 23, ['Go', 56, 41], 10.5, 11.5]
>>> list_3
['Bye', 'Hey', 23, ['Go', 56, 41], 10.5, 11.5]
>>> import copy
>>> list_3 = copy.deepcopy(list_1)
>>> list_3
[0, 'Hey', 23, ['Go', 56, 41], 10.5, 11.5]
>>> list_1
[0, 'Hey', 23, ['Go', 56, 41], 10.5, 11.5]
>>> list_1[3][0] = "Python"
>>> list_1
[0, 'Hey', 23, ['Python', 56, 41], 10.5, 11.5]
>>> list_3
[0, 'Hey', 23, ['Go', 56, 41], 10.5, 11.5]
>>> 
