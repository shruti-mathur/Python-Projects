Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> even = []
>>> for i in range(101):
	if i % 2 == 0:
		even.append(i)

		
>>> even
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> # OR
>>> even = [i for i in range(101) if i % 2 == 0]
>>> even
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> import time
>>> for i in range(10):
	print(i)
	time.sleep(1)

	
0
1
2
3
4
5
6
7
8
9
>>> import datetime
>>> now = datetime.datetime.now
>>> now
<built-in method now of type object at 0x000000006D381D40>
>>> today = datetime.datetime.now()
>>> today
datetime.datetime(2018, 3, 31, 13, 8, 10, 266714)
>>> print(today)
2018-03-31 13:08:10.266714
>>> import calendar
>>> calen = calendar.month(2018,3)
>>> print(calen)
     March 2018
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31

>>> calendar.calendar(2018)
'                                  2018\n\n      January                   February                   March\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n 1  2  3  4  5  6  7                1  2  3  4                1  2  3  4\n 8  9 10 11 12 13 14       5  6  7  8  9 10 11       5  6  7  8  9 10 11\n15 16 17 18 19 20 21      12 13 14 15 16 17 18      12 13 14 15 16 17 18\n22 23 24 25 26 27 28      19 20 21 22 23 24 25      19 20 21 22 23 24 25\n29 30 31                  26 27 28                  26 27 28 29 30 31\n\n       April                      May                       June\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n                   1          1  2  3  4  5  6                   1  2  3\n 2  3  4  5  6  7  8       7  8  9 10 11 12 13       4  5  6  7  8  9 10\n 9 10 11 12 13 14 15      14 15 16 17 18 19 20      11 12 13 14 15 16 17\n16 17 18 19 20 21 22      21 22 23 24 25 26 27      18 19 20 21 22 23 24\n23 24 25 26 27 28 29      28 29 30 31               25 26 27 28 29 30\n30\n\n        July                     August                  September\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n                   1             1  2  3  4  5                      1  2\n 2  3  4  5  6  7  8       6  7  8  9 10 11 12       3  4  5  6  7  8  9\n 9 10 11 12 13 14 15      13 14 15 16 17 18 19      10 11 12 13 14 15 16\n16 17 18 19 20 21 22      20 21 22 23 24 25 26      17 18 19 20 21 22 23\n23 24 25 26 27 28 29      27 28 29 30 31            24 25 26 27 28 29 30\n30 31\n\n      October                   November                  December\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n 1  2  3  4  5  6  7                1  2  3  4                      1  2\n 8  9 10 11 12 13 14       5  6  7  8  9 10 11       3  4  5  6  7  8  9\n15 16 17 18 19 20 21      12 13 14 15 16 17 18      10 11 12 13 14 15 16\n22 23 24 25 26 27 28      19 20 21 22 23 24 25      17 18 19 20 21 22 23\n29 30 31                  26 27 28 29 30            24 25 26 27 28 29 30\n                                                    31\n'
>>> cal = calendar.calendar(2018)
>>> print(cal)
                                  2018

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                1  2  3  4
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       5  6  7  8  9 10 11
15 16 17 18 19 20 21      12 13 14 15 16 17 18      12 13 14 15 16 17 18
22 23 24 25 26 27 28      19 20 21 22 23 24 25      19 20 21 22 23 24 25
29 30 31                  26 27 28                  26 27 28 29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1          1  2  3  4  5  6                   1  2  3
 2  3  4  5  6  7  8       7  8  9 10 11 12 13       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      14 15 16 17 18 19 20      11 12 13 14 15 16 17
16 17 18 19 20 21 22      21 22 23 24 25 26 27      18 19 20 21 22 23 24
23 24 25 26 27 28 29      28 29 30 31               25 26 27 28 29 30
30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5                      1  2
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       3  4  5  6  7  8  9
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      10 11 12 13 14 15 16
16 17 18 19 20 21 22      20 21 22 23 24 25 26      17 18 19 20 21 22 23
23 24 25 26 27 28 29      27 28 29 30 31            24 25 26 27 28 29 30
30 31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                      1  2
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       3  4  5  6  7  8  9
15 16 17 18 19 20 21      12 13 14 15 16 17 18      10 11 12 13 14 15 16
22 23 24 25 26 27 28      19 20 21 22 23 24 25      17 18 19 20 21 22 23
29 30 31                  26 27 28 29 30            24 25 26 27 28 29 30
                                                    31

>>> a = {"id" : 100, "Name" : "Sanaya"}
>>> list(a)
['id', 'Name']
>>> a
{'id': 100, 'Name': 'Sanaya'}
>>> a = {"id" : 100, "Name" : "Sanaya", "Age" : 21, "Salary" : 15000}
>>> list_1 = list(a)
>>> list_1
['id', 'Name', 'Age', 'Salary']
>>> list_2 = list(a.values())
>>> list_2
[100, 'Sanaya', 21, 15000]
>>> list(zip(list_1, list_2))
[('id', 100), ('Name', 'Sanaya'), ('Age', 21), ('Salary', 15000)]
>>> for i in zip(list_1, list_2):
	print(i)

	
('id', 100)
('Name', 'Sanaya')
('Age', 21)
('Salary', 15000)
>>> for  i in enumerate(range(10)):
	print(i)

	
(0, 0)
(1, 1)
(2, 2)
(3, 3)
(4, 4)
(5, 5)
(6, 6)
(7, 7)
(8, 8)
(9, 9)
>>> for i in enumerate(range(10,20)):
	print(i)

	
(0, 10)
(1, 11)
(2, 12)
(3, 13)
(4, 14)
(5, 15)
(6, 16)
(7, 17)
(8, 18)
(9, 19)
>>> for  i, j in enumerate(range(10,20)):
	print(i,j)

	
0 10
1 11
2 12
3 13
4 14
5 15
6 16
7 17
8 18
9 19
>>> 
