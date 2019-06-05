Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = "Lets do this"
\
>>> a[0]
'L'
>>> a[-2]
'i'
>>> a[0:5]
'Lets '
>>> a[3:6]
's d'
>>> a[3:6]      # this will go till 6-1 = 5th position
's d'
>>> a[-1:-5]
''
>>> a[-2:-5]
''
>>> b = [5,3,2,5,6,8,9,4]
>>> b[::-1]
[4, 9, 8, 6, 5, 2, 3, 5]
>>> a = "Lets do this"
>>> a[0:11:2]
'Lt oti'
>>> a[0::2]
'Lt oti'
>>> a[::2]
'Lt oti'
>>> 
