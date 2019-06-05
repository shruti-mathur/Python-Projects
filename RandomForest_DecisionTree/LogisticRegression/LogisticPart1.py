Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from math import exp
>>> def predict(row, coef):
	yhat = coef[0]
	for i in range(len(row)-1):
		yhat += coef[i+1] * row[i]

	
>>> return 1/(1 + exp(-yhat))
SyntaxError: 'return' outside function
>>> def predict(row, coef):
	yhat = coef[0]
	for i in range(len(row)-1):
		yhat += coef[i+1] * row[i]
	return 1/(1 + exp(-yhat))

>>> dataset = [
        [2.7810836,2.550537003,0],
    	[1.465489372,2.362125076,0],
    	[3.396561688,4.400293529,0],
    	[1.38807019,1.850220317,0],
    	[3.06407232,3.005305973,0],
    	[7.627531214,2.759262235,1],
    	[5.332441248,2.088626775,1],
    	[6.922596716,1.77106367,1],
    	[8.675418651,-0.242068655,1],
    	[7.673756466,3.508563011,1]
    ]
>>> coef = [-0.406605464, 0.852573316, -1.104746259]
>>> for i in dataset:
	p = predict(data, coef)
	print("Expected : %3f, Predicted : %3f, Actual : %3d " % (data[-1], p, round(p)))

	
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    p = predict(data, coef)
NameError: name 'data' is not defined
>>> for data in dataset:
	p = predict(data, coef)
	print("Expected : %3f, Predicted : %3f, Actual : %3d " % (data[-1], p, round(p)))

	
Expected : 0.000000, Predicted : 0.298757, Actual :   0 
Expected : 0.000000, Predicted : 0.145951, Actual :   0 
Expected : 0.000000, Predicted : 0.085333, Actual :   0 
Expected : 0.000000, Predicted : 0.219737, Actual :   0 
Expected : 0.000000, Predicted : 0.247059, Actual :   0 
Expected : 1.000000, Predicted : 0.954702, Actual :   1 
Expected : 1.000000, Predicted : 0.862034, Actual :   1 
Expected : 1.000000, Predicted : 0.971773, Actual :   1 
Expected : 1.000000, Predicted : 0.999295, Actual :   1 
Expected : 1.000000, Predicted : 0.905489, Actual :   1 
>>> 
