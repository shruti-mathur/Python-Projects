Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> import matplotlib.pyplot as plt
>>> x = np.linspace(-3.0,3.0,3)
>>> x
array([-3.,  0.,  3.])
>>> y = np.linspace(-3.0,3.0,4)
>>> X,Y = np.meshgrid(x,y)
>>> X
array([[-3.,  0.,  3.],
       [-3.,  0.,  3.],
       [-3.,  0.,  3.],
       [-3.,  0.,  3.]])
>>> Y
array([[-3., -3., -3.],
       [-1., -1., -1.],
       [ 1.,  1.,  1.],
       [ 3.,  3.,  3.]])
>>> x = np.linspace(-3.0,3.0,5)
>>> X,Y = np.meshgrid(x,y)
>>> X
array([[-3. , -1.5,  0. ,  1.5,  3. ],
       [-3. , -1.5,  0. ,  1.5,  3. ],
       [-3. , -1.5,  0. ,  1.5,  3. ],
       [-3. , -1.5,  0. ,  1.5,  3. ]])
>>> Y
array([[-3., -3., -3., -3., -3.],
       [-1., -1., -1., -1., -1.],
       [ 1.,  1.,  1.,  1.,  1.],
       [ 3.,  3.,  3.,  3.,  3.]])
>>> Z = np.sqrt(X**2 + Y**2)
>>> ply.contour(X,Y,Z)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    ply.contour(X,Y,Z)
NameError: name 'ply' is not defined
>>> plt.contour(X,Y,Z)
<matplotlib.contour.QuadContourSet object at 0x000001C2C84E8908>
>>> plt.show()
>>> plt.xlim(-5,5)
(-5, 5)
>>> plt.ylim(-5,5)
(-5, 5)
>>> plt.contour(X,Z,Y)
<matplotlib.contour.QuadContourSet object at 0x000001C2C5935320>
>>> plt.show()
>>> plt.contour(X,Y,Z)
<matplotlib.contour.QuadContourSet object at 0x000001C2C7EEE7B8>
>>> plt.show()
>>> cp = plt.contour(X,Y,Z)
>>> plt.clabel(cp, inline=True)
<a list of 9 text.Text objects>
>>> plt.show()
>>> cp = plt.contourf(X,Y,Z)
>>> plt.clabel(cp, inline=True)
<a list of 10 text.Text objects>
>>> plt.show()
>>> x = np.linspace(-3.0,3.0,100)
>>> y = np.linspace(-3.0,3.0,100)
>>> z = np.sqrt(X**2 + Y**2)
>>> X,Y = np.meshgrid(x,y)
>>> Z = np.sqrt(X**2 + Y**2)
>>> cp = plt.contourf(X,Y,Z)
>>> plt.show()
>>> 
