import numpy as np
#put the input file name in the single quote
matrix = np.loadtxt('dm2.test')
print (matrix)

rows = len(matrix) #determine the row size
columns = len(matrix[0]) #determine the column size

#print ("Number of rows is " , rows)
#print ("Number of columns is " , columns)

for i in range(0,319):#first block range
 for j in range(320,390): #second block range
  if matrix[i,j] < 0.6: #define the cutoff here
   print (i+1," ",j+1," ",matrix[i,j])
