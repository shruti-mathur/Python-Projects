Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [2,6,7,99,0]
>>> type(a)
<class 'list'>
>>> a = (2,6,7,99,0)
>>> type(a)
<class 'tuple'>
>>> users = {'id' : 100, 'Name' : 'Geeta', 'Age' : 24}
>>> users
{'id': 100, 'Name': 'Geeta', 'Age': 24}
>>> users['id']
100
>>> users['Name'] = 'Sanaya'
>>> users
{'id': 100, 'Name': 'Sanaya', 'Age': 24}
>>> users['Course'] = 'IT'
>>> users
{'id': 100, 'Name': 'Sanaya', 'Age': 24, 'Course': 'IT'}
>>> users.keys()
dict_keys(['id', 'Name', 'Age', 'Course'])
>>> users.values()
dict_values([100, 'Sanaya', 24, 'IT'])
>>> dict_items()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    dict_items()
NameError: name 'dict_items' is not defined
>>> users.items()
dict_items([('id', 100), ('Name', 'Sanaya'), ('Age', 24), ('Course', 'IT')])
>>> for data in users:
	print(data)

	
id
Name
Age
Course
>>> for data in users.values():
	print(data)

	
100
Sanaya
24
IT
>>> for data in users.items():
	print(data)

	
('id', 100)
('Name', 'Sanaya')
('Age', 24)
('Course', 'IT')
>>> users.pop()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    users.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> users.pop('id')
100
>>> users
{'Name': 'Sanaya', 'Age': 24, 'Course': 'IT'}
>>> users = {'id' : [101,102,103,104], "Name" : ['wes', 'laurel', 'asher', 'michela']}
>>> users
{'id': [101, 102, 103, 104], 'Name': ['wes', 'laurel', 'asher', 'michela']}
>>> usera['id']
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    usera['id']
NameError: name 'usera' is not defined
>>> users['id']
[101, 102, 103, 104]
>>> users['Name'][3]
'michela'
>>> users['Name'][3] = 'AnnaMae'
>>> users
{'id': [101, 102, 103, 104], 'Name': ['wes', 'laurel', 'asher', 'AnnaMae']}
>>> user_id = users['id']
>>> user_id.append(105)
>>> users
{'id': [101, 102, 103, 104, 105], 'Name': ['wes', 'laurel', 'asher', 'AnnaMae']}
>>> 
