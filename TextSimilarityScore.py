Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str_1 = "This is python programming and python is used for machine learning"
>>> word_token = str_1.split()
>>> word_token
['This', 'is', 'python', 'programming', 'and', 'python', 'is', 'used', 'for', 'machine', 'learning']
>>> word_token = set(str_1.split())
>>> word_token
{'machine', 'python', 'used', 'learning', 'for', 'This', 'programming', 'and', 'is'}
>>> str_2 = "R programming used for data analysis"
>>> from collections import *
>>> def DistCalc(str_1, str_2):
	str_split_1 = set(str_1.split())
	str_split_2 = set(str_2.split())
	return len(str_split_1 & str_split_2) / len(str_split_1 | str_split_2)

>>> DistCalc("Hello", "Hello")
1.0
>>> DistCalc("Machine", "Learning")
0.0
>>> set(str_1) & set(str_2)
{'y', 'g', 'm', 'd', ' ', 'a', 'r', 't', 'e', 'o', 'u', 'f', 'l', 'i', 'n', 'p', 's'}
>>> str_1
'This is python programming and python is used for machine learning'
>>> x = set(str_1.split())
>>> x
{'machine', 'python', 'used', 'learning', 'for', 'This', 'programming', 'and', 'is'}
>>> y = set(str_2.split())
>>> y
{'analysis', 'used', 'for', 'R', 'programming', 'data'}
>>> x & y
{'used', 'for', 'programming'}
>>> x = set(str_1.lower().split())
>>> x
{'machine', 'python', 'used', 'learning', 'for', 'is', 'programming', 'and', 'this'}
>>> y = set(str_2.lower().split())
>>> y
{'analysis', 'used', 'for', 'r', 'programming', 'data'}
>>> x | y
{'analysis', 'machine', 'python', 'used', 'learning', 'for', 'is', 'programming', 'r', 'and', 'this', 'data'}
>>> len(x & y) / len(x | y)
0.25
>>> 
