Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> users = []
>>> user_1 = ['Age' : 24, 'Name' : 'Wes']
SyntaxError: invalid syntax
>>> user_1 = {'Age' : 24, 'Name' : 'Wes'}
>>> users
[]
>>> users.append(user_1)
>>> users
[{'Age': 24, 'Name': 'Wes'}]
>>> user_2 = {'Age' : 30, 'Name' : 'Laurel'}
>>> users.append(user_2)
>>> user_3 = {'Age' : 16, 'Name' : 'Asher'}
>>> users.append(user_3)
>>> users
[{'Age': 24, 'Name': 'Wes'}, {'Age': 30, 'Name': 'Laurel'}, {'Age': 16, 'Name': 'Asher'}]
>>> for data in users:
	print(data)

	
{'Age': 24, 'Name': 'Wes'}
{'Age': 30, 'Name': 'Laurel'}
{'Age': 16, 'Name': 'Asher'}
>>> 
